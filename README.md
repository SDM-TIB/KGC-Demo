# KGC-Demo

This demo demonstrates how to execute the Knowledge Graph Creation Pipeline (KGC) for the ([Knowledge4Covid](https://www.sciencedirect.com/science/article/pii/S1570826822000440)) usecase.
A subset of the data used in the Knowledge4Covid paper is used for the demo.
Pubby is configured with the reserved domain (https://research.tib.eu/covid-19).

This [Video](https://drive.google.com/file/d/1NkCe-YVNLWVkTS7GkbCTZ5Z1j_Vrhexe/view?usp=sharing
) provides a general overview of how to run the pipeline or configure it for your own KG.

# Pipeline Creation

This directory contains the instructions for running the KGC pipeline

- `scripts` - contains scripts used for transforming sources to RDF and loading it to triple store (Virtuoso)
      - `virtuoso-script.sh`  - used to remotely connect and load data using `isql-v` tool of virtuoso on command line
      - `load_to_virtuos.py` - used to load the transformed RDF data to virtuoso using the `virtuoso-script.sh` script
- `docker-compose.yml` - docker compose setup for transforming data to RDF and load it to `Virtuoso` triple store.

# Downloading the required data

First we need to download the raw data that is going to be integrated into the created Knowledge Graph.
The data can be downloaded using this ([link](https://tib.eu/cloud/s/6HNEDLEdCdGztjz))

After downloading the data, the (data) directory should be placed under CreationPipeline directory



# Running the docker containers
To start the docker containers, run the following command
(Prerequisite: *Docker-ce*, *Docker-compose*)
```bash
docker-compose up -d
```
This command will download and start the three docker containers used in our pipeline
1) SDM-RDFizer
2) SPARQL Endpoint
3) Dereferencing Interface (Pubby)
4) Federated Query Engine (DeTrusty)
5) SHACL validator (Trav-SHACL)

Once the docker containers are up and running, execute the following command to fix the URLs of Pubby (the dereferencing tool)
```bash
docker exec -it covid19_pubby cp -r /usr/local/tomcat/webapps/pubby/. /usr/local/tomcat/webapps/ROOT/

```

# Creating RDF Dump using SDM-RDFizer

## Run `rdfizer` tool to create the RDF dump according to the above configuration and mapping files included in this config.

The docker container created above using the docker-compose.yaml file will attach this repository as volume at `/data` endpoint

```bash

docker exec -it covid19_sdmrdfizer /data/scripts/run_rdfizier.sh

```

This will create the RDF dumps according the configuration files in KGC-DIS directory, and store the RDF dump in `/rdf` directory, 
You can find the raw RDF file in `.nt` serialization inside 

- Load the RDF dump to Virtuoso


To load the generated RDF dump in step 2, we will use a script included in `scripts` folder as follows:

```bash

docker exec -it covid19_sdmrdfizer python3 /data/scripts/load_to_virtuoso.py

```
This script will also load the mappings and ontology data into the mappings and ontology SPARQL endpoint
Before running this, make sure you update the environmental variable in the `docker-compose.yml` file.

4. Open [http://localhost:8891/sparql](http://localhost:8891/sparql) in your browser, and you will get access to the created Knowledge Graph

## Validating the Knowledge Graph using Trav-SHACL
The generated Knowledge Graph can be validated against integrity constraints defined in SHACL by using `Trav-SHACL`.
The example constraints are in the directory `Trav-SHACL`.
You can either run the command

```bash

docker exec -it covid19_travshacl bash -c "python3 main.py -d /constraints http://covid19kg:8890/sparql /output/k4covid_validation/ DFS --heuristics TARGET IN BIG --selective --outputs"

```

you will find the result of the validation in the `output` directory or

5. Open [http://localhost:5001/validate](http://localhost:5001/validate) in your browser to access the interface of `Trav-SHACL`.

## Querying the Knowledge Graph using DeTrusty

As an alternative to using Virtuoso directly (see above), you can use `DeTrusty` to query the Knowledge Graph.
`DeTrusty` is a query engine enabling access to SPARQL endpoints.
Using `DeTrusty` you can also retrieve data from other sources, and, hence, execute a federated query.

6. Open [http://localhost:5002/sparql](http://localhost:5002/sparql) in your browser to get access to the YASGUI connected to `DeTrusty`.

We provide the source description needed for `DeTrusty`. However, they can be recomputed using the following command:

```bash

docker exec -it covid19_detrusty bash -c "python3 /DeTrusty/create_source_description.py && /DeTrusty/Scripts/restart_workers.sh"

```
