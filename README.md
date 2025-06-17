# Xenopus laevis Population Genomics Scripts for "The allopolyploid genome of Xenopus laevis behaves like a functional diploid in extant populations" paper:

This repository contains two custom scripts used for analyzing genetic diversity and allele distribution in natural populations of Xenopus laevis. 

## Repository Contents

### 1. `Alleles.py` script:

This script calculates fixed and private allele frequency across different populations:

* Fixed alleles – alleles that are homozygous across all individuals in the population.
* Private alleles – alleles that are unique to a specific population.
* Shared alleles – alleles that are found in two or more populations.

#### Input:

* VCF file with genotype calls.
* Population assignment file (tab-delimited: sample ID and population name).

#### Output:

* Summary table with the percentages of fixed, private, and shared alleles per population.

---

### 2. `Exons_nucleotide_diversity` script:

This script estimates nucleotide diversity around protein-coding exons in non-admixed individuals from the south-western Cape population.

#### Methodology:

* The first and last exons for each protein-coding gene were extracted from the X. laevis GFF annotation file.
* For each exon, 10Kb of flanking sequence was extracted both upstream and downstream.
* Nucleotide diversity was calculated using this customized Perl script tailored to handle population-genomic data.

#### Categories analyzed:

* First exons: `n = 33,866`
* Last exons: `n = 33,866`
* Single-exon genes: `n = 7,729`

#### Requirements:

* GFF3 genome annotation file of Xenopus laevis.
* Combined and genotyped VCF files of your samples of interest.

---

## Usage

Clone the repository:

```bash
git clone https://github.com/dareen22/Xenopus-laevis-WGS.git
```

---

## Citation

If you use these scripts in your work, please cite our publication:

> "The allopolyploid genome of *Xenopus laevis* behaves like a functional diploid in extant populations" (2025, Submitted to BMC Genomics)

---

## Contact

For questions or collaborations, feel free to contact:
Dareen Almojil  – [dareenalmojil@gmail.com) or (da4251@nyu.edu)

