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

The goal of running **MonoPhylo** is to determine which groupings are monophyletic in a given phylogenetic tree. In order to achieve this, it is necessary to first obtain a list of the tips in the tree and subsequently define the groups. It is also important to ensure the phylogenetic tree is properly rooted for the analysis, otherwise the groupings may not be correctly assessed. Finally, using a file that defines the major groupings, the groups can be assessed for the given phylogenetic tree. Instructions for completing each of these major tasks can be found below. 

### Obtaining a list of tree tips:

To obtain an output file containing a list of tips sorted alphabetically, **MonoPhylo** can be used the following way:

```
python MonoPhylo.py -t <tree file> -o <output directory> --write_tips
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `--write_tips`

> Flag that specifies to write the tip labels to an output file. If used without the optional flag `--genus`, the output file will be called `Tip_List.txt`.

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --write_tips
```

The above command will search the tree file `RAxML_bestTree.Iguania.tre` to find all tip names present and write the output file called `Tip_List.txt` to the specified directory.


If the tip labels in the tree are formatted in a way that is consistent with binomial or trinomial taxon names (`Genus_species` and/or `Genus_species_subspecies`), then an additional feature can be used for this step. Rather than outputting a list of tip labels, the output will include tip labels and genus labels. Here is an example of how to use this feature:

```
python MonoPhylo.py -t <tree file> -o <output directory> --write_tips --genus
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `--write_tips`

> Flag that specifies to write the tip labels to an output file.

##### `--genus`

> Flag that specifies that the tip labels follow the format `Genus_species` and/or `Genus_species_subspecies`. When used, the output files will be called `Species_List.txt` and `Genus_List.txt`.

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --write_tips --genus
```

The above command will search the tree file `RAxML_bestTree.Iguania.tre` to find all tip names present, break the names into genus and species components and write the output files called `Species_List.txt` and `Genus_List.txt` to the specified directory.








Two complete tutorials are provided in the [Example-data folder](https://github.com/dportik/MonoPhylo/tree/master/Example-data).




## Citation

**MonoPhylo** is currently described in a pre-print available on BioRxiv:

+ Portik, D.M., and J.J. Wiens. (2019) SuperCRUNCH: A toolkit for creating and manipulating supermatrices and other large phylogenetic datasets. BioRxiv, https://doi.org/10.1101/538728.

If you use **MonoPhylo** for your research, please cite the above BioRxiv publication (for now).

## License

GNU Lesser General Public License v3.0

## Contact

MonoPhylo is written and maintained by Daniel Portik (daniel.portik@gmail.com)

