# Geospatial Modeling with Python

**Sergio Souza Costa** — LambdaGEO, UFMA

A practical guide to geographic data science and discrete spatial simulation
using the Python ecosystem and the [DisSModel](https://github.com/lambdageo/dissmodel) framework.

## Build the book

```bash
pip install -r requirements.txt
mkdocs serve        # preview at http://127.0.0.1:8000
mkdocs build        # build static site to site/
mkdocs gh-deploy    # deploy to GitHub Pages
```

## Structure

```
docs/
  index.md
  part1/   ch01 … ch05   # Python for Data Science
  part2/   ch06 … ch10   # Geographic Data Science
  part3/   ch11 … ch20   # Discrete Spatial Modeling
```

## Contributing

Each chapter lives on its own branch: `chapter/chNN-slug`.
Open a PR to `main` when a chapter is ready for review.

---
*LambdaGEO Research Group · Federal University of Maranhão (UFMA)*
