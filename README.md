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

## Check the chapters

The notebooks are stored with their outputs and the site does not execute
them. To run every chapter against the pinned packages (Python 3.11+) and list
the cells that fail:

```bash
python scripts/run_notebooks.py               # all parts
python scripts/run_notebooks.py part4 part6   # some parts
```

Errors caused by a missing network connection are reported apart from errors
in the code.

## Structure

```
docs/
  index.md
  # Volume I — Foundations
  part1/   ch01 … ch05   # Scientific Python for Researchers
  part2/   ch06 … ch16   # Geographic Data Science
  part3/   ch17 … ch20   # Foundations of Spatial Simulation
  # Volume II — The DisSModel Ecosystem
  part4/   ch21 … ch25   # DisSModel: Core and Paradigms
  part5/   ch26 … ch27   # Domain Modeling: Land Use & Coastal Systems
  part6/   ch28 … ch31   # Data, Reproducibility & Verification
  part7/   ch32 … ch35   # Scaling, Migration & Reference (ch33 optional)
```

## PDF version

```bash
mkdocs serve
# open http://127.0.0.1:8000/print_page/ in Chrome/Edge
# Ctrl+P → "Save as PDF" → enable "Background graphics"
```

## Citation and license

Cite this book using [`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository" button)
or the DOI on Zenodo once the first release is out. Text, figures and code are released under
[CC BY 4.0](LICENSE).

## Contributing

Each chapter lives on its own branch: `chapter/chNN-slug`.
Open a PR to `main` when a chapter is ready for review.

---
*LambdaGEO Research Group · Federal University of Maranhão (UFMA)*
