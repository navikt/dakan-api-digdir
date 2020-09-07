API_RDF = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://xmlns.com/foaf/0.1/> .

<API.DatakatalogAPI> a dcat:DataService ;
    dct:description "Datakatalog api for s3 og elastic search"@nb ;
    dct:publisher <https://data.brreg.no/enhetsregisteret/oppslag/enheter/889640782> ;
    dct:title "Datakatalog API"@nb ;
    dcat:endpointDescription <https://data.nav.no/api/swagger/ui> ;
    dcat:endpointURL <https://data.nav.no/api> .

<https://data.nav.no> a dcat:Catalog ;
    dct:publisher <https://data.brreg.no/enhetsregisteret/oppslag/enheter/889640782> ;
    dct:title "NAV åpne APIer"@nb ;
    dcat:service <API.DatakatalogAPI> ;
    ns1:homepage <https://data.nav.no> .\n\n"""
