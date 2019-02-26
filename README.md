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

In addition to the instructions posted here, two complete example analyses can be found in the [Example-data](https://github.com/dportik/MonoPhylo/tree/master/Example-data) folder. The complete set of input files and output files generated for each step, along with instructions, can be found for each analysis folder present.

Quick Navigation:

+ [Obtaining a list of tree tips](#OLTP)
+ [Defining groups for the tip labels](#DGTP)
+ [Ensuring the tree is properly rooted](#ETPR)
+ [Assessing the phylogenetic status of groups](#APSG)


### 1. Obtaining a list of tree tips <a name="OLTP"></a>

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

If the tip labels in the tree are formatted in a way that is consistent with binomial or trinomial taxon names (`Genus_species` and/or `Genus_species_subspecies`), then an additional flag (`--genus`) can be used for this step. Rather than outputting a list of tip labels, the output will include the genus and species labels. Here is an example of how to use this feature:

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

Notice that rather than containing a single column labeled *Tip*, there are now two columns labeled *Species* and *Genus* with the correct contents. The `Genus_List.txt` is similar to this file, but will only have a single column containing a list of all unique genera:

```
Genus
Acanthocercus
Acanthosaura
Agama
...
```

### 2. Defining groups for the tip labels <a name="DGTP"></a>

Once an output file containing the tip labels is obtained, the next step is to use this file to construct a map file. The map file will define the groups to test. The map file should be in tab-delimited format. The first column will have a complete list of the tips in the tree (labeled *Tips* or *Species* depending on the option used to generate the tip labels file). Any additional column added allows for a grouping to be set. If the `--genus` flag was used to generate the tip label file, the second column will automatically contain the genus groupings. The additional columns can be used to represent any type of taxon grouping (sub-family, family, super-family, order) or any custom-defined group. Members belonging to a particular group should be assigned the same group name for a given column, and all tips not assigned to any group for that column should be assigned a `NA` value.

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

In this example map file I labeled the columns according to a particular taxonomic level, and the groupings matched those levels. Note that there was no *SubFamily* value assigned to the genus `Anolis`, and the `NA` value was used instead. The `NA` value will exclude a tip from being assigned to any grouping for that category. This is useful for outgroups, which can be assigned `NA` across all columns and be excluded from analysis. In this sense, a group category (column) does not require information for each of the tips. 

The map file can contain more taxa than are actually present in the tree. Only taxon names that match those found in the tree will be included in the analysis. However, it is extremely important that all taxa present in the tree that belong to a particular group are included in the map file, otherwise the group can never be found as monophyletic (because some members are missing). This is why it makes the most sense to construct the map file from the tip labels output file created by **MonoPhylo**.

How you make the map file is ultimately up to you, but it might be helpful to use a spreadsheet editor (such as Excel) to add columns and values. Regardless of how the file is constructed, the final format must be tab-delimited. Sometimes using Excel or other applications to generate a tab-delmited text file will include hidden characters, so make sure to open the output file in a text editor and ensure UTF-8 encoding and Unix line breaks (line breaks marked by `\n`, rather than `\r\n`). This will allow **MonoPhylo** to parse the file correctly.


### 3. Ensuring the tree is properly rooted <a name="ETPR"></a>

To correctly assess whether groupings are monophyletic, it is important to ensure that the phylogenetic tree is properly rooted. If the tree is unrooted, **MonoPhylo** can be used to correctly root the tree based on the MRCA of a set of taxa/tip labels (minimally two, but up to five taxa). The tip labels must be present in the tree, or an error will be thrown. The tip labels output file can be used to identify the labels for this step. The tree can be written to an output tree file and inspected to ensure the root placement is correct. The rooted tree file can also be used for analysis. If the input tree file contains support values, these will be preserved in the rooted tree file. Here is an example of how to use **MonoPhylo** to root a tree:

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

##### `--write_root`

> Flag indicating the rooted tree should be written to an output file. The output tree file will be written to the specified output directory, and will have a name identical to the input tree file but with a prefix (`Rooted_`) added. For example `My-Tree.tre` would be rooted and written as `Rooted_My-Tree.tre`.

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --root --tip1 Acanthocercus_adramitanus --tip2 Agama_africana --write_root
```

The above command will root the tree file `RAxML_bestTree.Iguania.tre` using the MRCA of `Acanthocercus_adramitanus` and `Agama_africana`. Note that in this case, a rooted tree file called `Rooted_RAxML_bestTree.Iguania.tre` will be created in the specified output directory.

#### Including additional taxa in the set for rooting:

The rooting procedure will find the MRCA of a set of taxa and use it to root the phylogeny. This requires a minimum of two taxa, but up to five taxa can be included in the set used to identify the MRCA. To include more than two taxa, the optional `--tip3`, `--tip4`, and `--tip5` flags can be used:

```
python MonoPhylo.py -t <tree file> -o <output directory> --root --tip1 <tip/taxon label> --tip2 <tip/taxon label> --tip3 <tip/taxon label> --tip4 <tip/taxon label> --tip5 <tip/taxon label> --write_root
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `--root`

> Flag that specifies to root the phylogenetic tree using the MRCA of minimally two taxa (using the `--tip1` and `--tip2` flags).

##### `--tip1` <tip/taxon label>

> Required: The name of the first tip/taxon label to use in rooting the tree.

##### `--tip2` <tip/taxon label>

> Required: The name of the second tip/taxon label to use in rooting the tree.

##### `--tip3` <tip/taxon label>

> Optional: The name of the third tip/taxon label to use in rooting the tree.

##### `--tip4` <tip/taxon label>

> Optional: The name of the fourth tip/taxon label to use in rooting the tree.

##### `--tip5` <tip/taxon label>

> Optional: The name of the fifth tip/taxon label to use in rooting the tree.


#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ --root --tip1 Acanthocercus_adramitanus --tip2 Agama_africana --tip3 Amblyrhynchus_cristatus --tip4 Tropidurus_semitaeniatus --write_root
```
The above command will root the tree file `RAxML_bestTree.Iguania.tre` using the MRCA of four taxa: `Acanthocercus_adramitanus`, `Agama_africana`, `Amblyrhynchus_cristatus`, and `Tropidurus_semitaeniatus`. In this case, the `--write_root` flag specifies a rooted tree file called `Rooted_RAxML_bestTree.Iguania.tre` will be created in the specified output directory.


### 4. Assessing the phylogenetic status of groups <a name="APSG"></a>

Once a map file has been constructed and the tree is properly rooted, the defined groups can be assessed. There are two types of analyses, which only vary in whether the input tree contains support values or not. For each group category (e.g., a column in the map file), an output file will be created. In addition, the results across all group categories can be found in the output file labeled `All_Groups_results.txt`. The results files for each group category will contain the following columns of information:

+ **Grouping** - The name of the group, as indicated in the map file.
+ **Number_Contained_Taxa** - The number of taxa contained in the group. This number includes only the taxa that were found in the tree.
+ **Monophyletic** - A value of `True` or `False` will be assigned based on whether the grouping was found to be monophyletic. If the group contained only a single taxon, a value of `NA` is assigned instead.
+ **Category** - Possible values include `Monophyletic`, `Paraphyletic`, and `Polyphyletic`. If the group contained only a single taxon, a value of `NA` is assigned instead.
+ **Support** - If the tree contains support values for nodes and this option is invoked, the support value will be listed for groups found to be monophyletic. If the group is paraphyletic, polyphyletic, or contains only a single taxon, a value of `NA` is assigned instead.
+ **Number_Interfering_Species** - If the group is paraphyletic or polyphyletic, the **NUMBER** of additional taxa that must be included to make the group monophyletic is listed. This is the number of taxa that are 'interfering' with the monophyly of the group. If the group is monophyletic, this value will be 0. 
+ **Interfering_Species** - If the group is paraphyletic or polyphyletic, the **NAMES** of the additional taxa that must be included to make the group monophyletic are listed. These are the names of the taxa that are 'interfering' with the monophyly of the group. If the group is monophyletic, this column will be blank.

Instructions for running the analysis for both tree types are provided below.

#### Assessing groups in trees without support values:

To run the analysis for a tree without support values for nodes, the following command can be used:

```
python MonoPhylo.py -t <tree file> -o <output directory> -m <map file>
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `-m`

> The full path to a map file that contains the tip/taxon labels and their corresponding groupings.


#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/Rooted_RAxML_bestTree.Iguania.tre -o bin/Analysis/Output1/ -m bin/Analysis/Iguania_groupings.txt
```

The above command will assess all groupings defined in `Iguania_groupings.txt` in the tree file `Rooted_RAxML_bestTree.Iguania.tre`. All output files will be created in the specified output directory.

In this usage the output files will not contain any information about support values, because we did not include the `--support` flag. Here is an example of the truncated contents from one of the results files (in this case genera):

```
Grouping	Number_Contained_Taxa	Monophyletic	Category	Number_Interfering_Species	Interfering_Species
Acanthocercus	5	FALSE	Polyphyletic	10	Agama_robecchii, Pseudotrapelus_aqabensis, Pseudotrapelus_chlodnickii, Pseudotrapelus_dhofarensis, Pseudotrapelus_jensvindumi, Pseudotrapelus_neumanni, Pseudotrapelus_sinaitus, Xenagama_batillifera, Xenagama_taylori, Xenagama_wilmsi
Acanthosaura	4	TRUE	Monophyletic	0	
Agama	38	FALSE	Polyphyletic	14	Acanthocercus_adramitanus, Acanthocercus_annectens, Acanthocercus_atricollis, Acanthocercus_cyanogaster, Acanthocercus_yemensis, Pseudotrapelus_aqabensis, Pseudotrapelus_chlodnickii, Pseudotrapelus_dhofarensis, Pseudotrapelus_jensvindumi, Pseudotrapelus_neumanni, Pseudotrapelus_sinaitus, Xenagama_batillifera, Xenagama_taylori, Xenagama_wilmsi
Amblyrhynchus	1	NA	NA	0	
Amphibolurus	2	TRUE	Monophyletic	0	
Anisolepis	2	TRUE	Monophyletic	0	
Anolis	324	TRUE	Monophyletic	0	
Aphaniotis	1	NA	NA	0	
Archaius	1	NA	NA	0	
Basiliscus	4	TRUE	Monophyletic	0	
```

#### Assessing groups in trees containing support values:

To run the analysis for a tree containing support values for nodes, the following command can be used:

```
python MonoPhylo.py -t <tree file> -o <output directory> -m <map file> --support
```

#### Argument Explanations:

##### `-t <path-to-file>`

> The full path to a file that contains a phylogenetic tree in NEWICK format.

##### `-o <path-to-directory>`

> The full path to an existing directory to write the output files.

##### `-m`

> The full path to a map file that contains the tip/taxon labels and their corresponding groupings.

##### `--support`

> A flag indicating the input tree contains support values and that they should be included in the output files.

#### Example Use:

```
python MonoPhylo.py -t bin/Analysis/Rooted_RAxML_bipartitions.Iguania.tre -o bin/Analysis/Output1/ -m bin/Analysis/Iguania_groupings.txt --support
```

The above command will assess all groupings defined in `Iguania_groupings.txt` in the tree file `Rooted_RAxML_bipartitions.Iguania.tre`. All output files will be created in the specified output directory.

In this usage the output files will contain an additional column with information about support values, because we used the `--support` flag. Here is an example of the truncated contents from one of the results files (in this case genera):

```
Grouping	Number_Contained_Taxa	Monophyletic	Category	Support	Number_Interfering_Species	Interfering_Species
Acanthocercus	5	FALSE	Polyphyletic	NA	10	Agama_robecchii, Pseudotrapelus_aqabensis, Pseudotrapelus_chlodnickii, Pseudotrapelus_dhofarensis, Pseudotrapelus_jensvindumi, Pseudotrapelus_neumanni, Pseudotrapelus_sinaitus, Xenagama_batillifera, Xenagama_taylori, Xenagama_wilmsi
Acanthosaura	4	TRUE	Monophyletic	100	0	
Agama	38	FALSE	Polyphyletic	NA	14	Acanthocercus_adramitanus, Acanthocercus_annectens, Acanthocercus_atricollis, Acanthocercus_cyanogaster, Acanthocercus_yemensis, Pseudotrapelus_aqabensis, Pseudotrapelus_chlodnickii, Pseudotrapelus_dhofarensis, Pseudotrapelus_jensvindumi, Pseudotrapelus_neumanni, Pseudotrapelus_sinaitus, Xenagama_batillifera, Xenagama_taylori, Xenagama_wilmsi
Amblyrhynchus	1	NA	NA	NA	0	
Amphibolurus	2	TRUE	Monophyletic	100	0	
Anisolepis	2	TRUE	Monophyletic	100	0	
Anolis	324	TRUE	Monophyletic	95	0	
Aphaniotis	1	NA	NA	NA	0	
Archaius	1	NA	NA	NA	0	
Basiliscus	4	TRUE	Monophyletic	96	0	
```


