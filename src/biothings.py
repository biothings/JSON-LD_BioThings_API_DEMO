from biothings_helper import construct_url, find_api, find_value_from_output_type, find_id_from_uri
from config import AVAILABLE_API_ENDPOINTS

def dict2list(_dict):
	results = []
	for k,v in _dict.items():
		for _item in v:
			for _k, _v in _item.items():
				if _k != 'source':
					if type(_v) == list:
						for _id in _v:
							if _id:
								results.append(_id)
					else:
						if _v:
							results.append(_v)
	results = list(set(results))
	results.sort()
	return results


class IdListHandler():

	def list_handler(self, input_id_list, _input_type, _output_type, uri=False):
		if uri:
			_input_type = find_id_from_uri(_input_type)
			_output_type = find_id_from_uri(_output_type)
		output = {}
		for _input_id in input_id_list:
			available_endpoint_list = find_api(_input_type, _output_type)
			for _endpoint in available_endpoint_list:
				_api = AVAILABLE_API_ENDPOINTS[_endpoint]["api"]
				_url = construct_url(_endpoint, _input_id, _input_type)
				_value = find_value_from_output_type(_url, _endpoint, _output_type)
				if _input_id not in output:
					output[_input_id] = [{'source': _api, _output_type: _value}]
				else:
					output[_input_id].append({'source': _api, _output_type: _value})
		return output


def get_biothings(api, id, fields_uri):
	'''
	Given id/ids and output type, 
	fetch all available APIs providing annotate or query service
	fetch all IDs related by annotate or query api

	'''
	endpoint_id = None
	for i in range(0, len(AVAILABLE_API_ENDPOINTS)):
		if AVAILABLE_API_ENDPOINTS[i]['api'] == api and AVAILABLE_API_ENDPOINTS[i]['type'] == 'get':
			endpoint_id = i
	if endpoint_id:
		_url = construct_url(endpoint_id, id, find_id_from_uri(fields_uri))
		_value = find_value_from_output_type(_url, endpoint_id, find_id_from_uri(fields_uri))
		return _value
