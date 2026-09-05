# Entity/relation-skema

Denne mappe er den **maskinlæsbare** del af context-wikien: virksomheden udtrykt som entities (noder) og relationer (kanter) i en simpel graf. De håndskrevne markdown-filer i `context/company/` er den menneskelæsbare forklaring og linker hertil.

## Entity-fil (`entities/<id>.yaml`)

```yaml
id: kort-unikt-id          # slug, bruges som reference fra relations.yaml
type: company | product | team | person | customer_segment | market | brand
name: Visningsnavn
summary: Én-to sætninger.
attributes:                # frit skema pr. type, udfyld hvad der er relevant
  key: value
status: confirmed | todo    # 'todo' = mangler stadig reelt indhold
```

## Relationer (`relations.yaml`)

Én global liste, så grafen kan læses/forespørges samlet uden at åbne hver entity-fil:

```yaml
- from: entity-id
  type: relation_type       # fx offers, targets, part_of, competes_with, produces
  to: entity-id
  note: valgfri kontekst
```

## Regler

1. Enhver entity, der nævnes i en relation, skal have sin egen fil i denne mappe.
2. Slet aldrig en entity uden at fjerne/opdatere relationerne der peger på den.
3. `status: todo` betyder feltet er et gæt/placeholder — ret det til `confirmed` når indholdet er bekræftet.
