# BioWeave

BioWeave is an open-source systems biology framework designed to identify molecular interaction networks, bridge genes, and biological modules associated with disease progression using transcriptomic datasets.

## Current Focus

### Oral Dysplasia and Early Oral Malignant Transformation

Dataset:

* GSE30784

Comparison:

* Normal oral mucosa vs Oral Dysplasia

## Current Findings

### Major Biological Themes

* Cell adhesion remodeling
* Extracellular matrix reorganization
* Host defense activation
* Bacteria-responsive signaling

### Candidate Bridge Genes

* FN1
* TGFB1
* STAT1
* CD44
* CCL2

### Proposed Model

Host defense activation

↓

STAT1 signaling

↓

CCL2-mediated immune communication

↓

TGFB1 activation

↓

FN1-driven extracellular matrix remodeling

↓

CD44-associated epithelial reorganization

↓

Oral dysplasia

## Software Architecture

```text
src/
├── utils.py
├── gse30784_pipeline.py
├── differential_expression.py
├── annotation.py
└── enrichment.py
```

## Roadmap

### Version 0.1

* GEO dataset loading
* Differential expression analysis
* Probe annotation
* Gene list generation

### Version 0.2

* STRING integration
* Network module identification
* Hub gene detection

### Version 0.3

* Multi-dataset validation
* Automated visualization
* Mechanistic figure generation

### Long-Term Vision

BioWeave aims to evolve into a reusable disease intelligence platform capable of integrating transcriptomics, protein interaction networks, pathway analysis, and explainable systems biology for hypothesis generation and biomarker discovery.
