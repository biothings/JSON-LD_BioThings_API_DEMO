AVAILABLE_IDS= {"ensembl_gene_id": {
	"uri": "http://identifiers.org/ensembl.gene/",
	"example": "ENSG00000139618"
},
 "entrez_gene_id": {
 	"uri": "http://identifiers.org/ncbigene/",
 	"example": 1017
 },
 "hgnc_gene_symbol": {
 	"uri": "http://identifiers.org/hgnc.symbol/",
 	"example": "CDK7"
 },
 "hgvs_id": {
 	"uri": "http://identifiers.org/hgvs/",
 	"example": "chr6:123456G>A"
 },
 "dbsnp_id": {
 	"uri": "http://identifiers.org/dbsnp/",
 	"example": "rs123456"
 },
 "drugbank_id": {
 	"uri": "http://identifiers.org/drugbank/",
 	"example": "DB00002"
 },
 "pubchem_id": {
 	"uri": "http://identifiers.org/pubchem.compound/",
 	"example": 100101
 },
 "pubmed_id": {
 	"uri": "http://identifiers.org/pubmed/",
 	"example": 16333295
 },
 "uniprot_id": {
 	"uri": "http://identifiers.org/uniprot/",
 	"example": "P62158"
 },
 "wikipathway_id": {
 	"uri": "http://identifiers.org/wikipathways/",
 	"example": "WP100"
 },
 "clinicaltrial_id": {
 	"uri": "http://identifiers.org/clinicaltrials/",
 	"example": "NCT01314001"
 }}

AVAILABLE_API_SOURCES={"mygene.info": {
 	"annotate_ids": ["entrez_gene_id", "ensembl_gene_id"],
 	"query_ids": ["uniprot_id", "ensembl_gene_id", "hgnc_gene_symbol", "wikipathway_id", "pubmed_id"],
 	"annotate_syntax": "http://mygene.info/v3/gene/{{input}}?dotfield=true",
 	"query_syntax": "http://mygene.info/v3/query?q={{input}}",
  "description": "gene annotation service",
 	"jsonld": {
 		"context_file_path": "context/mygene_context.json"
 	}
 },
  "myvariant.info": {
  	"annotate_ids": ["hgvs_id"],
  	"query_ids": ["entrez_gene_id", "hgnc_gene_symbol", "ensembl_gene_id", "dbsnp_id", "pubmed_id", "uniprot_id"],
  	"annotate_syntax": "http://myvariant.info/v1/variant/{{input}}?dotfield=true",
  	"query_syntax": "http://myvariant.info/v1/query?q={{input}}",
  	"jsonld": {
  		"context_file_path": "context/myvariant_context.json"
  	}
  },
  "mydrug.info": {
  	"annotate_ids": ["drugbank_id"],
  	"query_ids": ["dbsnp_id", "pubchem_id", "drugbank_id", "pubmed_id", "hgnc_gene_symbol", "uniprot_id", "clinicaltrial_id"],
  	"annotate_syntax": "http://c.biothings.io/v1/drug/{{input}}?dotfield=true",
  	"query_syntax": "http://c.biothings.io/v1/query?q={{input}}",
  	"jsonld": {
  		"context_file_path": "context/mydrug_context.json"
  	}
  }
}


CLIENT_LIST = {"mygene.info", "myvariant.info", "mydrug.info"}

