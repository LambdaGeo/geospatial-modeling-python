# Geospatial Modeling with Python

**Sergio Souza Costa** — LambdaGEO, UFMA

---

This book comes in two volumes, sharing one site and one numbering.

## Volume I — Foundations (Ch 1–20)

A self-contained geographic data science and scientific Python course —
**no DisSModel required**. Python fundamentals, Pandas, data cleaning,
vector and raster geospatial analysis, spatial statistics, and the
simulation paradigms (cellular automata, discrete-event simulation)
built by hand before any framework enters the picture. If your interest
is geospatial Python on its own, this volume is the whole book you need.

- **Part I** — Scientific Python for Researchers
  Core tools and practices: Python fundamentals, Pandas, data cleaning, EDA,
  and software engineering for reproducible science.

- **Part II** — Geographic Data Science
  A dual-substrate approach covering both vector and raster data models,
  multidimensional arrays, spatial relationships, and raster-vector integration.

- **Part III** — Foundations of Spatial Simulation
  Cellular automata, discrete-event simulation with salabim, NumPy
  vectorization, and the performance problem that motivates DisSModel.

## Volume II — The DisSModel Ecosystem (Ch 21–33)

Picks up exactly where Volume I leaves off and hands its concepts to
[DisSModel](https://github.com/DisSModel/dissmodel), the Python-native
spatial modeling framework this book's own research group develops —
installation, every simulation paradigm as a framework, domain case
studies, infrastructure, and a TerraME/LUCCME migration guide. (The
`dissmodel` package's own API reference lives with the code, at
[dissmodel.github.io/dissmodel](https://dissmodel.github.io/dissmodel/);
this volume is the narrative path to it, not a substitute.)

- **Part IV** — DisSModel: Core and Paradigms
  Installing and building models with DisSModel, then each simulation
  paradigm in turn — system dynamics, cellular automata, agent-based modeling.

- **Part V** — Domain Modeling: Land Use & Coastal Systems
  DisSLUCC's land-use change models and a full coastal dynamics case study.

- **Part VI** — Data & Infrastructure
  Reproducibility, the DisSModel Platform, and spatial data cubes.

- **Part VII** — Scaling, Migration & Reference
  Ensemble scenarios, migrating an existing TerraME/LUCCME model, and how to
  contribute to the ecosystem.

---

## Part I — Scientific Python for Researchers

*Chapters 1–5 are fully independent of DisSModel and can be read standalone.*

| Ch | Title | Notebook |
|----|-------|----------|
| 1 | The Scientific Python Ecosystem | `part1/ch01_ecosystem.ipynb` |
| 2 | The Geospatial Python Toolbox | `part1/ch02_toolbox.ipynb` |
| 3 | Tabular Data with Pandas | `part1/ch03_pandas.ipynb` |
| 4 | Data Cleaning and Exploratory Analysis | `part1/ch04_cleaning_eda.ipynb` |
| 5 | Software Engineering for Scientific Python | `part1/ch05_software_eng.ipynb` |

---

## Part II — Geographic Data Science

*A dual-substrate treatment of spatial data: vector and raster as complementary
models. Chapters 6–16 are fully independent of DisSModel.*

| Ch | Title | Substrate | Notebook |
|----|-------|-----------|----------|
| 6 | Introduction to Spatial Data | Both | `part2/ch06_spatial_intro.ipynb` |
| 7 | Vector Data with GeoPandas | Vector | `part2/ch07_vector.ipynb` |
| 8 | Raster Data with NumPy and rasterio | Raster | `part2/ch08_raster.ipynb` |
| 9 | Multidimensional Arrays with Xarray | Raster | `part2/ch09_xarray.ipynb` |
| 10 | Spatial Relationships and Weights | Both | `part2/ch10_weights.ipynb` |
| 11 | Point Pattern Analysis | Vector | `part2/ch11_pointpatterns.ipynb` |
| 12 | Exploratory Spatial Data Analysis | Both | `part2/ch12_esda.ipynb` |
| 13 | Spatial Regression | Vector | `part2/ch13_regression.ipynb` |
| 14 | Clustering and Regionalization | Vector | `part2/ch14_clustering.ipynb` |
| 15 | Visualizing Spatial Data | Both | `part2/ch15_visualization.ipynb` |
| 16 | Raster-Vector Integration Patterns | Both | `part2/ch16_integration.ipynb` |

---

## Part III — Foundations of Spatial Simulation

*Simulation paradigms built by hand, before DisSModel is introduced. All four
chapters are readable without any DisSModel knowledge.*

| Ch | Title | Notebook |
|----|-------|----------|
| 17 | Paradigms of Spatial Simulation | `part3/ch17_paradigms.ipynb` |
| 18 | Cellular Automata from Scratch | `part3/ch18_ca.ipynb` |
| 19 | Discrete-Event Simulation with salabim | `part3/ch19_des.ipynb` |
| 20 | The Performance Problem — and the Solution | `part3/ch20_performance.ipynb` |

---

## Part IV — DisSModel: Core and Paradigms

*Where the framework itself takes over — installation, architecture, and each
simulation paradigm from Part III revisited with DisSModel doing the
bookkeeping.*

| Ch | Title | Notebook |
|----|-------|----------|
| 21 | Introducing DisSModel | `part4/ch21_dissmodel.ipynb` |
| 22 | Building Models with DisSModel | `part4/ch22_building.ipynb` |
| 23 | System Dynamics with DisSModel | `part4/ch23_sysdyn.ipynb` |
| 24 | Cellular Automata with DisSModel | `part4/ch24_ca_dissmodel.ipynb` |
| 25 | Agent-Based Modeling with DisSModel | `part4/ch25_abm.ipynb` |

---

## Part V — Domain Modeling: Land Use & Coastal Systems

| Ch | Title | Notebook |
|----|-------|----------|
| 26 | Land Use and Cover Change Modeling | `part5/ch26_lucc.ipynb` |
| 27 | Case Study — Coastal Dynamics | `part5/ch27_coastal.ipynb` |

---

## Part VI — Data & Infrastructure

| Ch | Title | Notebook |
|----|-------|----------|
| 28 | Reproducibility and Experiment Provenance | `part6/ch28_provenance.ipynb` |
| 29 | Running Models with the DisSModel Platform | `part6/ch29_platform.ipynb` |
| 30 | Spatial Data Cubes | `part6/ch30_disscube.ipynb` |

---

## Part VII — Scaling, Migration & Reference

| Ch | Title | Notebook |
|----|-------|----------|
| 31 | Ensemble Scenarios and Sensitivity Analysis | `part7/ch31_ensemble.ipynb` |
| 32 | Migrating from TerraME/LUCCME to DisSModel | `part7/ch32_migration.ipynb` |
| 33 | Architecture and Contributing | `part7/ch33_architecture.ipynb` |

---

## How to Use This Book

Each chapter is a Jupyter notebook. You can read it as a book or run it
interactively. Code cells are self-contained within each chapter.

Parts I and II require no knowledge of DisSModel and are suitable for readers
interested in geographic data science alone. Part III introduces simulation
concepts independently before Part IV hands the same problems to the
framework. Parts V through VII assume familiarity with DisSModel's core API
from Part IV.

## Installation

```bash
pip install geopandas rasterio xarray zarr libpysal salabim
```

For Part IV onward, which use DisSModel directly:

```bash
pip install dissmodel
```

Extension packages (`dissmodel-ca`, `dissmodel-sysdyn`, `dissmodel-abm`,
`disslucc-continuous`, `disslucc-discrete`, `brmangue-dissmodel`) aren't on
PyPI yet — install each one straight from GitHub, e.g.:

```bash
pip install "git+https://github.com/DisSModel/dissmodel-ca.git"
```

---

## Source Code

All notebooks and supporting code are available at:

- Book repository: [github.com/lambdageo/geospatial-modeling-python](https://github.com/lambdageo/geospatial-modeling-python)
- DisSModel framework and API reference: [github.com/DisSModel/dissmodel](https://github.com/DisSModel/dissmodel)

---

## Citation

If you use this material in your research or teaching, please cite:

```
Costa, S. S. (2028). Geospatial Modeling with Python.
LambdaGEO Research Group, Federal University of Maranhão (UFMA).
https://lambdageo.github.io/geospatial-modeling-python
```

---

*LambdaGEO Research Group · Federal University of Maranhão (UFMA)*
[lambdageo.github.io](https://lambdageo.github.io)
