AVAILABLE_API_SOURCES={"mygene.info": {
 	"annotate_ids": ["http://identifiers.org/ncbigene/"],
 	"query_ids": ["http://identifiers.org/uniprot/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/wikipathways/", "http://identifiers.org/pubmed/"],
 	"annotate_syntax": "http://mygene.info/v3/gene/{{input}}?dotfield=true",
 	"query_syntax": "http://mygene.info/v3/query?q={{input}}&fetch_all=TRUE&fields=_id",
  "description": "gene annotation service",
 	"jsonld": {
 		"context_file_path": "context/mygene_context.json"
 	}
 },
  "myvariant.info": {
  	"annotate_ids": ["http://identifiers.org/hgvs/"],
  	"query_ids": ["http://identifiers.org/ncbigene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/dbsnp/", "http://identifiers.org/pubmed/", "http://identifiers.org/uniprot/", "http://identifiers.org/omim/"],
  	"annotate_syntax": "http://myvariant.info/v1/variant/{{input}}?dotfield=true",
  	"query_syntax": "http://myvariant.info/v1/query?q={{input}}&fetch_all=TRUE&fields=_id",
  	"jsonld": {
  		"context_file_path": "context/myvariant_context.json"
  	}
  },
  "mychem.info": {
  	"annotate_ids": ["http://identifiers.org/drugbank/"],
  	"query_ids": ["http://identifiers.org/dbsnp/", "http://identifiers.org/pubchem.compound/", "http://identifiers.org/drugbank/", "http://identifiers.org/pubmed/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/uniprot/", "http://identifiers.org/clinicaltrials/"],
  	"annotate_syntax": "http://c.biothings.io/v1/drug/{{input}}?dotfield=true",
  	"query_syntax": "http://c.biothings.io/v1/query?q={{input}}&fetch_all=TRUE&fields=_id",
  	"jsonld": {
  		"context_file_path": "context/mychem_context.json"
  	}
  }
}

AVAILABLE_API_ENDPOINTS = [
  {
    "url_syntax": "http://mygene.info/v3/query?q={{input}}&fetch_all=TRUE&fields=_id",
    "input": ["http://identifiers.org/uniprot/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/wikipathways/", "http://identifiers.org/pubmed/"],
    "output": ["http://identifiers.org/ncbigene/"],
    "jsonld": "context/mygene_query_context.json",
    "api": "mygene.info",
    "type": "query"
  },
  {
    "url_syntax": "http://mygene.info/v3/gene/{{input}}",
    "input": ["http://identifiers.org/ncbigene/"],
    "output": ["http://identifiers.org/uniprot/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/wikipathways/", "http://identifiers.org/pubmed/"],
    "jsonld": "context/mygene_context.json",
    "api": "mygene.info",
    "type": "annotate"
  },
  {
    "url_syntax": "http://myvariant.info/v1/query?q={{input}}&fetch_all=TRUE&fields=_id",
    "input": ["http://identifiers.org/ncbigene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/dbsnp/", "http://identifiers.org/pubmed/", "http://identifiers.org/uniprot/"],
    "output": ["http://identifiers.org/hgvs/"],
    "jsonld": "context/myvariant_query_context.json",
    "api": "myvariant.info",
    "type": "query"
  },
  {
    "url_syntax": "http://myvariant.info/v1/variant/{{input}}",
    "input": ["http://identifiers.org/hgvs/"],
    "output": ["http://identifiers.org/ncbigene/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/dbsnp/", "http://identifiers.org/pubmed/", "http://identifiers.org/uniprot/"],
    "jsonld": "context/myvariant_context.json",
    "api": "myvariant.info",
    "type": "annotate"
  },
  {
    "url_syntax": "http://mychem.info/v1/query?q={{input}}&fetch_all=TRUE&fields=_id",
    "input": ["http://identifiers.org/dbsnp/", "http://identifiers.org/pubchem.compound/", "http://identifiers.org/drugbank/", "http://identifiers.org/pubmed/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/uniprot/", "http://identifiers.org/clinicaltrials/"],
    "output": ["http://identifiers.org/inchikey/"],
    "jsonld": "context/mychem_query_context.json",
    "api": "mychem.info",
    "type": "query"
  },
  {
    "url_syntax": "http://mychem.info/v1/drug/{{input}}",
    "input": ["http://identifiers.org/inchikey/", "http://identifiers.org/drugbank/"],
    "output": ["http://identifiers.org/dbsnp/", "http://identifiers.org/pubchem.compound/", "http://identifiers.org/drugbank/", "http://identifiers.org/pubmed/", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/uniprot/", "http://identifiers.org/clinicaltrials/"],
    "jsonld": "context/mychem_query_context.json",
    "api": "mychem.info",
    "type": "annotate"
  }
]
