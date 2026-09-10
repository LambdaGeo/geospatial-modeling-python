# Geospatial Modeling with Python

**Sergio Souza Costa** — LambdaGEO, UFMA

---

This book is a practical guide to geographic data science and discrete spatial
simulation using the Python ecosystem — from Python fundamentals through the
full [DisSModel](https://github.com/DisSModel/dissmodel) framework, including
installation, architecture, and a TerraME/LUCCME migration guide. (The
`dissmodel` package's own API reference lives with the code, at
[dissmodel.github.io/dissmodel](https://dissmodel.github.io/dissmodel/); this
book is the narrative path to it, not a substitute.)

It is organized in seven parts:

- **Part I** — Scientific Python for Researchers
  Core tools and practices: Python fundamentals, Pandas, data cleaning, EDA,
  and software engineering for reproducible science.

- **Part II** — Geographic Data Science
  A dual-substrate approach covering both vector and raster data models,
  multidimensional arrays, spatial relationships, and raster-vector integration.

- **Part III** — Foundations of Spatial Simulation
  Cellular automata, discrete-event simulation with salabim, NumPy
  vectorization, and the performance problem that motivates DisSModel.

- **Part IV** — DisSModel: Core and Paradigms
  Installing and building models with DisSModel, then each simulation
  paradigm in turn — system dynamics, cellular automata, agent-based modeling.

- **Part V** — Domain Modeling: Land Use & Coastal Systems
  DisSLUCC's land-use change models and a full coastal dynamics case study.

- **Part VI** — Data & Infrastructure
  Reproducibility, the Brazilian Earth Observation ecosystem, the DisSModel
  Platform, and spatial data cubes.

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
models. Chapters 6–13 are fully independent of DisSModel.*

| Ch | Title | Substrate | Notebook |
|----|-------|-----------|----------|
| 6 | Introduction to Spatial Data | Both | `part2/ch06_spatial_intro.ipynb` |
| 7 | Vector Data with GeoPandas | Vector | `part2/ch07_vector.ipynb` |
| 8 | Raster Data with NumPy and rasterio | Raster | `part2/ch08_raster.ipynb` |
| 9 | Multidimensional Arrays with Xarray | Raster | `part2/ch09_xarray.ipynb` |
| 10 | Spatial Relationships and Weights | Both | `part2/ch10_weights.ipynb` |
| 11 | Exploratory Spatial Data Analysis | Both | `part2/ch11_esda.ipynb` |
| 12 | Visualizing Spatial Data | Both | `part2/ch12_visualization.ipynb` |
| 13 | Raster-Vector Integration Patterns | Both | `part2/ch13_integration.ipynb` |

---

## Part III — Foundations of Spatial Simulation

*Simulation paradigms built by hand, before DisSModel is introduced. All four
chapters are readable without any DisSModel knowledge.*

| Ch | Title | Notebook |
|----|-------|----------|
| 14 | Paradigms of Spatial Simulation | `part3/ch14_paradigms.ipynb` |
| 15 | Cellular Automata from Scratch | `part3/ch15_ca.ipynb` |
| 16 | Discrete-Event Simulation with salabim | `part3/ch16_des.ipynb` |
| 17 | The Performance Problem — and the Solution | `part3/ch17_performance.ipynb` |

---

## Part IV — DisSModel: Core and Paradigms

*Where the framework itself takes over — installation, architecture, and each
simulation paradigm from Part III revisited with DisSModel doing the
bookkeeping.*

| Ch | Title | Notebook |
|----|-------|----------|
| 18 | Introducing DisSModel | `part4/ch18_dissmodel.ipynb` |
| 19 | Building Models with DisSModel | `part4/ch19_building.ipynb` |
| 20 | System Dynamics with DisSModel | `part4/ch20_sysdyn.ipynb` |
| 21 | Cellular Automata with DisSModel | `part4/ch21_ca_dissmodel.ipynb` |
| 22 | Agent-Based Modeling with DisSModel | `part4/ch22_abm.ipynb` |

---

## Part V — Domain Modeling: Land Use & Coastal Systems

| Ch | Title | Notebook |
|----|-------|----------|
| 23 | Land Use and Cover Change Modeling | `part5/ch23_lucc.ipynb` |
| 24 | Case Study — Coastal Dynamics | `part5/ch24_coastal.ipynb` |

---

## Part VI — Data & Infrastructure

| Ch | Title | Notebook |
|----|-------|----------|
| 25 | Reproducibility and Experiment Provenance | `part6/ch25_provenance.ipynb` |
| 26 | DisSModel and the Brazilian Earth Observation Ecosystem | `part6/ch26_ecosystem.ipynb` |
| 27 | Running Models with the DisSModel Platform | `part6/ch27_platform.ipynb` |
| 28 | Spatial Data Cubes | `part6/ch28_disscube.ipynb` |

---

## Part VII — Scaling, Migration & Reference

| Ch | Title | Notebook |
|----|-------|----------|
| 29 | Ensemble Scenarios and Sensitivity Analysis | `part7/ch29_ensemble.ipynb` |
| 30 | Migrating from TerraME/LUCCME to DisSModel | `part7/ch30_migration.ipynb` |
| 31 | Architecture and Contributing | `part7/ch31_architecture.ipynb` |

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
