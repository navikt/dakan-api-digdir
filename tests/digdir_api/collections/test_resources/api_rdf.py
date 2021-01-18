API_RDF = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://xmlns.com/foaf/0.1/> .

<API.Arbeidsplassen> a dcat:DataService ;
    dct:description "Stillingssøk på Arbeidsplassen inneholder en oversikt over de fleste aktive ledige stillinger. Stillingssøket inneholder både stillinger som er registrert direkte hos NAV samt hentet inn fra en rekke nettsteder Stillingsdata meldes og registreres i NAV basert på (Lov om arbeidsmarkedstjenester § 7,2004). Ikke alle stillinger som blir meldt til NAV blir publisert på Arbeidsplassen. Du finner dokumentasjon av applikasjonsgrensesnittet på https://github.com/navikt/pam-public-feed"@nb ;
    dct:publisher <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/889640782> ;
    dct:title "Arbeidsplassen"@nb ;
    dcat:endpointDescription <https://arbeidsplassen.nav.no/public-feed/swagger> ;
    dcat:endpointURL <https://arbeidsplassen.nav.no/public-feed/api/v1> .

<https://data.nav.no> a dcat:Catalog ;
    dct:publisher <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/889640782> ;
    dct:title "NAV åpne APIer"@nb ;
    dcat:service <API.Arbeidsplassen> ;
    ns1:homepage <https://data.nav.no> .\n\n"""
