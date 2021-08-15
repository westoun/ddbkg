#### Sample SPARQL Queries for [DDB-KG](http://ddbkg.fiz-karlsruhe.de)

1. Look for all works of author "Schiller"
    ```
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX gnd: <http://d-nb.info/gnd/>
    PREFIX gndo: <http://d-nb.info/standards/elementset/gnd#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX frbr: <http://purl.org/vocab/frbr/core#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    
    SELECT DISTINCT ?title ?work ?author
    WHERE {
      ?work rdf:type fabio:Work .
      ?work dcterms:creator ?author .
      ?author foaf:name ?author_name FILTER regex(str(?author_name), "Schiller", "i") .
      ?work dcterms:title ?title .
            }
    ```