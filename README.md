[![DOI](https://zenodo.org/badge/428750304.svg)](https://zenodo.org/badge/latestdoi/428750304)

# **FASTA-FRAG**

### Script to fragment FASTA files into smaller sequence chunks

This script cuts a FASTA (also supports multiple sequences at once) into fragments of defined length. Depth of Coverage and displacement per coverage/tiling can be defined. First and last fragments can be shorter. Multiple fragment length can be chosen.

# Requirements
- python
- Biopython


# Usage example:
Basic usage:
``` 
python FASTA-FRAG.py -i in.fasta -s 50 -t 5 -d 10 -o out.fasta  
```

For help use:
``` 
python FASTA-FRAG.py -h  
```


# Cite:
Meriam Guellil. (2021). MeriamGuellil/FASTA-FRAG: (0.0.0). Zenodo. https://doi.org/10.5281/zenodo.5705869

# References:
Cock, Peter J. A., Tiago Antao, Jeffrey T. Chang, Brad A. Chapman, Cymon J. Cox, Andrew Dalke, Iddo Friedberg, et al. 2009. “Biopython: Freely Available Python Tools for Computational Molecular Biology and Bioinformatics.” Bioinformatics  25 (11): 1422–23. https://doi.org/10.1093/bioinformatics/btp163.
