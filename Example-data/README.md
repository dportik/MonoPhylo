# MonoPhylo

---------------

## Overview

**MonoPhylo** is a python script that can be used to assess the status of various user-defined relationships in phylogenetic trees. **MonoPhylo** can be used to accomplish the following tasks:

+ Output a complete list of all the tips in the tree. If the tips follow the naming scheme of `Genus_species` or `Genus_species_subspecies`, it can also output a complete list of genera. This file can be used to construct the groupings to test.

+ Root the tree using the MRCA of up to five taxa for the analysis, and optionally write the rooted tree to an output file.

+ Check the status (monophyletic, paraphyletic, polyphyletic) of all groupings defined by the user (genus, family, higher level taxonomy, etc.), and if the tree has support values it can obtain the support levels for each grouping.

**MonoPhylo** was written as a companion to the program **SuperCRUNCH**, and is described in the following pre-print article:

+ Portik, D.M., and J.J. Wiens. (2019) SuperCRUNCH: A toolkit for creating and manipulating supermatrices and other large phylogenetic datasets. BioRxiv, https://doi.org/10.1101/538728.


## Version

The current release of **MonoPhylo** is v1.0.

## Installation

**MonoPhylo** is a module written in Python (2.7) that functions as a stand-alone command-line script (`MonoPhylo.py`). It can be downloaded and executed independently without the need to install **MonoPhylo** as a Python package or library, making it easy to use and edit. There is one Python package that must be installed prior to use of **MonoPhylo**:

+ [ETE3](http://etetoolkit.org/): Installation instructions [here](http://etetoolkit.org/download/).

## Instructions for Analyses






## Citation

**MonoPhylo** is currently described in a pre-print available on BioRxiv:

+ Portik, D.M., and J.J. Wiens. (2019) SuperCRUNCH: A toolkit for creating and manipulating supermatrices and other large phylogenetic datasets. BioRxiv, https://doi.org/10.1101/538728.

If you use **MonoPhylo** for your research, please cite the above BioRxiv publication (for now).

## License

GNU Lesser General Public License v3.0

## Contact

MonoPhylo is written and maintained by Daniel Portik (daniel.portik@gmail.com)

