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
   
2. Look for all works of all DDB objects related to "Schillers Räuber"
    ```
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX gnd: <http://d-nb.info/gnd/>
    PREFIX gndo: <http://d-nb.info/standards/elementset/gnd#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX frbr: <http://purl.org/vocab/frbr/core#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    
    SELECT DISTINCT ?ddbitem ?title ?work ?author
    WHERE {
      ?work rdf:type fabio:Work .
      ?work dcterms:creator ?author .
      ?work fabio:hasPortrayal ?ddbitem .
      ?author foaf:name ?author_name FILTER regex(str(?author_name), "Schiller", "i") .
      ?work dcterms:title ?title FILTER regex(str(?title), "R.*uber", "i") .
            }
    ```

3. Look for digitized copies of "Die Räuber"
    ```
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX gnd: <http://d-nb.info/gnd/>
    PREFIX gndo: <http://d-nb.info/standards/elementset/gnd#>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX frbr: <http://purl.org/vocab/frbr/core#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    
        SELECT DISTINCT ?title ?ddbitem ?type ?epub
        WHERE {
          ?work rdf:type fabio:Work ;
                fabio:hasRealization ?expression .
          ?expression fabio:hasRepresentation ?ddbitem ;
                dcterms:title ?title 
                FILTER regex(str(?title), "Die R.*uber", "i") .
          ?ddbitem dcterms:type ?type ;
                fabio:hasReproduction ?di .
          ?di fabio:isExemplarOf ?epub .        
    }
    ```
   - Click [here](https://ise-fizkarlsruhe.github.io/ddbkg/cq/cq03.html) for results   