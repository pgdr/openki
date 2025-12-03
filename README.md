---
author: Pål Grønås Drange
title: Open KI
institute: Department of Informatics, University of Bergen
theme: metropolis
date: December 4, 2025
aspectratio: 169
header-includes:
  - \usetheme{metropolis}
  - \definecolor{beaublue}{rgb}{0.74, 0.83, 0.9}
  - \setbeamertemplate{frame footer}{\tiny{\textcolor{beaublue}{Open KI 2025 (\insertframenumber/\inserttotalframenumber)}}}
  - \usepackage{tikzsymbols}
  - \usefonttheme{professionalfonts}
  - \usepackage{arev}
  - \usepackage{wasysym}
---



# Klassisk programvare vs ML-systemer

- Klassisk programvare:
  - Program tar input
  - Program kjører (logikk)
  - Program produserer output
- Koden er logikken

# ML-systemer


![](trening.png)


* Treningsdata blir brukt til å lage en statistisk modell

# ML-systemer


![](bruk.png)


* Bruker gir input til systemet som videresender(\*) til modell
* Systemet får output fra modell og gir(\*) til bruker



# Hva er en modell?


![](linear.png)


# Hva er en modell?


![](cubic.png)

# Hva er en modell?


![](decision.png)

# Hva er en modell?


![](neural.png)


# ML-systemets 4 komponenter

1. Treningssystem (kode + infrastruktur)
2. Treningsdata
3. Trent modell (vekter)
4. Tjenestesystem (ML-systemet som bruker modellen)





# Treningdata: den problematiske delen

- Treningdata:
  - Store nettbaserte innhentinger, bøker, kode, proprietære kilder

- Selv om datasett er _tilgjengelige_:
  - inneholder opphavsrettsbeskyttet/proprietært innhold

- I Norge kan det være ulovlig å
  - Laste ned, lagre, redistribuere

- Åpenhet vs. personvern, opphavsrett, forretningshemmeligheter, ulovlig materiale

- Åpne data krever attribusjon (BY)

- Treningskostnader for LLM-er


# Forklarbar KI og inspeksjon

Hvorfor? (XAI)

- Åpne modeller:
  - Inspeksjon av vekter: mekanistisk forklarbarhet, bias, diskriminering
  - Finjustering for nye oppgaver
  - Kontroll over input, output, prompt

- Transparens og kontroll
  - Politisk innhold


# Kontroll over innganger og utganger

* Hva sendes til modellen?  (er noe injisert?)
* Hva returneres fra modellen? (er noe sensurert?)
* Tjenesteleverandør har
  * Økonomiske og politiske interesser
  * (se: Cambridge Analytica)


# Forgiftede data og manipulering

* Inneholder treningsdata _gift_?
* Skjevt innhold?

# Fordeler og ulemper

Fordeler

- Transparens og revidering
- Vitenskapelig reproduksjon
- Lokal kontroll
- Finjustering og overføringstrening

Ulemper

- Personvern- og opphavsrettkonflikter
- Misbruk av kraftige åpne modeller
