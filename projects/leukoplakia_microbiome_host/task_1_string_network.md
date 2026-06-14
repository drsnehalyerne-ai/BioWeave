# Task 1: STRING Network Construction

## Objective

Construct a protein–protein interaction network from the 1297 dysplasia-associated genes identified from GSE30784.

## Input

BioWeave_Dysplasia_Genes.csv

## Analysis Plan

1. Upload genes to STRING.
2. Use Homo sapiens.
3. Minimum interaction score = 0.700.
4. Remove disconnected nodes.
5. Export network statistics.
6. Identify hub genes.
7. Identify modules related to:

   * Bacterial response
   * Cell adhesion
   * ECM remodeling

## Expected Output

* STRING network
* Hub genes
* Network modules
* Candidate bridge genes linking bacterial response and epithelial remodeling
