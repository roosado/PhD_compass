# Sources

Where to search during a scan or target research. Pick the rows for the owner's regions and field. In folder mode, add good sources you discover to the save file's Scan log so later scans reuse them.

## Position and programme boards
| Source | URL | Coverage |
|---|---|---|
| EURAXESS | https://euraxess.ec.europa.eu/jobs/search | Europe-wide; MSCA Doctoral Network posts are listed here |
| AcademicPositions | https://academicpositions.com | Europe-wide (blocks direct fetching: use a site-restricted web search) |
| FindAPhD | https://www.findaphd.com | UK-heavy, plus Europe, North America, Australia (may block fetching: use site search) |
| jobs.ac.uk | https://www.jobs.ac.uk | UK and Ireland |
| Nature Careers | https://www.nature.com/naturecareers | International, science |
| Science Careers | https://jobs.sciencecareers.org | International, science |
| jobRxiv | https://jobrxiv.org | Science jobs, including PhD posts |
| Times Higher Education Unijobs | https://www.timeshighereducation.com/unijobs | International, all fields |
| AcademicTransfer | https://www.academictransfer.com | Netherlands |
| Jobbnorge | https://www.jobbnorge.no | Norway (and some Nordic institutions) |
| ADUM | https://adum.fr | France, doctoral offers |
| ABG | https://www.abg.asso.fr | France, doctoral offers |
| CNRS jobs | https://emploi.cnrs.fr | France, doctoral contracts at CNRS labs |
| theses.fr | https://theses.fr | France, theses in progress: shows which groups run doctoral projects |
| Max Planck IMPRS | https://www.mpg.de/imprs | Germany, graduate schools with yearly calls |
| Helmholtz careers | https://www.helmholtz.de/en/career/ | Germany, research centres |
| DAAD scholarship database | https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/ | Funding for study and research in Germany, filterable by nationality |
| Universitaly | https://www.universitaly.it | Italy, national portal |
| HigherEdJobs | https://www.higheredjobs.com | United States (mostly staff and faculty; few PhD posts) |
| University and institute vacancy pages | — | Often the most complete and current; many Nordic universities post only there |
| Group websites | — | Members, recent hires, "open positions" notes |

Programme-based systems (US, Canada, many graduate schools) are found through department and graduate-school pages rather than boards: search for the field's departments in the chosen countries and read each programme's admissions and funding pages.

## Funded projects (a grant means positions)
| Source | URL | Use |
|---|---|---|
| CORDIS | https://cordis.europa.eu | EU projects (ERC, MSCA, EIC): holders, partners, dates |
| ERC dashboard | https://erc.europa.eu/projects-statistics/erc-dashboard | ERC grants by panel, host and year |
| UKRI Gateway to Research | https://gtr.ukri.org | UK research council grants and studentship programmes |
| NSF Award Search | https://www.nsf.gov/awardsearch/ | US National Science Foundation grants |
| NIH RePORTER | https://reporter.nih.gov | US National Institutes of Health grants |
| NSERC awards database | https://www.nserc-crsng.gc.ca/ase-oro/index_eng.asp | Canada, natural sciences and engineering |
| ARC grants data portal | https://dataportal.arc.gov.au/NCGP/Web/Grant/Grants | Australian Research Council grants |
| DFG GEPRIS | https://gepris.dfg.de | German Research Foundation projects |
| SNSF data portal | https://data.snf.ch/grants | Swiss National Science Foundation grants |
| ANR | https://anr.fr/en/ | French National Research Agency |
| NWO projects | https://www.nwo.nl/en/projects | Dutch Research Council |
| FWF | https://www.fwf.ac.at/en | Austrian Science Fund |
| FWO | https://www.fwo.be/en/ | Research Foundation – Flanders |
| Research Council of Finland | https://www.aka.fi/en/ | Finland |
| Swedish Research Council | https://www.vr.se/english.html | Sweden |
| Research Council of Norway | https://www.forskningsradet.no/en/ | Norway |
| Independent Research Fund Denmark | https://dff.dk/en | Denmark |
| FCT | https://www.fct.pt | Portugal |
| KAKEN | https://kaken.nii.ac.jp/en/ | Japan, JSPS grants |

## People and papers
| Source | URL | Use |
|---|---|---|
| Google Scholar | https://scholar.google.com | Recent papers, author profiles |
| OpenAlex API | https://api.openalex.org | Structured search of works, authors and institutions, e.g. `/works?search=<terms>&filter=from_publication_date:<YYYY-MM-DD>`; check current usage limits |
| Semantic Scholar | https://www.semanticscholar.org | Papers and authors |
| ORCID | https://orcid.org | Career history, grants |
| arXiv | https://arxiv.org | Physics, mathematics, computer science, quantitative biology, statistics, EE, economics preprints (API: https://export.arxiv.org/api/query) |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | Life sciences and medicine |
| bioRxiv | https://www.biorxiv.org | Biology preprints |
| ChemRxiv | https://chemrxiv.org | Chemistry preprints |
| EarthArXiv | https://eartharxiv.org | Earth sciences preprints |
| SSRN | https://www.ssrn.com | Social sciences, law, economics |
| RePEc IDEAS | https://ideas.repec.org | Economics |
| SocArXiv | https://osf.io/preprints/socarxiv | Social sciences |
| PhilPapers | https://philpapers.org | Philosophy |

## Finding groups through events
Speaker and author lists of the field's main conferences, summer schools and workshops show active groups. Find the two or three flagship meetings of each area and read the programmes of the last two editions.

## Fetch notes
- Some boards block direct fetching (HTTP 403): search them with a site-restricted web search (`site:academicpositions.com <keywords>`) and open individual ads.
- EURAXESS keyword search (checked 2026-09-21): use `https://euraxess.ec.europa.eu/jobs/search?f%5B0%5D=keywords%3A<term>`; a plain `?keywords=` parameter is ignored and returns the newest jobs. Matching is loose full-text, newest first, so read the first page or two.
- AcademicTransfer search (checked 2026-09-21): `https://www.academictransfer.com/en/jobs/?q=<term>` fetches directly.
- CORDIS bulk data (checked 2026-09-21): [the Horizon Europe projects CSV](https://cordis.europa.eu/data/cordis-HORIZONprojects-csv.zip) lists every project and participant; filtering it locally by keyword is much faster than searching project by project.
- Parallel search agents share one web-search budget for the session: brief each to prefer fetching known pages over new searches, and split a scan across three or four agents at most.
- Vacancy PDFs: fetch and read the file.
- Very long PDFs may exceed fetch limits: use the abstract page or an HTML version.
- Community sites (forums, admissions-results boards) can hint at timelines, but never count as a source for a fact in the save file.
