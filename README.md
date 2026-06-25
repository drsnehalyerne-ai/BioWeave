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

This architecture allows researchers to systematically isolate stage-specific molecular shifts alongside persistent progression-associated genes.

---

## What’s New in BioWeave v2

BioWeave v2 represents a major structural upgrade from the original exploratory framework:

* **Automated Metadata-Driven Grouping**: Reconstructs clinical cohorts (**Control**, **Dysplasia**, and **Cancer**) dynamically from GEO series-matrix metadata parsing rather than relying on hard-coded sample indices.
* **Two-Stage Differential Expression Workflow**: Segregates upstream premalignant shifts (`Control → Dysplasia`) from downstream malignant conversion (`Dysplasia → Cancer`).
* **Bridge-Gene Identification Module**: Implements automated intersection logic to uncover overlapping transcriptomic shifts across both disease transitions.
* **Standardized File Export**: Systematizes outputs into comparison-specific Differential Expression Gene (DEG) tables, a standalone bridge-gene matrix, and a reproducible run summary log.
* **Modular Pipeline Architecture**: Transitioned the code base into an structured, executable script system designed for scalability.

---

## Current BioWeave v2 Workflow

The workflow executes sequentially through the following computational layers:
