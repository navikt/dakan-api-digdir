API_RDF = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

<https://data.nav.no> a dcat:Catalog ;
    dct:title "NAV åpne APIer"@nb ;
    dcat:service <https://data.nav.no/apier//API.Arbeidsplassen> ;
    foaf:homepage <https://data.nav.no> .

<https://data.nav.no/apier//API.Arbeidsplassen> a dcat:DataService ;
    dct:description "Stillingssøk på Arbeidsplassen inneholder en oversikt over de fleste aktive ledige stillinger. Stillingssøket inneholder både stillinger som er registrert direkte hos NAV samt hentet inn fra en rekke nettsteder Stillingsdata meldes og registreres i NAV basert på (Lov om arbeidsmarkedstjenester § 7,2004). Ikke alle stillinger som blir meldt til NAV blir publisert på Arbeidsplassen. Du finner dokumentasjon av applikasjonsgrensesnittet på https://github.com/navikt/pam-public-feed"@nb ;
    dct:title "Arbeidsplassen"@nb ;
    dcat:endpointDescription <https://arbeidsplassen.nav.no/public-feed/swagger> ;
    dcat:endpointURL <https://arbeidsplassen.nav.no/public-feed/api/v1> .

"""
