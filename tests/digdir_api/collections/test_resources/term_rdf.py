TERMS_RDF = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/skosno#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.nav.no> a skos:Collection ;
    rdfs:label "Approved terms"@en,
        "Godkjente begreper"@nb,
        "Godkjende omgrep"@nn ;
    dct:description "NAV approved terms"@en,
        "NAV godkjente begreper"@nb,
        "NAV godkjende omgrep"@nn ;
    dct:publisher <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/889640782> ;
    skos:member <BEGREP-1694> .

<BEGREP-1694> a skos:Concept ;
    dct:modified "2020-05-05"^^xsd:date ;
    dct:publisher <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/889640782> ;
    dct:subject ""@en,
        "Ytelsesavdelingen"@nb,
        ""@nn ;
    skosxl:altLabel [ a skosxl:Label ;
            skosxl:literalForm ""@nb ] ;
    skosxl:hiddenLabel [ a skosxl:Label ;
            skosxl:literalForm ""@nb ] ;
    skosxl:prefLabel [ a skosxl:Label ;
            skosxl:literalForm ""@en,
                "Business Use Case (EESSI)"@nb,
                ""@nn ] ;
    dcat:contactPoint [ a vcard:Organization ;
            vcard:hasEmail <mailto:begrepskatalogen@nav.no> ;
            vcard:hasOrganizationName ""@en,
                ""@nb,
                ""@nn ] ;
    ns1:definisjon [ a ns1:Definisjon ;
            rdfs:label ""@en,
                "Et bruksområde av Use Case som beskriver typiske forretningsoperasjoner mellom en aktør på utsiden og en organisasjon."@nb,
                ""@nn ;
            dct:source [ rdfs:label "EESSI Architecture Overview Document"@nb ] ;
            skos:scopeNote ""@en,
                "Business Use Case viser samhandling mellom aktører og forretningsprosesser, og trenger ikke inneholde referanser til teknologi. Forkortelsen BUC inngår i  forkortelses-stammespråket i EESSI som betegnelse på modeller for meldingsflyten mellom aktører i en saksbehandlingsprosess."@nb,
                ""@nn ;
            ns1:forholdTilKilde ns1:basertPåKilde ] .

"""
