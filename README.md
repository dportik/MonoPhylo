# MonoPhylo

---------------

## Overview

**MonoPhylo** is a python script that can be used to assess the status of various user-defined relationships in phylogenetic trees. **MonoPhylo** can be used to accomplish the following tasks:

+ Output a complete list of all the tips in the tree. If the tips follow the naming scheme of `Genus_species` or `Genus_species_subspecies`, it can also output a complete list of genera. This file can be used to construct the groupings to test.

+ Root the tree using the MRCA of up to five taxa for the analysis, and optionally write the rooted tree to an output file.

+ Check the status (monophyletic, paraphyletic, polyphyletic) of all groupings defined by the user (genus, family, higher level taxonomy, etc.), and if the tree has support values it can obtain the support levels for each grouping.

**MonoPhylo** was written as a companion to the program [SuperCRUNCH](https://github.com/dportik/SuperCRUNCH).

## Version

The current release of **MonoPhylo** is v1.0.

## Installation

**MonoPhylo** is a module written in Python (2.7) that functions as a stand-alone command-line script (`MonoPhylo.py`). It can be downloaded and executed independently without the need to install **MonoPhylo** as a Python package or library, making it easy to use and edit. There is one Python package that must be installed prior to use of **MonoPhylo**:

+ [ETE3](http://etetoolkit.org/): Installation instructions [here](http://etetoolkit.org/download/).

## Citation

**MonoPhylo** is currently described in a pre-print available on BioRxiv:

+ Portik, D.M., and J.J. Wiens. (2019) SuperCRUNCH: A toolkit for creating and manipulating supermatrices and other large phylogenetic datasets. BioRxiv, https://doi.org/10.1101/538728.

If you use **MonoPhylo** for your research, please cite the above BioRxiv publication (for now).

## License

GNU Lesser General Public License v3.0

## Contact

MonoPhylo is written and maintained by Daniel Portik (daniel.portik@gmail.com)

## Instructions for Analyses and Tutorials

The goal of running **MonoPhylo** is to determine which groupings are monophyletic in a given phylogenetic tree. In order to achieve this, it is necessary to first obtain a list of the tips in the tree and subsequently define the groups. It is also important to ensure the phylogenetic tree is properly rooted for the analysis, otherwise the groupings may not be correctly assessed. Finally, using a file that defines the major groupings, the groups can be assessed for the given phylogenetic tree. Instructions for completing each of these major tasks can be found below. 

In addition to the instructions posted here, two complete example analyses can be found in the [Example-data folder](https://github.com/dportik/MonoPhylo/tree/master/Example-data). The complete set of input files and output files generated for each step, along with instructions, can be found for each analysis folder present.


### 1. Obtaining a list of tree tips

#### Trees containing any type of tip label:

Phylogenetic trees can have many kinds of labels, including taxon names, accession numbers, or other unique identifiers. To obtain an output file containing a list of tips sorted alphabetically, **MonoPhylo** can be used the following way:

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

Here is an example of what the truncated contents of `Tip_List.txt` might look like:
```
Tip
Acanthocercus_adramitanus
Acanthocercus_atricollis
Acanthosaura_armata
Acanthosaura_capra
Agama_aculeata
Agama_africana
...
```

#### Trees containing tip labels representing taxon names:

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

Here is an example of what the truncated contents of `Species_List.txt` might look like:

```
Species	Genus
Acanthocercus_adramitanus	Acanthocercus
Acanthocercus_annectens	Acanthocercus
Acanthosaura_armata	Acanthosaura
Acanthosaura_capra	Acanthosaura
Agama_aculeata	Agama
Agama_africana	Agama
...
```

Notice that rather than containing a single column labeled *Tip*, there are now two columns labeled *Species* and *Genus* with the correct contents. The `Genus_List.txt` is similar to this file, but will only have a single column representing the unique genera entries:

```
Genus
Acanthocercus
Acanthosaura
Agama
...
```

### 2. Defining groups for the tip labels

Once an output file containing the tip labels is obtained, the next step is to use this file to construct a map file. The map file will define the groups to test. The map file should be in tab-delimited format. The first column will have a complete list of the tips in the tree (labeled Tips or Species depending on the option used to generate the tip labels file). Any additional column added allows for a grouping to be set. If the `--genus` flag was used, the second column will automatically contain the genera groupings. The column can be used to represent any type of taxon grouping (sub-family, family, super-family, order) or custom-defined group. Members of a particular group should be assigned the same group name for a given column, and any tip not assigned to a group for that column should be assigned a `NA` value.

Here is an example of the contents of a map file I generated:

```
Species	Genus	Family	SubFamily	MajorGroup
Acanthocercus_adramitanus	Acanthocercus	Agamidae	Agaminae	Acrodonta
Acanthocercus_annectens	Acanthocercus	Agamidae	Agaminae	Acrodonta
Acanthosaura_armata	Acanthosaura	Agamidae	Draconinae	Acrodonta
Acanthosaura_capra	Acanthosaura	Agamidae	Draconinae	Acrodonta
Agama_aculeata	Agama	Agamidae	Agaminae	Acrodonta
Agama_africana	Agama	Agamidae	Agaminae	Acrodonta
Amblyrhynchus_cristatus	Amblyrhynchus	Iguanidae	NA	Pleurodonta
Amphibolurus_muricatus	Amphibolurus	Agamidae	Amphibolurinae	Acrodonta
Amphibolurus_norrisi	Amphibolurus	Agamidae	Amphibolurinae	Acrodonta
Anisolepis_grilli	Anisolepis	Leiosauridae	Enyaliinae	Pleurodonta
Anisolepis_longicauda	Anisolepis	Leiosauridae	Enyaliinae	Pleurodonta
Anolis_acutus	Anolis	Dactyloidae	NA	Pleurodonta
Anolis_aeneus	Anolis	Dactyloidae	NA	Pleurodonta
...
```

In this example map file I labeled the columns according to a particular taxonomic level, and the groupings matched those levels. Note that there was no SubFamily assigned to the genus Anolis, and that the `NA` value was used instead. The `NA` value will exclude a tip from being assigned to any grouping for that category. This is useful for outgroups, which can be assigned `NA` across all columns and be excluded from analysis. 

The map file can contain more taxa than are actually present in the tree. Only taxon names that match those found in the tree will be included in the analysis. However, it is extremely important that all taxa present in the tree that belong to a particular group are included in the map file, otherwise the group cannot be found as monophyletic. This is why it makes the most sense to construct the map file from the tip labels output file created by **MonoPhylo**.

How you make the map file is ultimately up to you, but it might be helpful to use a spreadsheet editor (such as Excel) to add columns and values. Regardless of how the file is constructed, it must be tab-delimited. Sometimes using Excel or other applications to generate tab-delmited text file will include hidden characters, so make sure to open the file in a text editor and ensure the format includes Unix line breaks (line breaks marked by `\n`, rather than `\r\n`) and UTF-8 encoding. This will ensure that **MonoPhylo** can parse the file correctly.


### 3. Ensuring the tree is properly rooted

To correctly assess whether groupings are monophyletic, it is important to ensure that the phylogenetic tree is properly rooted. If the tree is unrooted, **MonoPhylo** can be used to correctly root the tree based on the MRCA of a set of taxa/tip labels (minimally two, but up to five taxa). The tip labels must be present in the tree, or an error will be thrown. The tree can be written to an output tree file and inspected to ensure the root placement is correct. The rooted tree file can be used for analysis. Here is an example of how to use **MonoPhylo** to root a tree:

```
python MonoPhylo.py -t <tree file> -o <output directory> --root --tip1 <tip/taxon label> --tip2 <tip/taxon label>
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `--root`

> Flag that specifies to root the phylogenetic tree using the MRCA of minimally two taxa (using the `--tip1` and `--tip2` flags).

##### `--tip1` <tip/taxon label>

> The name of the first tip/taxon label to use in rooting the tree.

##### `--tip2` <tip/taxon label>

> The name of the second tip/taxon label to use in rooting the tree.


#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --root --tip1 Acanthocercus_adramitanus --tip2 Agama_africana
```

The above command will root the tree file `RAxML_bestTree.Iguania.tre` using the MRCA of `Acanthocercus_adramitanus` and `Agama_africana`. Note that in this case, no output files will be created in the specified output directory.

#### Writing the rooted tree to an output tree file:

To write the rooted tree to an output file, an additional flag must be included (`--write_root`). For example:

```
python MonoPhylo.py -t <tree file> -o <output directory> --root --tip1 <tip/taxon label> --tip2 <tip/taxon label> --write_root
```

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --root --tip1 Acanthocercus_adramitanus --tip2 Agama_africana --write_root
```

The above command will root the tree file `RAxML_bestTree.Iguania.tre` using the MRCA of `Acanthocercus_adramitanus` and `Agama_africana`. Note that in this case, a rooted tree file called `Rooted_RAxML_bestTree.Iguania.tre` will be created in the specified output directory.

#### Including additional taxa in the set for rooting:

The rooting procedure will find the MRCA of a set of taxa and use it to root the phylogeny. This requires a minimum of two taxa, but up to five taxa can be included in the set used to identify the MRCA. To include more than two taxa, the optional `--tip3`, `--tip4`, and `--tip5` flags can be used:

```
python MonoPhylo.py -t <tree file> -o <output directory> --root --tip1 <tip/taxon label> --tip2 <tip/taxon label> --tip3 <tip/taxon label> --tip4 <tip/taxon label> --tip4 <tip/taxon label> --write_root
```

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --root --tip1 Acanthocercus_adramitanus --tip2 Agama_africana --tip3 Amblyrhynchus_cristatus --tip4 Tropidurus_semitaeniatus --write_root
```
The above command will root the tree file `RAxML_bestTree.Iguania.tre` using the MRCA of `Acanthocercus_adramitanus`, `Agama_africana`, `Amblyrhynchus_cristatus`, and `Tropidurus_semitaeniatus`. Note that in this case, a rooted tree file called `Rooted_RAxML_bestTree.Iguania.tre` will be created in the specified output directory.


### 4. Assessing the phylogenetic status of groups:






