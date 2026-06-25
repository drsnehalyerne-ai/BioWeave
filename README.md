# BioWeave v2.0

### Progression-aware transcriptomics pipeline for oral carcinogenesis

**BioWeave** is a computational transcriptomics framework for studying disease progression from public gene-expression datasets. **BioWeave v2.0** introduces a stage-wise oral carcinogenesis analysis workflow built around **GSE30784**, enabling metadata-driven sample grouping, differential expression analysis across key disease transitions, and bridge-gene discovery across premalignant and malignant stages.

This release upgrades BioWeave from an exploratory transcriptomics scaffold into a **progression-aware analysis pipeline** for modeling oral cancer development as a molecular continuum from **control epithelium → dysplasia → carcinoma**.

---

## Overview

Oral carcinogenesis is not a single binary event but a staged biological process involving progressive transcriptomic rewiring from normal mucosa to dysplastic lesions and eventually invasive carcinoma. Most public transcriptomic analyses collapse this trajectory into a single case–control comparison, which can obscure genes involved in **early premalignant transition**, **late malignant transformation**, and **shared progression programs**.

**BioWeave v2.0** addresses this by implementing a stage-wise workflow on the GEO dataset **GSE30784**, with three core analytical layers:

1. **Control vs Dysplasia** differential expression
2. **Dysplasia vs Cancer** differential expression
3. **Bridge-gene discovery** across both transitions

This structure allows BioWeave to capture both **stage-specific molecular changes** and **shared progression-associated genes** that persist across oral carcinogenesis.

---

## What’s New in BioWeave v2.0

BioWeave v2.0 is a major upgrade from the original BioWeave framework. Key additions in this release include:

* **Metadata-driven sample grouping from GEO**

  * reconstruction of **control**, **dysplasia**, and **cancer** cohorts directly from GEO series-matrix metadata rather than hard-coded sample ordering

* **Two-stage differential expression workflow**

  * **Control → Dysplasia**
  * **Dysplasia → Cancer**

* **Bridge-gene identification**

  * overlap-based discovery of genes shared across both disease transitions

* **Structured output export**

  * comparison-specific DEG tables
  * bridge-gene list
  * run summary file for reproducibility

* **A clearer progression-analysis architecture**

  * BioWeave now operates as a reusable stage-wise transcriptomics workflow rather than a single exploratory script

---

## Current BioWeave v2.0 Workflow

The current release is built around **GSE30784**, a public oral carcinogenesis transcriptomic dataset containing control, dysplasia, and oral squamous cell carcinoma samples.

### Workflow steps

1. **Load GEO series matrix**

   * parse expression matrix from `GSE30784_series_matrix.txt.gz`

2. **Load GPL annotation**

   * parse Affymetrix platform annotation from `GPL570.annot.gz`

3. **Reconstruct sample groups from GEO metadata**

   * identify and assign samples to:

     * **Control**
     * **Dysplasia**
     * **Cancer**

4. **Prepare expression matrix**

   * convert expression values to numeric form
   * index matrix by probe ID

5. **Run stage-wise differential expression**

   * **Control vs Dysplasia**
   * **Dysplasia vs Cancer**

6. **Filter significant DEGs**

   * adjusted p-value threshold
   * log fold-change threshold

7. **Annotate DEG tables**

   * map probes to platform annotation

8. **Identify bridge genes**

   * compute overlap of annotated genes between:

     * Control vs Dysplasia DEGs
     * Dysplasia vs Cancer DEGs

9. **Export results**

   * DEG tables for each transition
   * bridge-gene list
   * run summary file

---

## Current GSE30784 Results

Using the current BioWeave v2.0 pipeline on **GSE30784**, the following outputs were obtained:

### Sample groups

* **Control:** 45 samples
* **Dysplasia:** 17 samples
* **Cancer:** 167 samples

### Differential expression results

* **Control vs Dysplasia**

  * **1818 significant DEGs**
  * **1731 annotated DEGs**

* **Dysplasia vs Cancer**

  * **1196 significant DEGs**
  * **1133 annotated DEGs**

### Bridge genes

* **247 bridge genes** shared across both transitions

These bridge genes represent candidate molecular programs that persist from the premalignant state into overt malignancy and may be relevant for progression biology, biomarker discovery, and systems-level network analysis.

---

## Repository Structure

A typical BioWeave v2 repository structure should look like this:

```text
BioWeave/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── sample_metadata.py
│   ├── differential_expression.py
│   ├── annotation.py
│   ├── bridge_genes.py
│   ├── enrichment.py
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
```

