from DeTrusty.Molecule.MTCreation import create_rdfmts

endpoints = {
    "https://labs.tib.eu/sdm/covid19kg/sparql": {
        "mappings": [
            "/data/mappings/Treatment/CovidTreatment.ttl",
            "/data/mappings/drug/drug_target_interaction.ttl",
            "/data/mappings/drug/toxicity.ttl",
            "/data/mappings/drug/drug_drug_interaction.ttl",
            "/data/mappings/drug/target.ttl",
            "/data/mappings/drug/drug_toxicity_interaction.ttl",
            "/data/mappings/drug/drug_disorder_interaction.ttl",
            "/data/mappings/drug/enzyme.ttl",
            "/data/mappings/drug/drug_sideeffect_interaction.ttl",
            "/data/mappings/drug/NCRD.ttl",
            "/data/mappings/drug/drug_enzyme_interaction.ttl",
            "/data/mappings/drug/disorder.ttl",
            "/data/mappings/drug/drug_cui.ttl",
            "/data/mappings/drug/CRD.ttl",
            "/data/mappings/drug_predictions/drug_target_predictions.ttl",
            "/data/mappings/drug_predictions/drug_enzyme_predictions.ttl",
            "/data/mappings/drug_predictions/drug_sideeffect_predictions.ttl",
            "/data/mappings/publication/has_topic.ttl",
            "/data/mappings/publication/cord-19_metadata.ttl",
            "/data/mappings/publication/cord-19_relations.ttl",
            "/data/mappings/publication/cord-19_entities.ttl",
            "/data/mappings/publication/mentioned_in.ttl",
            "/data/mappings/publication/semrep_LC_resources.ttl",
            "/data/mappings/publication/publication_LC_journal_types.ttl",
            "/data/mappings/publication/publication_LC_authors.ttl",
            "/data/mappings/publication/publication.ttl",
            "/data/mappings/publication/annotation.ttl",
            "/data/mappings/publication/semrep.ttl",
            "/data/mappings/annotation/all_CUIs.ttl",
            "/data/mappings/annotation/CUI_wikidata_dbpedia.ttl"
        ]
    },
    "https://dbpedia.org/sparql": {
        "types": [
            "http://dbpedia.org/ontology/Drug",
            "http://dbpedia.org/ontology/Protein",
            "http://dbpedia.org/ontology/Enzyme",
            "http://dbpedia.org/ontology/Disease",
            "http://dbpedia.org/ontology/Gene"
        ]
    },
    "https://query.wikidata.org/sparql": {
        "types": [
            "http://www.wikidata.org/entity/Q8386",
            "http://www.wikidata.org/entity/Q718753",
            "http://www.wikidata.org/entity/Q8047",
            "http://www.wikidata.org/entity/Q104053",
            "http://www.wikidata.org/entity/Q12136",
            "http://www.wikidata.org/entity/Q96337364",
            "http://www.wikidata.org/entity/Q45959"
        ]
    }
}

config = create_rdfmts(endpoints)

