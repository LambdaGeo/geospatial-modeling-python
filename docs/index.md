# Geospatial Modeling with Python

**Sergio Souza Costa** — LambdaGEO, UFMA

---

This book is a practical guide to geographic data science and discrete spatial
simulation using the Python ecosystem.

!!! info "Relationship to the technical reference"
    This book is the **didactic textbook** — from scratch up to DisSModel. For
    installation details, the full API, architecture decisions, and a
    TerraME/LUCCME → DisSModel migration guide, see the companion
    [*DisSModel Book*](https://github.com/DisSModel/dissmodel-book).

It is organized in four parts:

- **Part I** — Scientific Python for Researchers  
  Core tools and practices: Python fundamentals, Pandas, data cleaning, EDA,
  and software engineering for reproducible science.

- **Part II** — Geographic Data Science  
  A dual-substrate approach covering both vector and raster data models,
  multidimensional arrays, spatial relationships, and raster-vector integration.

- **Part III** — Discrete Spatial Modeling  
  Cellular automata, discrete-event simulation with salabim, NumPy
  vectorization, and the [DisSModel](https://github.com/DisSModel/dissmodel)
  framework — including a full coastal dynamics case study.

- **Part IV** — DisSModel in Practice  
  The Brazilian Earth Observation ecosystem, the DisSModel Platform,
  and ensemble scenario analysis.

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
| 9 | Multidimensional Arrays with Xarray | Raster | `part2/ch09_xarray.ipynb` ⭐ |
| 10 | Spatial Relationships and Weights | Both | `part2/ch10_weights.ipynb` |
| 11 | Exploratory Spatial Data Analysis | Both | `part2/ch11_esda.ipynb` |
| 12 | Visualizing Spatial Data | Both | `part2/ch12_visualization.ipynb` |
| 13 | Raster-Vector Integration Patterns | Both | `part2/ch13_integration.ipynb` ⭐ |

⭐ New chapters added in this edition.

---

## Part III — Discrete Spatial Modeling

*Chapters 14–18 introduce simulation paradigms and build toward the DisSModel
framework. Chapters 14–16 can be read without prior DisSModel knowledge.*

| Ch | Title | DisSModel dependency | Notebook |
|----|-------|----------------------|----------|
| 14 | Paradigms of Spatial Simulation | None | `part3/ch14_paradigms.ipynb` |
| 15 | Cellular Automata from Scratch | None | `part3/ch15_ca.ipynb` |
| 16 | Discrete-Event Simulation with salabim | None | `part3/ch16_des.ipynb` |
| 17 | The Performance Problem — and the Solution | None | `part3/ch17_performance.ipynb` |
| 18 | Introducing DisSModel | API | `part3/ch18_dissmodel.ipynb` |
| 19 | Building Models with DisSModel | API | `part3/ch19_building.ipynb` |
| 20 | Land Use and Cover Change Modeling | API | `part3/ch20_lucc.ipynb` |
| 21 | Case Study — Coastal Dynamics | API | `part3/ch21_coastal.ipynb` |
| 22 | Reproducibility and Experiment Provenance | API | `part3/ch22_provenance.ipynb` |

---

## Part IV — DisSModel in Practice

| Ch | Title | Notebook |
|----|-------|----------|
| 23 | DisSModel and the Brazilian Earth Observation Ecosystem | `part4/ch23_ecosystem.ipynb` |
| 24 | Running Models with the DisSModel Platform | `part4/ch24_platform.ipynb` |
| 25 | Ensemble Scenarios and Sensitivity Analysis | `part4/ch25_ensemble.ipynb` |

---

## How to Use This Book

Each chapter is a Jupyter notebook. You can read it as a book or run it
interactively. Code cells are self-contained within each chapter.

Parts I and II require no knowledge of DisSModel and are suitable for readers
interested in geographic data science alone. Part III introduces simulation
concepts independently before coupling to the framework. Part IV assumes
familiarity with the full DisSModel API.

## Installation

```bash
pip install geopandas rasterio xarray zarr libpysal salabim
```

For chapters in Part III and IV that use DisSModel:

```bash
pip install dissmodel>=0.4.0
```

For the coastal dynamics case study (Chapter 21):

```bash
pip install coastal-dynamics
```

---

## Source Code

All notebooks and supporting code are available at:

- Book repository: [github.com/lambdageo/geospatial-modeling-python](https://github.com/lambdageo/geospatial-modeling-python)
- DisSModel framework: [github.com/DisSModel/dissmodel](https://github.com/DisSModel/dissmodel)
- Coastal dynamics models: [github.com/DisSModel/coastal-dynamics](https://github.com/DisSModel/coastal-dynamics)

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
