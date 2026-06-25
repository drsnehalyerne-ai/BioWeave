# BioWeave v2

### Progression-Aware Transcriptomics Pipeline for Oral Carcinogenesis

**BioWeave** is an open-source computational transcriptomics framework developed to model disease progression from public gene-expression datasets. **BioWeave v2** introduces a structured, stage-wise oral carcinogenesis analysis workflow built around the NCBI GEO dataset **GSE30784**. The pipeline enables automated, metadata-driven sample grouping, differential expression analysis across critical histopathological transitions, and bridge-gene discovery across premalignant and malignant stages.

This release upgrades BioWeave from an exploratory transcriptomics scaffold into a reusable **progression-aware analysis pipeline**, treating oral cancer development as a molecular continuum rather than a binary case-control state: **Control Epithelium → Oral Epithelial Dysplasia → Oral Squamous Cell Carcinoma (OSCC)**.

---

## Overview

Oral carcinogenesis is a multi-step biological process involving progressive transcriptomic rewiring. Standard public transcriptomic analyses frequently collapse this trajectory into a single binary "Normal vs. Tumor" comparison. This approach can obscure critical genes involved in **early premalignant transition**, **late malignant transformation**, and the **shared progression programs** that bridge these states.

**BioWeave v2** addresses this limitation by implementing a sequential, stage-wise workflow on **GSE30784** across three distinct analytical layers:

1. **Control vs. Dysplasia** differential expression (capturing early transition drivers)
2. **Dysplasia vs. Cancer** differential expression (capturing malignant transformation events)
3. **Bridge-Gene Discovery** (identifying overlapping markers active across both sequential transitions)

---

## Current BioWeave v2 Workflow

### Execution Steps
1. **Parse GEO Series Matrix**: Extracts the expression intensity data from `GSE30784_series_matrix.txt.gz`.
2. **Parse GPL Platform Metadata**: Extracts and indexes probe annotations from `GPL570.annot.gz`.
3. **Cohort Reconstruction**: Dynamically assigns samples to **Control**, **Dysplasia**, or **Cancer** cohorts using metadata string matching.
4. **Stage-Wise Differential Expression**: Executes independent statistical testing for `Control vs. Dysplasia` and `Dysplasia vs. Cancer`.
5. **Bridge-Gene Intersection**: Intersects the two discrete annotated DEG lists to isolate cross-stage progression markers.

---

## Current GSE30784 Results

* **Control:** 45 samples
* **Dysplasia:** 17 samples
* **Cancer (OSCC):** 167 samples

### Differential Expression Outputs
* **Control vs. Dysplasia**: 1,818 significant probe-level DEGs (1,731 annotated genes)
* **Dysplasia vs. Cancer**: 1,196 significant probe-level DEGs (1,133 annotated genes)
* **Bridge Genes**: **247 distinct bridge genes** shared across both transitions.

---

## Repository Structure

```text
BioWeave/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── gse30784_pipeline.py
│
├── data/
│   ├── GSE30784_series_matrix.txt.gz
│   └── GPL570.annot.gz
│
└── results/
    ├── control_vs_dysplasia_deg.csv
    ├── dysplasia_vs_cancer_deg.csv
    ├── bridge_genes.csv
    └── run_summary.txt
---

## Citation

If you use BioWeave v2 or adapt its stage-wise framework for your research, please cite this repository:

* **Direct Link:** [https://github.com/drsnehalyerne-ai/BioWeave](https://github.com/drsnehalyerne-ai/BioWeave)

```text
Yerne, S. (2026). BioWeave v2: A Progression-Aware Transcriptomics Pipeline for Oral Carcinogenesis. GitHub Repository: [https://github.com/drsnehalyerne-ai/BioWeave](https://github.com/drsnehalyerne-ai/BioWeave)
