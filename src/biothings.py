from biothings_helper import construct_url, find_api, find_value_from_output_type, find_id_from_uri
from config import AVAILABLE_ENDPOINTS

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
				_api = AVAILABLE_ENDPOINTS[_endpoint]["api"]
				_url = construct_url(_endpoint, _input_id, _input_type)
				_value = find_value_from_output_type(_url, _endpoint, _output_type)
				if _input_id not in output:
					output[_input_id] = [{'source': _api, _output_type: _value}]
				else:
					output[_input_id].append({'source': _api, _output_type: _value})
		return output

'''
	def list_handler(self, input_id_list, input_type, output_type):
		output_id_list = []
		for _input_id in input_id_list:
			ih = IdHandler(_input_id, input_type)
			output_ids = ih.retrieve_id(output_type)
			if type(output_ids) == list:
				for _output_id in output_ids:
					output_id_list.append(_output_id)
			else:
				output_id_list.append(output_ids)
		return output_id_list
'''

class IdHandler():
	'''
	Given id/ids and their type, 
	fetch all available APIs providing annotate or query service
	fetch all IDs related by annotate or query api

	'''
	def __init__(self, ids, type):
		self._ids = ids
		self._type = type
		self.annotate_api_id = find_annotate_api_ids(self._type)
		self.query_api_id = find_query_api_ids(self._type)
		self.available_annotate_id = []
		self.available_query_id = []
		for _api, _ids in self.annotate_api_id.items():
			for _id in _ids:
				self.available_annotate_id.append(_id)
		for _api, _ids in self.query_api_id.items():
			for _id in _ids:
				self.available_query_id.append(_id)		

	def available_apis(self):
		print('Available annotate APIs: {}'.format(self.annotate_api_id.keys()))
		print('Available query APIs: {}'.format(self.query_api_id.keys()))

	def available_ids(self):
		print('Available ids from annotate apis: {}'.format(self.available_annotate_id))
		print('Available ids from query apis: {}'.format(self.available_query_id))

	def retrieve_id(self, output_type):
		if output_type in self.available_annotate_id:
			for _api, _id in self.annotate_api_id.items():
				if output_type in _id:
					return find_value_from_output_type(_api, self._ids, output_type)
		elif output_type in self.available_query_id:
			for _api, _id in self.query_api_id.items():
				if output_type in _id:
					return query_ids_from_output_type(_api, self._type, self._ids)
		else:
			print("coundn't")
