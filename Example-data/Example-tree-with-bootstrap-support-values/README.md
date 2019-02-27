## Example Analysis: Tree with bootstrap support values

---------------

This directory contains all the input files, output files, and instructions to replicate this **MonoPhylo** analysis of a tree with bootstrap support values.

The input tree (`RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre`) was generated from a supermatrix created for Iguania using **SuperCRUNCH**. Specifically, I used RAxML to perform 100 bootstrap replicates and used them to score the best ML tree. 

Below are the major steps of this **MonoPhylo** analysis and the commands used for each step.

## 1. Obtaining a list of tree tips

This particular tree has tip labels that represent species labels, and they follow the format `Genus_species`. This allowed me to use the `--genus` flag for this step:

```
python /bin/MonoPhylo/MonoPhylo.py -t /bin/Example-tree-with-bootstrap-support-values/RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre -o /binExample-tree-with-bootstrap-support-values/Output1 --write_tips --genus
```

The output on the screen looked like this:

```
Found 1426 tips in tree.

Found 111 genera across tree.

Writing genus and species labels to Species_List.txt in the output directory.

Writing genus labels to Genus_List.txt in the output directory.
```

This step produced the `Species_List.txt` and `Genus_List.txt` output files located in the directory `Output1`.

## 2. Defining groups for the tip labels

I used the `Species_List.txt` file located in the directory `Output1` as the starting point for the required map file, which defines all the groupings. I opened this file in Excel and edited it as a spreadsheet (`Iguania_Grouping_Key.xlsx`). I then exported it as a tab-delimited text file, making sure to use UTF-8 encoding and Unix line breaks (checked with a separate text editor, BBEDit). The resulting map file (`Iguania_Grouping_Key.txt`) was used for assessing the groups.

## 3. Ensuring the tree is properly rooted

I rooted the tree file using the MRCA of a set of two taxa. I used the names from the `Species_List.txt` to ensure they were correctly spelled and present in the tree. I used the optional `--write_root` flag to write the rooted tree to an output file:

```
python /bin/MonoPhylo/MonoPhylo.py -t /bin//Example-tree-with-bootstrap-support-values/RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre -o /bin/Example-tree-with-bootstrap-support-values/Output2 --root --tip1 Hoplocercus_spinosus --tip2 Leiocephalus_macropus --write_root
```

The output on the screen looked like this:

```
Found 1426 tips in tree.

Using tips ['Hoplocercus_spinosus', 'Leiocephalus_macropus'] to root tree.

Wrote rooted tree file 'Rooted_RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre' to directory: /bin/Example-tree-with-bootstrap-support-values/Output2.
```

This produced the rooted tree file (`Rooted_RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre`) in the directory `Output2`. I inspected the tree to ensure the root was placed where I intended, and used the rooted tree file for the final step. Note that the support values from the input tree file were preserved in the rooted tree file - the ETE3 package does a great job reading and writing trees.

## 4. Assessing the phylogenetic status of groups

I used the map file I created (`Iguania_Grouping_Key.txt`) and the rooted tree file (`Rooted_RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre`) to run the final step. The input tree included bootstrap support values, so I included the optional `--support` flag:

```
python /bin/MonoPhylo/MonoPhylo.py -t /bin//Example-tree-with-bootstrap-support-values/Rooted_RAxML_bipartitions.Iguania_SuperCRUNCH_NCBI_Concatenated_Alignment.tre -o /bin/Example-tree-with-bootstrap-support-values/Output3  -m /bin/Example-tree-with-bootstrap-support-values/Iguania_Grouping_Key.txt --support
```

The output on the screen looked like this:

