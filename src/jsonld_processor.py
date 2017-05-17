import json
import requests
from pyld import jsonld

from config import AVAILABLE_API_SOURCES


def fetch_doc_from_api(url):
    '''
    This function takes an uri, and call the uri
    using requests, and then return a json document
    if the call is valid
    '''
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print("invalid uri: {}".format(url))


def load_context(api):
    '''
    load context file from a specific path
    e.g. mygene.info context file
    '''
    if 'jsonld' in AVAILABLE_API_SOURCES[api]:
        return json.loads(open(AVAILABLE_API_SOURCES[api]["jsonld"]["context_file_path"]).read())

def nquads_transform(doc):
    '''
    This function takes a json-ld document,
    and parse it into nquads format (rdf)
    '''
    t = jsonld.JsonLdProcessor()
    nquads = t.parse_nquads(jsonld.to_rdf(doc, {'format': 'application/nquads'}))['@default']
    return nquads


def jsonld_converter(json_doc, api):
    '''
    give a json doc and api name
    transform it into jsonld_format
    '''
    context = load_context(api)
    json_doc.update(context)
    return jsonld_doc

def fetch_value_by_uri(nquads, uri):
    '''
    give a nquads and a uri,
    find all values related to this uri
    if find multiple values, return a list
    if only single value found, return the item
    '''
    value_list = []
    for item in nquads:
        if item['predicate']['value'] == uri:
            value_list.append(item['object']['value'])
    value = list(set(value_list))
    if len(value) == 1:
        return value[0]
    else:
        return value


def get_uri_list(nquads):
    '''
    give a nquads, return all available uris in it
    '''
    uri_list = list(set([_doc['predicate']['value'] for _doc in nquads]))
    return uri_list

def get_uri_value_pairs(nquads):
    uri_value_pairs = {}
    uri_list = get_uri_list(nquads)
    for _uri in uri_list:
        uri_value_pairs.update({_uri: fetch_value(nquads, _uri)})
    return uri_value_pairs
