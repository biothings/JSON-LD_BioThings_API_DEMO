from jsonld_processor import fetch_value_by_uri, load_context, nquads_transform
from utils.mongo import get_src_db
#from biothings_helper import Biothingsexplorer

def get_discrepancy_id(output_file_name, mongo_collection, uri):
	src = get_src_db()
	context = load_context('mygene.info')
	data = src[mongo_collection].find()
	with open(output_file_name, 'w') as f:
		for _doc in data:
			_doc.update(context)
			jsonld_doc = nquads_transform(_doc)
			rsid = fetch_value_by_uri(jsonld_doc, uri)
			if type(rsid) == list:
				f.write(_doc['_id'] + "\n")

def get_discrepancy_id_url(output_file_name, mongo_collection, uri):
	bt = Biothingsexplorer()
	doc = 
	data = src[mongo_collection].find()
	with open(output_file_name, 'w') as f:
		for _doc in data:
			_doc.update(context)
			jsonld_doc = nquads_transform(_doc)
			rsid = fetch_value_by_uri(jsonld_doc, uri)
			if type(rsid) == list:
				f.write(_doc['_id'] + "\n")