> Depending on your repository preference, `results/` can either be tracked as example outputs or excluded through `.gitignore`.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BioWeave.git
cd BioWeave
```

Install required Python packages:

```bash
pip install pandas scipy statsmodels
```

If you plan to extend the enrichment or network modules, additional packages may be needed later.

---

## Required Input Files

BioWeave v2.0 currently expects the following input files:

* **GEO series matrix**

  * `GSE30784_series_matrix.txt.gz`

* **GPL annotation file**

  * `GPL570.annot.gz`

These should be placed in the expected data directory used by the pipeline, for example:

```python
DATA_DIR = "/content/drive/MyDrive/BioWeave/data"
```

or modified to match your local environment.

---

## How to Run

The main stage-wise oral carcinogenesis workflow is executed through:

```python
import runpy
_ = runpy.run_path("src/gse30784_pipeline.py", run_name="__main__")
```

If running directly from the command line:

```bash
python src/gse30784_pipeline.py
```

---

## Output Files

BioWeave v2.0 currently generates the following outputs:

### 1. `control_vs_dysplasia_deg.csv`

Significant differentially expressed genes/probes for the **Control vs Dysplasia** comparison after annotation and filtering.

### 2. `dysplasia_vs_cancer_deg.csv`

Significant differentially expressed genes/probes for the **Dysplasia vs Cancer** comparison after annotation and filtering.

### 3. `bridge_genes.csv`

List of genes shared across both transitions, representing progression-associated bridge genes.

### 4. `run_summary.txt`

A summary of:

* sample counts
* DEG counts
* bridge-gene count
* filtering thresholds used during the run

---

## Biological Rationale

The central biological idea behind BioWeave v2.0 is that oral cancer should be modeled as a **progressive molecular trajectory**, not simply as a terminal tumor phenotype.

### Why use stage-wise comparisons?

A single tumor-vs-control comparison mixes together:

* early field changes
* dysplastic transformation
* malignant invasion-associated programs

By separating the trajectory into:

* **Control → Dysplasia**
* **Dysplasia → Cancer**

BioWeave allows the user to distinguish:

### Early transition genes

Genes altered during the shift from histologically normal mucosa to premalignant dysplasia.

### Late transition genes

Genes associated with malignant conversion from dysplasia to carcinoma.

### Bridge genes

Genes shared across both transitions that may represent persistent progression programs and candidate molecular drivers of oral carcinogenesis.

This structure makes BioWeave particularly useful for:

* progression biology
* biomarker prioritization
* bridge-gene network analysis
* systems-biology interpretation of oral premalignancy and OSCC evolution

---

## Current Limitations

BioWeave v2.0 is a substantial upgrade, but it is still an **early research-code release** rather than a fully mature software package. Current limitations include:

* DEG outputs are still largely **probe-level / annotation-attached**, not fully collapsed to a clean gene-level representation
* enrichment workflows are not yet fully integrated into the main progression pipeline
* current release is focused on **GSE30784** rather than a multi-dataset meta-framework
* downstream network, hub-gene, and pathway prioritization layers are still under active development

These limitations are part of the planned roadmap for future versions.

---

## Roadmap

### Planned upgrades for BioWeave v2.x / v3

* **Gene-level collapsing of probe-level DEG outputs**
* **GO / KEGG enrichment integration**
* **Bridge-gene network analysis**
* **Hub-gene prioritization**
* **Support for additional oral carcinogenesis and progression datasets**
* **Cleaner modular CLI / configuration structure**
* **Extension toward broader disease-progression transcriptomics workflows**

---

## Suggested Versioning Interpretation

### BioWeave v1

Initial public framework / early transcriptomic scaffold

### BioWeave v2

First progression-aware oral carcinogenesis analysis engine:

* metadata-driven grouping
* stage-wise DEG analysis
* bridge-gene discovery
* structured reproducible outputs

---

## Citation

If you use BioWeave in academic work, please cite the repository release and acknowledge the original GEO dataset used in the workflow.

**Current BioWeave release:**
**BioWeave v2.0** — progression-aware transcriptomics pipeline for oral carcinogenesis

You may later replace this section with a formal citation once the repository is archived on Zenodo or linked to a manuscript.

---

## Author

**Dr. Snehal Yerne**
Department of Oral and Maxillofacial Pathology
Swargiya Dadasaheb Kalmegh Smruti Dental College and Hospital
Nagpur, Maharashtra, India

---

## Contact / Collaboration

BioWeave is being developed as an evolving computational framework for oral disease progression, transcriptomics, and systems-level biomarker discovery.

If you work in:

* oral cancer biology
* oral epithelial dysplasia
* transcriptomics
* systems biology
* computational pathology
* progression modeling

and would like to discuss collaborations, benchmarking, or future extensions of BioWeave, feel free to connect through GitHub or academic correspondence.

---

## BioWeave v2.0 in One Line

**BioWeave v2.0 transforms oral carcinogenesis transcriptomics from a single case–control analysis into a progression-aware workflow spanning control epithelium, dysplasia, and carcinoma, with bridge-gene discovery across disease transitions.**
