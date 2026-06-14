# Manuscript Concept v1

## Working Title

Bacteria-Responsive Host Remodeling Networks Associated with Early Oral Malignant Transformation: An Integrative Systems Biology Analysis

---

## Background

Oral leukoplakia and oral epithelial dysplasia represent key premalignant stages in the development of oral squamous cell carcinoma (OSCC). Although dysplasia is associated with an increased risk of malignant transformation, the molecular mechanisms linking host responses, epithelial barrier disruption, and tissue remodeling remain incompletely understood.

Recent evidence suggests that oral microbial dysbiosis may contribute to oral carcinogenesis through modulation of host signaling pathways. However, the systems-level interaction between bacteria-responsive host programs and tissue remodeling networks during early malignant transformation remains poorly characterized.

---

## Objective

To identify molecular networks associated with the transition from normal oral mucosa to oral dysplasia and investigate the relationship between bacteria-responsive host signaling, epithelial barrier disruption, and extracellular matrix remodeling.

---

## Dataset

### GEO Dataset

GSE30784

### Samples

* Normal oral mucosa: 45
* Oral dysplasia: 17
* Oral squamous cell carcinoma: 167

### Comparison Performed

Normal vs Dysplasia

---

## Workflow

GSE30784

↓

Differential Expression Analysis

↓

Probe Annotation (GPL570)

↓

GO Enrichment

↓

KEGG Enrichment

↓

STRING Network Analysis

↓

Hub Gene Identification

↓

Biological Network Interpretation

---

## Differential Expression Results

* Significant probes: 1818
* Unique genes: 1297

Notable dysregulated genes:

* CXCL14
* KRT17
* CLDN10
* TMPRSS2
* GCNT3
* SIM2

---

## GO Biological Process Enrichment

Major enriched biological processes:

* Tissue development
* Cell adhesion
* Extracellular matrix organization
* Response to bacterium
* Cell junction organization
* Intermediate filament cytoskeleton organization

---

## KEGG Pathway Enrichment

Major enriched pathways:

* Cornified envelope formation
* ECM–receptor interaction
* Integrin signaling
* Cadherin signaling
* Focal adhesion
* Cell adhesion molecule interaction

---

## STRING Network Analysis

### Network Statistics

* Nodes: 1191
* Edges: 2085
* Expected edges: 692
* Average node degree: 3.5
* Clustering coefficient: 0.357
* PPI enrichment p-value: <1×10⁻¹⁶

### Top Hub Genes

* FN1
* CD44
* COL1A1
* MMP9
* STAT1
* TGFB1
* COL1A2
* COL3A1
* COL4A1
* CCL2

---

## Proposed Biological Modules

### Module 1: Epithelial Barrier Remodeling

Representative genes:

* CLDN10
* CD44
* Cadherin-associated genes
* Junction-associated genes

### Module 2: Extracellular Matrix Remodeling

Representative genes:

* FN1
* COL1A1
* COL1A2
* COL3A1
* MMP2
* MMP9

### Module 3: Host Defense and Immune Activation

Representative genes:

* STAT1
* CCL2
* ISG15
* MX1
* DDX58
* OAS2

---

## Working Biological Model

Host defense activation

↓

STAT1 / CCL2 signaling

↓

TGFB1-mediated remodeling

↓

FN1-driven extracellular matrix reorganization

↓

Loss of epithelial integrity

↓

Development of oral dysplasia

---

## Novelty

Rather than focusing solely on individual hub genes, this study proposes that early oral malignant transformation is driven by coordinated interactions between:

1. Host defense activation
2. Epithelial barrier disruption
3. Extracellular matrix remodeling

This systems-level framework may provide new insights into the biological mechanisms underlying oral dysplasia progression.

---

## Next Analyses

1. Module-specific network analysis
2. Identification of bridge genes
3. Literature validation of hub genes
4. Mechanistic figure generation
5. Manuscript drafting
