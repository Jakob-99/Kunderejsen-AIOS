# Context / Company Wiki

Dette er repoets **context-mappe** — en levende videnbase om virksomheden, bygget efter principperne for *context engineering* (Andrej Karpathy): giv en AI-agent (eller et nyt menneske) præcis den kontekst, den skal bruge, uden at den skal gætte eller lede.

## Principper

1. **Ét indgangspunkt** — start altid her (`context/README.md`), og lad dig linke videre.
2. **Én kilde til sandhed** — hver oplysning findes ét sted. Andre dokumenter linker til den, de kopierer den ikke.
3. **Kortfattet og konkret** — skrevet så en model kan læse det direkte og handle på det. Ingen marketingsprog, ingen fyld.
4. **Levende dokument** — når noget ændrer sig i virksomheden, opdatér filen med det samme. Forældet kontekst er værre end ingen kontekst.
5. **Placeholders er tilladte** — mangler vi info, markeres det tydeligt som `TODO` frem for at gætte.

## Indhold

Wikien har to lag:

- **`company/*.md`** — menneskelæsbar prosa: hvad tingene betyder, i sammenhæng.
- **`entities/*.yaml` + `relations.yaml`** — maskinlæsbar graf af de samme ting: entities (noder) og deres indbyrdes relationer (kanter). Se [`entities/_schema.md`](entities/_schema.md) for format.

De to lag skal stemme overens: nævner et markdown-dokument en ting/relation, skal den også findes i graf-laget, og omvendt.

| Fil | Indhold |
|---|---|
| [`company/overview.md`](company/overview.md) | Hvad er Figurio, mission, hvad vi laver |
| [`company/brand.md`](company/brand.md) | Visuel identitet og tone of voice |
| [`company/products-services.md`](company/products-services.md) | Produkter, ydelser, hvordan de hænger sammen |
| [`company/organization.md`](company/organization.md) | Team, roller, ansvar |
| [`company/customers-market.md`](company/customers-market.md) | Målgruppe, marked, konkurrenter |
| [`glossary.md`](glossary.md) | Interne begreber og forkortelser |
| [`processes.md`](processes.md) | Centrale arbejdsgange og processer |
| [`entities/`](entities/) | Entities som data (company, product, brand, market, customer_segment, …) |
| [`relations.yaml`](relations.yaml) | Relationer mellem entities |

## Sådan bruges wikien

- **Nyt indhold**: tilføj det i den relevante fil frem for at oprette en ny, medmindre emnet reelt er nyt — opret i så fald en ny fil og link den herfra.
- **Modstrid**: hvis to filer siger noget forskelligt, er det et signal om at én skal opdateres — ikke at begge har ret.
- **AI-agenter** (Claude Code m.fl.) bør læse denne fil først for at få overblik, og derefter kun de underliggende filer der er relevante for opgaven.
