# Pipeline Creation

Required modifications to use the KGCP for another usecase:


- Adding the new Ontology for the new usecase in the following path
```
KGC-Demo/KGC-DIS/
```

- Defining the mappings rules for the new use case datasets under the following path
```
KGC-Demo/KGC-DIS/CSV2RDF-RMLMappingRules/
```


- Configuring the SDM-RDFizer config files related to the new datasets and mappings under the following path
```
KGC-Demo/KGC-DIS/SDM-RDFizer-Configs/
```

- Configuring the SDM-RDFizer config files related to the new datasets and mappings under the following path
```
KGC-Demo/KGC-DIS/SDM-RDFizer-Configs/
```

- Modifying the following environment variables inside the docker-compose file
```

hostname - can always be changed for all the three containers. But should also be changed if mentioned in the depends_on section of another container.

ports - can always be changed but only the left part (host machine port) and not the container port part.

SPARQL_ENDPOINT_IP - the container name of the SPARQL endpoint.

SPARQL_ENDPOINT_USER - the username to manage the SPARQL endpoint.

SPARQL_ENDPOINT_PASSWD - the password to manage the SPARQL endpoint.

SPARQL_ENDPOINT_GRAPH - The reserved domain for the Linked Data Frontend.

SPARQL_ENDPOINT - The URL of the SPARQL endpoint that contains the data and the ontology.

PROJECT_HOMEPAGE_URL - The reserved domain for the Linked Data Frontend.

PROJECT_NAME - The new usecase name.

DEFAULT_RESOURCE - A default resource for the generated KG.

DEFAULT_NAMED_GRAPH - The name of the graph inside the SPARQL endpoint.

COMMON_URI_PREFIX - The reserved domain for the Linked Data Frontend.

PUBBY_ROOT_URL - The reserved domain for the Linked Data Frontend.

```