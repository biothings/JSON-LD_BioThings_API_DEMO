from config import *
from jsonld_processor import load_context, fetch_doc_from_api, nquads_transform, get_uri_value_pairs,fetch_value_by_uri, flatten_doc
import json

def find_id_from_uri(uri):
    for _id in AVAILABLE_IDS.keys():
        if AVAILABLE_IDS[_id]["uri"] == uri:
            return _id

def uri_to_field_name(uri, api):
    context = load_context(api)
    return [_field for _field, _uri in context["@context"].items() if _uri==uri]

def compose_query_parameter_from_uri(uri, value, api):
    field_name_list = uri_to_field_name(uri, api)
    string = ":" + value + " OR "
    if len(field_name_list) >1:
        return (string.join(field_name_list) + ":" + value)
    else:
        return (field_name_list[0] + ':' + value)

def find_annotate_api_ids(_type):
    '''
    Give an ID, look through all availalble api sources,
    if the ID can be annotated by this API, return API names in a list
    '''
    api_id = {}
    for _source in AVAILABLE_API_SOURCES:
        if "annotate_ids" in AVAILABLE_API_SOURCES[_source] and _type in AVAILABLE_API_SOURCES[_source]["annotate_ids"]:
            api_id[_source] = AVAILABLE_API_SOURCES[_source]['query_ids']
    return api_id

def find_query_api_ids(_type):
    api_id = {}
    for _source in AVAILABLE_API_SOURCES:
        if "query_ids" in AVAILABLE_API_SOURCES[_source] and _type in AVAILABLE_API_SOURCES[_source]["query_ids"]:
            api_id[_source] = AVAILABLE_API_SOURCES[_source]['annotate_ids']
    return api_id

def find_value_from_output_type(_url, endpoint_id, _output_type):
    '''
    given an api, input value
    return the value related to the uri
    '''
    json_doc = fetch_doc_from_api(_url)
    if 'hits' in json_doc and json_doc['hits']:
        json_doc = flatten_doc(json_doc)
        context = json.load(open(AVAILABLE_API_ENDPOINTS[endpoint_id]["jsonld"]))
        json_doc.update(context)
        nquads_doc = nquads_transform(json_doc)
        uri = AVAILABLE_IDS[_output_type]["uri"]
        return fetch_value_by_uri(nquads_doc, uri)
    elif 'hits' not in json_doc:
        json_doc = flatten_doc(json_doc)
        context = json.load(open(AVAILABLE_API_ENDPOINTS[endpoint_id]["jsonld"]))
        json_doc.update(context)
        nquads_doc = nquads_transform(json_doc)
        uri = AVAILABLE_IDS[_output_type]["uri"]
        return fetch_value_by_uri(nquads_doc, uri)

def query_ids_from_output_type(api, _type, _value):
    uri = AVAILABLE_IDS[_type]["uri"]
    query_info = compose_query_parameter_from_uri(uri, _value, api)
    print(query_info)
    id_list = ClientRedirect().get_id_list(api, query_info, fetch_all=True)
    return id_list

def find_api(_input, _output):
    endpoint_list = []
    for i in range(0, len(AVAILABLE_API_ENDPOINTS)):
        if _input in AVAILABLE_API_ENDPOINTS[i]["input"] and _output in AVAILABLE_API_ENDPOINTS[i]["output"]:
            endpoint_list.append(i)
    return endpoint_list

def construct_url(endpoint_id, _input, _input_type):
    endpoint = AVAILABLE_API_ENDPOINTS[endpoint_id]
    if endpoint["type"] == "get":
        url = endpoint["url_syntax"].replace("{{input}}", _input)
        return url
    elif endpoint["type"] == "query":
        uri = AVAILABLE_IDS[_input_type]["uri"]
        query_para = compose_query_parameter_from_uri(uri, _input, endpoint['api'])
        url = endpoint["url_syntax"].replace("{{input}}", query_para)
        return url







