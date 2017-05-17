from config import AVAILABLE_API_SOURCES
from biothings_helper import find_id_from_uri, find_value_from_output_type, query_ids_from_output_type

def uri_query(input_value, input_type, output_type):
	input_name = find_id_from_uri(input_type)
	output_name = find_id_from_uri(output_type)
	api_results = api_lookup(input_name, output_name)
	if api_results:
		print('{} api(s) could be utilized based on the input_type, output_type you provided: {}'.format(len(api_results), [_doc['api'] for _doc in api_results]))
		uri_query_results = []
		for _result in api_results:
			if _result['type'] == 'annotate':
				uri_query_results.append({_result['api']: find_value_from_output_type(_result['api'], input_value, output_name)})
			elif _result['type'] == 'query':
				uri_query_results.append({_result['api']: query_ids_from_output_type(_result['api'], input_name, input_value)})
		for query_result in uri_query_results:
			for api, value in query_result.items():
				print('{} returns the following results based on your query: {}'.format(api, value))
		return uri_query_results




def api_lookup(input_name, output_name):
	results = []
	for _api in AVAILABLE_API_SOURCES.keys():
		if input_name in AVAILABLE_API_SOURCES[_api]["annotate_ids"] and output_name in AVAILABLE_API_SOURCES[_api]["query_ids"]:
			results.append({'api': _api, 'type': 'annotate'})
		if input_name in AVAILABLE_API_SOURCES[_api]["query_ids"] and output_name in AVAILABLE_API_SOURCES[_api]["annotate_ids"]:
			results.append({'api': _api, 'type': 'query'})
	if results:
		return results
	else:
		print('no api could be found taking input {}, and return output {}'.format(input_name, output_name))