```
Found 1426 tips in tree.


Examining tips and groupings in map file.

Category: Genus
	Subgroup Acanthocercus contains 5 taxa.
	Subgroup Acanthosaura contains 4 taxa.
	Subgroup Agama contains 38 taxa.
	Subgroup Amblyrhynchus contains 1 taxa.
	Subgroup Amphibolurus contains 2 taxa.
	Subgroup Anisolepis contains 2 taxa.
	Subgroup Anolis contains 324 taxa.
	Subgroup Aphaniotis contains 1 taxa.
	Subgroup Archaius contains 1 taxa.
	Subgroup Basiliscus contains 4 taxa.
	Subgroup Brachylophus contains 3 taxa.
	Subgroup Bradypodion contains 17 taxa.
	Subgroup Bronchocela contains 5 taxa.
	Subgroup Brookesia contains 28 taxa.
	Subgroup Bufoniceps contains 1 taxa.
	Subgroup Cachryx contains 2 taxa.
	Subgroup Callisaurus contains 1 taxa.
	Subgroup Calotes contains 15 taxa.
	Subgroup Calumma contains 31 taxa.
	Subgroup Ceratophora contains 5 taxa.
	Subgroup Chalarodon contains 1 taxa.
	Subgroup Chamaeleo contains 14 taxa.
	Subgroup Chelosania contains 1 taxa.
	Subgroup Chlamydosaurus contains 1 taxa.
	Subgroup Conolophus contains 3 taxa.
	Subgroup Cophosaurus contains 1 taxa.
	Subgroup Cophotis contains 2 taxa.
	Subgroup Coryphophylax contains 1 taxa.
	Subgroup Corytophanes contains 3 taxa.
	Subgroup Crotaphytus contains 9 taxa.
	Subgroup Ctenoblepharys contains 1 taxa.
	Subgroup Ctenophorus contains 24 taxa.
	Subgroup Ctenosaura contains 13 taxa.
	Subgroup Cyclura contains 8 taxa.
	Subgroup Diplolaemus contains 4 taxa.
	Subgroup Diporiphora contains 16 taxa.
	Subgroup Dipsosaurus contains 1 taxa.
	Subgroup Draco contains 34 taxa.
	Subgroup Enyalioides contains 14 taxa.
	Subgroup Enyalius contains 9 taxa.
	Subgroup Eurolophosaurus contains 3 taxa.
	Subgroup Furcifer contains 21 taxa.
	Subgroup Gambelia contains 3 taxa.
	Subgroup Gonocephalus contains 9 taxa.
	Subgroup Gowidon contains 2 taxa.
	Subgroup Holbrookia contains 5 taxa.
	Subgroup Hoplocercus contains 1 taxa.
	Subgroup Hydrosaurus contains 3 taxa.
	Subgroup Hypsilurus contains 5 taxa.
	Subgroup Iguana contains 2 taxa.
	Subgroup Intellagama contains 1 taxa.
	Subgroup Japalura contains 11 taxa.
	Subgroup Kinyongia contains 21 taxa.
	Subgroup Laemanctus contains 1 taxa.
	Subgroup Laudakia contains 6 taxa.
	Subgroup Leiocephalus contains 15 taxa.
	Subgroup Leiolepis contains 5 taxa.
	Subgroup Leiosaurus contains 4 taxa.
	Subgroup Liolaemus contains 181 taxa.
	Subgroup Lophocalotes contains 2 taxa.
	Subgroup Lophognathus contains 2 taxa.
	Subgroup Lophosaurus contains 3 taxa.
	Subgroup Lyriocephalus contains 1 taxa.
	Subgroup Malayodracon contains 1 taxa.
	Subgroup Mantheyus contains 1 taxa.
	Subgroup Microlophus contains 21 taxa.
	Subgroup Moloch contains 1 taxa.
	Subgroup Morunasaurus contains 1 taxa.
	Subgroup Nadzikambia contains 2 taxa.
	Subgroup Oplurus contains 6 taxa.
	Subgroup Otocryptis contains 2 taxa.
	Subgroup Palleon contains 2 taxa.
	Subgroup Paralaudakia contains 6 taxa.
	Subgroup Petrosaurus contains 3 taxa.
	Subgroup Phoxophrys contains 1 taxa.
	Subgroup Phrynocephalus contains 27 taxa.
	Subgroup Phrynosoma contains 18 taxa.
	Subgroup Phymaturus contains 44 taxa.
	Subgroup Physignathus contains 1 taxa.
	Subgroup Plica contains 3 taxa.
	Subgroup Pogona contains 7 taxa.
	Subgroup Polychrus contains 8 taxa.
	Subgroup Pristidactylus contains 6 taxa.
	Subgroup Psammophilus contains 1 taxa.
	Subgroup Pseudocalotes contains 15 taxa.
	Subgroup Pseudotrapelus contains 6 taxa.
	Subgroup Ptyctolaemus contains 2 taxa.
	Subgroup Rankinia contains 1 taxa.
	Subgroup Rhampholeon contains 15 taxa.
	Subgroup Rieppeleon contains 3 taxa.
	Subgroup Saara contains 3 taxa.
	Subgroup Salea contains 2 taxa.
	Subgroup Sarada contains 3 taxa.
	Subgroup Sauromalus contains 4 taxa.
	Subgroup Sceloporus contains 89 taxa.
	Subgroup Sitana contains 5 taxa.
	Subgroup Stellagama contains 1 taxa.
	Subgroup Stenocercus contains 40 taxa.
	Subgroup Strobilurus contains 1 taxa.
	Subgroup Trapelus contains 8 taxa.
	Subgroup Trioceros contains 33 taxa.
	Subgroup Tropidurus contains 28 taxa.
	Subgroup Tympanocryptis contains 9 taxa.
	Subgroup Uma contains 6 taxa.
	Subgroup Uracentron contains 2 taxa.
	Subgroup Uranoscodon contains 1 taxa.
	Subgroup Uromastyx contains 14 taxa.
	Subgroup Urosaurus contains 8 taxa.
	Subgroup Urostrophus contains 2 taxa.
	Subgroup Uta contains 3 taxa.
	Subgroup Xenagama contains 3 taxa.
Category: Family
	Subgroup Agamidae contains 325 taxa.
	Subgroup Chamaeleonidae contains 188 taxa.
	Subgroup Corytophanidae contains 8 taxa.
	Subgroup Crotaphytidae contains 12 taxa.
	Subgroup Dactyloidae contains 324 taxa.
	Subgroup Hoplocercidae contains 16 taxa.
	Subgroup Iguanidae contains 37 taxa.
	Subgroup Leiocephalidae contains 15 taxa.
	Subgroup Leiosauridae contains 27 taxa.
	Subgroup Liolaemidae contains 226 taxa.
	Subgroup Opluridae contains 7 taxa.
	Subgroup Phrynosomatidae contains 134 taxa.
	Subgroup Polychrotidae contains 8 taxa.
	Subgroup Tropiduridae contains 99 taxa.
Category: SubFamily
	Subgroup Agaminae contains 101 taxa.
	Subgroup Amphibolurinae contains 76 taxa.
	Subgroup Draconinae contains 123 taxa.
	Subgroup Enyaliinae contains 13 taxa.
	Subgroup Hydrosaurinae contains 3 taxa.
	Subgroup Leiolepidinae contains 5 taxa.
	Subgroup Leiosaurinae contains 14 taxa.
	Subgroup Phrynosomatinae contains 31 taxa.
	Subgroup Sceloporinae contains 103 taxa.
	Subgroup Uromastycinae contains 17 taxa.
Category: MajorGroup
	Subgroup Acrodonta contains 513 taxa.
	Subgroup Pleurodonta contains 913 taxa.




Examining Genus:
	Acanthocercus is Polyphyletic
	Acanthosaura is Monophyletic
	Agama is Polyphyletic
	Amblyrhynchus contains only 1 taxon
	Amphibolurus is Monophyletic
	Anisolepis is Monophyletic
	Anolis is Monophyletic
	Aphaniotis contains only 1 taxon
	Archaius contains only 1 taxon
	Basiliscus is Monophyletic
	Brachylophus is Monophyletic
	Bradypodion is Monophyletic
	Bronchocela is Monophyletic
	Brookesia is Monophyletic
	Bufoniceps contains only 1 taxon
	Cachryx is Monophyletic
	Callisaurus contains only 1 taxon
	Calotes is Monophyletic
	Calumma is Monophyletic
	Ceratophora is Monophyletic
	Chalarodon contains only 1 taxon
	Chamaeleo is Monophyletic
	Chelosania contains only 1 taxon
	Chlamydosaurus contains only 1 taxon
	Conolophus is Monophyletic
	Cophosaurus contains only 1 taxon
	Cophotis is Monophyletic
	Coryphophylax contains only 1 taxon
	Corytophanes is Monophyletic
	Crotaphytus is Monophyletic
	Ctenoblepharys contains only 1 taxon
	Ctenophorus is Polyphyletic
	Ctenosaura is Monophyletic
	Cyclura is Monophyletic
	Diplolaemus is Monophyletic
	Diporiphora is Monophyletic
	Dipsosaurus contains only 1 taxon
	Draco is Monophyletic
	Enyalioides is Polyphyletic
	Enyalius is Paraphyletic
	Eurolophosaurus is Monophyletic
	Furcifer is Monophyletic
	Gambelia is Monophyletic
	Gonocephalus is Monophyletic
	Gowidon is Monophyletic
	Holbrookia is Monophyletic
	Hoplocercus contains only 1 taxon
	Hydrosaurus is Monophyletic
	Hypsilurus is Polyphyletic
	Iguana is Monophyletic
	Intellagama contains only 1 taxon
	Japalura is Polyphyletic
	Kinyongia is Polyphyletic
	Laemanctus contains only 1 taxon
	Laudakia is Monophyletic
	Leiocephalus is Monophyletic
	Leiolepis is Monophyletic
	Leiosaurus is Monophyletic
	Liolaemus is Monophyletic
	Lophocalotes is Monophyletic
	Lophognathus is Monophyletic
	Lophosaurus is Monophyletic
	Lyriocephalus contains only 1 taxon
	Malayodracon contains only 1 taxon
	Mantheyus contains only 1 taxon
	Microlophus is Monophyletic
	Moloch contains only 1 taxon
	Morunasaurus contains only 1 taxon
	Nadzikambia is Monophyletic
	Oplurus is Polyphyletic
	Otocryptis is Paraphyletic
	Palleon is Monophyletic
	Paralaudakia is Monophyletic
	Petrosaurus is Monophyletic
	Phoxophrys contains only 1 taxon
	Phrynocephalus is Monophyletic
	Phrynosoma is Monophyletic
	Phymaturus is Monophyletic
	Physignathus contains only 1 taxon
	Plica is Monophyletic
	Pogona is Monophyletic
	Polychrus is Monophyletic
	Pristidactylus is Paraphyletic
	Psammophilus contains only 1 taxon
	Pseudocalotes is Polyphyletic
	Pseudotrapelus is Monophyletic
	Ptyctolaemus is Monophyletic
	Rankinia contains only 1 taxon
	Rhampholeon is Monophyletic
	Rieppeleon is Monophyletic
	Saara is Monophyletic
	Salea is Polyphyletic
	Sarada is Monophyletic
	Sauromalus is Monophyletic
	Sceloporus is Monophyletic
	Sitana is Monophyletic
	Stellagama contains only 1 taxon
	Stenocercus is Monophyletic
	Strobilurus contains only 1 taxon
	Trapelus is Monophyletic
	Trioceros is Monophyletic
	Tropidurus is Polyphyletic
	Tympanocryptis is Monophyletic
	Uma is Monophyletic
	Uracentron is Polyphyletic
	Uranoscodon contains only 1 taxon
	Uromastyx is Monophyletic
	Urosaurus is Monophyletic
	Urostrophus is Paraphyletic
	Uta is Monophyletic
	Xenagama is Monophyletic
Found 68 monophyletic groups out of 84 testable groupings.
Of 111 total groupings, 27 contained a single taxon and were ignored.


Examining Family:
	Agamidae is Monophyletic
	Chamaeleonidae is Monophyletic
	Corytophanidae is Monophyletic
	Crotaphytidae is Monophyletic
	Dactyloidae is Monophyletic
	Hoplocercidae is Monophyletic
	Iguanidae is Monophyletic
	Leiocephalidae is Monophyletic
	Leiosauridae is Monophyletic
	Liolaemidae is Monophyletic
	Opluridae is Monophyletic
	Phrynosomatidae is Monophyletic
	Polychrotidae is Monophyletic
	Tropiduridae is Monophyletic
Found 14 monophyletic groups out of 14 testable groupings.
Of 14 total groupings, 0 contained a single taxon and were ignored.


Examining SubFamily:
	Agaminae is Monophyletic
	Amphibolurinae is Monophyletic
	Draconinae is Monophyletic
	Enyaliinae is Monophyletic
	Hydrosaurinae is Monophyletic
	Leiolepidinae is Monophyletic
	Leiosaurinae is Monophyletic
	Phrynosomatinae is Monophyletic
	Sceloporinae is Monophyletic
	Uromastycinae is Monophyletic
Found 10 monophyletic groups out of 10 testable groupings.
Of 10 total groupings, 0 contained a single taxon and were ignored.


Examining MajorGroup:
	Acrodonta is Monophyletic
	Pleurodonta is Monophyletic
Found 2 monophyletic groups out of 2 testable groupings.
Of 2 total groupings, 0 contained a single taxon and were ignored.
```

The first half of the output on screen shows the groupings found and how many taxa are included in each. The second half is the assessment for each 'category' of groupings (represented by a column), and a quick summary of the results. Note that any group that contains only one taxon is automatically excluded because it isn't possible to assess monophyly. 

This produced the following output files in `Output3`:

+ `All_Groups_results.txt`
+ `Group_Family_results.txt`
+ `Group_Genus_results.txt`
+ `Group_MajorGroup_results.txt`
+ `Group_SubFamily_results.txt`
+ `Summary.log`



