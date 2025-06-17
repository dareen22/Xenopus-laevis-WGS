# Xenopus laevis Population Genomics Scripts 

Paper:  "The allopolyploid genome of Xenopus laevis behaves like a functional diploid in extant populations"

This repository contains two custom scripts used for analyzing genetic diversity and allele distribution in natural populations of Xenopus laevis. 

## Repository Contents

### 1. `Alleles.py` script:

This script calculates fixed and private allele frequency across different populations.


### 2. `Exons_nucleotide_diversity` script:

This script estimates nucleotide diversity around protein-coding exons.

#### Methodology:

* The first and last exons for each protein-coding gene were extracted from the X. laevis GFF annotation file.
* For each exon, 10Kb of flanking sequence was extracted both upstream and downstream.
* Nucleotide diversity was calculated using this customized Perl script tailored to handle population-genomic data.

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

