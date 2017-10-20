from config import AVAILABLE_API_ENDPOINTS
from biothings_helper import find_value_from_output_type, query_ids_from_output_type

def uri_query(input_value, input_name, output_name):
	api_results = api_lookup(input_name, output_name)
	if api_results:
		print('{} api(s) could be utilized based on the input_type, output_type you provided: {}'.format(len(api_results), [_doc['api'] for _doc in api_results]))
		uri_query_results = []
		for _result in api_results:
			if _result['type'] == 'annotate':
				uri_query_results.append({_result['api']: find_value_from_output_type(_result, input_value, output_name)})
			elif _result['type'] == 'query':
				uri_query_results.append({_result['api']: query_ids_from_output_type(_result, input_name, input_value)})
		for query_result in uri_query_results:
			for api, value in query_result.items():
				print('{} returns the following results based on your query: {}'.format(api, value))
		return uri_query_results


def api_lookup(input_name, output_name):
	results = []
	for _endpoint in AVAILABLE_API_ENDPOINTS:
		if input_name in _endpoint['input'] and output_name in _endpoint['output']:
			results.append(_endpoint)
	if results:
		return results
	else:
		print('no api could be found taking input {}, and return output {}'.format(input_name, output_name))