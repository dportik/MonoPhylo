import sys
import os
import shutil
import argparse
from ete3 import Tree

def get_args():
    """Get arguments from CLI"""
    parser = argparse.ArgumentParser(
            description="""------------------------------------------------------------------------------
    MonoPhylo: A tool for examining phylogenetic relationships in newick tree files. For
    usage instructions, please see documentation available at: https://github.com/dportik/MonoPhylo.
	------------------------------------------------------------------------------""")
    parser.add_argument("-t", "--tree",
                            required=True,
                            help="REQUIRED: The full path to a newick tree file.")
    
    parser.add_argument("-o", "--out_dir",
                            required=True,
                            help="REQUIRED: The full path to an existing directory to write "
                            "output files.")
    
    parser.add_argument("-m", "--map",
                            required=False,
                            default=None,
                            help="OPTIONAL: The full path to a map file containing tip names "
                            "and grouping schemes for examining monophyly.")
    
    parser.add_argument("--write_tips",
                            required=False,
                            action='store_true',
                            help="OPTIONAL: Obtain list of tips in tree and write to output file.")
    
    parser.add_argument("--genus",
                            required=False,
                            action='store_true',
                            help="OPTIONAL: Obtain genus names from tips in tree. Requires "
                            "tips to be labeled in GENUS_SPECIES format.")
    
    parser.add_argument("--support",
                            required=False,
                            action='store_true',
                            help="OPTIONAL: Obtain support values for monophyletic groupings "
                            "- requires a tree with support values present.")
    
    parser.add_argument("--root",
                            required=False,
                            action='store_true',
                            help="OPTIONAL: Root tree using MRCA of tree tip labels specified "
                            "using tip flags (minimally -tip1 and -tip2).")
    
    parser.add_argument("--tip1",
                            required=False,
                            default=None,
                            help="Required for --root: The name of the first tree tip.")
    
    parser.add_argument("--tip2",
                            required=False,
                            default=None,
                            help="Required for --root: The name of the second tree tip.")
    
    parser.add_argument("--tip3",
                            required=False,
                            default=None,
                            help="Optional for --root: The name of a third tree tip.")
    
    parser.add_argument("--tip4",
                            required=False,
                            default=None,
                            help="Optional for --root: The name of a fourth tree tip.")
    
    parser.add_argument("--tip5",
                            required=False,
                            default=None,
                            help="Optional for --root: The name of a fifth tree tip.")
    
    parser.add_argument("--write_root",
                            required=False,
                            action='store_true',
                            help="Optional for --root: Write the rooted tree to an output file (newick format).")
    
    return parser.parse_args()

def read_tree(t_file):
    """
    Read tree file, raise errors if not formatted correctly.
    """
    try:
        tree = Tree(t_file)
    except:
        try:
            with open(t_file, 'r') as fh_in:
                newick = [line.strip() for line in fh_in if line.startswith('(') and line.endswith(';')]
            tree = Tree(newick[0])
        except:
            raise TypeError("\n\nFILE ERROR: Not able to read tree from file path or the string in the file.\n\nCheck file to ensure it is a proprely formatted newick tree.\n\n")
    return tree

def get_taxa(tree):
    """
    Get a list of tips/taxa in the tree,
    sorted alphabetically.
    """
    taxa = sorted([leaf.name for leaf in tree])
    print("\n\nFound {} tips in tree.\n".format(len(taxa)))
    return taxa 

def root_tree(tree, tiplist, taxa):
    """
    Root tree using the taxa list provided. Check
    to ensure taxa are actually valid tips first.
    """
    for t in tiplist:
        if t not in taxa:
            raise NameError("\n\n{} does not match any tip found in this tree.\n\n"
                                "Try writing tips to file and obtaining names directly "
                                "from file.\n\n".format(t))
    print("\nUsing tips {} to root tree.\n".format(tiplist))
    ancestor = tree.get_common_ancestor(tiplist)
    #print ancestor
    tree.set_outgroup(ancestor)
    
def root_writer(infile, tree, out_dir):
    outname = "Rooted_{}".format(infile.split('/')[-1])
    tree.write(format=0, outfile=outname)
    print("\nWrote rooted tree file '{1}' to directory: {0}.\n".format(out_dir, outname))

def get_genera(taxa):
    """
    If names follow Genus_species, obtain all unique Genus
    components, return as list sorted alphabetically.
    """
    genera = sorted(set([t.split('_')[0] for t in taxa]))
    print("\nFound {} genera across tree.\n".format(len(genera)))
    return genera

def genus_dict(taxa, genera):
    """
    Create a dictionary where each genus is a key and
    a list of contained species are the corresponding 
    value.
    """
    gdicts = {}
    for g in genera:
        taxa_list = [t for t in taxa if t.split('_')[0] == g]
        gdicts[g] = taxa_list
    return gdicts

def write_map_file_genus(gdicts):
    """
    Write the lists of genera and species
    labels to corresponding output files.
    """
    print("\nWriting genus and species labels to Species_List.txt in the output directory.\n")
    genera = sorted(gdicts.keys())
    with open('Species_List.txt', 'a') as fh_out:
        fh_out.write("{}\t{}\n".format("Species","Genus"))
        for g in genera:
            for species in gdicts[g]:
                #print species, g
                fh_out.write("{}\t{}\n".format(species,g))
    print("\nWriting genus labels to Genus_List.txt in the output directory.\n")
    with open('Genus_List.txt', 'a') as fh_out:
        fh_out.write("{}\n".format("Genus"))
        for g in genera:
            fh_out.write("{}\n".format(g))
                
def write_map_file_tip(taxa):
    """
    Write list of tips to output file (used
    if --genus not supplied).
    """
    print("\nWriting {} tip labels to Tip_List.txt in the output directory.\n".format(len(taxa)))
    with open('Tip_List.txt', 'a') as fh_out:
        fh_out.write("{}\n".format("Tip"))
        for t in taxa:
            fh_out.write("{}\n".format(t))

def groups_to_dicts(contents, groups, i, taxa):
    """
    Return a dictionary where group labels are keys 
    and taxa lists are values.
    """
    gdict = {}
    for g in groups:
        taxa_list = [c[0] for c in contents[1:] if c[i] == g and c[0] in taxa]
        if taxa_list:
            gdict[g] = taxa_list
            print("\tSubgroup {} contains {} taxa.".format(g, len(taxa_list)))
    return gdict
            
def parse_mapfile(map, taxa):
    """
    For each grouping, create a list containing: [Group Label, Group Dictionary]
    Place all in one list:[ [Group1 Label, Group1 Dictionary], [Group2 Label, Group2 Dictionary], etc.]
    """
    print("\nExamining tips and groupings in map file.\n")
    with open(map, 'r') as fh:
        contents = [l.strip().split('\t') for l in fh if l.strip()]
        
    task_list = []
    cols = len(contents[0])
    for i in range(1,cols):
        label = contents[0][i]
        groups = sorted(set([c[i] for c in contents[1:] if c[i] != "NA"]))
        print "Category: {}".format(label)
        gdict = groups_to_dicts(contents, groups, i, taxa)
        task_list.append([label, gdict])
    return task_list

def test_monophyly(label, dicts, tree):
    """
    Where d is a dictionary with group labels are keys
    and corresponding lists of species/tips are values.
    """
    outname = "{0}_{1}_results.txt".format("Group", label)
    log = "Summary.log"
    
    groupings = sorted(dicts.keys())
    mono_count = int(0)
    skip_count = int(0)
    with open(log, 'a') as fh_log:
        print("\n\nExamining {}:".format(label))
        fh_log.write("Examining {}:\n".format(label))
        with open(outname, 'a') as fh_out:
            fh_out.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format("Grouping", "Number_Contained_Taxa", 
                                                                     "Monophyletic", "Category", 
                                                                     "Number_Interfering_Species", 
                                                                     "Interfering_Species"))
            for g in groupings:
                results = tree.check_monophyly(values = dicts[g], target_attr="name", unrooted = True)
                names = sorted([r.name for r in results[2]])

                if len(dicts[g]) > 1:
                    truth = results[0]
                    mono = results[1].capitalize()
                    print("\t{0} is {1}".format(g, mono))
                    fh_log.write("\t{0} is {1}\n".format(g, mono))
                else:
                    truth = "NA"
                    mono = "NA"
                    print("\t{0} contains only 1 taxon".format(g))
                    fh_log.write("\t{0} contains only 1 taxon\n".format(g))
                
                fh_out.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(g, len(dicts[g]), truth, mono,
                                                                         len(names), ", ".join(names)))

                if mono == "Monophyletic":
                    mono_count += 1
                elif mono == "NA":
                    skip_count += 1
                    
        print("Found {0} monophyletic groups out of {1} testable groupings."
                  "\nOf {2} total groupings, {3} contained a single taxon "
                  "and were ignored.\n\n".format(mono_count, (len(groupings)-skip_count),
                                                     len(groupings), skip_count))
        
        fh_log.write("Found {0} monophyletic groups out of {1} testable groupings."
                         "\nOf {2} total groupings, {3} contained a single taxon "
                         "and were ignored.\n\n".format(mono_count, (len(groupings)-skip_count),
                                                            len(groupings), skip_count))
        
def test_monophyly_support(label, dicts, tree):
    """
    Where d is a dictionary with group labels are keys
    and corresponding lists of species/tips are values.
    """
    outname = "{0}_{1}_results.txt".format("Group", label)
    log = "Summary.log"
    
    groupings = sorted(dicts.keys())
    mono_count = int(0)
    skip_count = int(0)
    
    with open(log, 'a') as fh_log:
        print("\n\nExamining {}:".format(label))
        fh_log.write("Examining {}:\n".format(label))
        with open(outname, 'a') as fh_out:
            fh_out.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format("Grouping", "Number_Contained_Taxa",
                                                                          "Monophyletic", "Category", "Support",
                                                                          "Number_Interfering_Species", "Interfering_Species"))
            for g in groupings:
                results = tree.check_monophyly(values = dicts[g], target_attr="name", unrooted = True)
                names = sorted([r.name for r in results[2]])

                if len(dicts[g]) > 1:
                    truth = results[0]
                    mono = results[1].capitalize()
                    print("\t{0} is {1}".format(g, mono))
                    fh_log.write("\t{0} is {1}\n".format(g, mono))
                else:
                    truth = "NA"
                    mono = "NA"
                    print("\t{0} contains only 1 taxon".format(g))
                    fh_log.write("\t{0} contains only 1 taxon\n".format(g))
                
                if results[1] == "monophyletic" and len(dicts[g]) > 1:
                    internal_node = tree.get_common_ancestor(dicts[g])
                    support = internal_node.support
                else:
                    support = "NA"
                    
                fh_out.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(g, len(dicts[g]), truth, mono,
                                                                              support, len(names), ", ".join(names)))

                if mono == "Monophyletic":
                    mono_count += 1
                elif mono == "NA":
                    skip_count += 1
                    
        print("Found {0} monophyletic groups out of {1} testable groupings."
                  "\nOf {2} total groupings, {3} contained a single taxon and "
                  "were ignored.\n\n".format(mono_count, (len(groupings)-skip_count),
                                                 len(groupings), skip_count))
        
        fh_log.write("Found {0} monophyletic groups out of {1} testable groupings."
                         "\nOf {2} total groupings, {3} contained a single taxon and "
                         "were ignored.\n\n".format(mono_count, (len(groupings)-skip_count),
                                                        len(groupings), skip_count))
        
def main():
    args = get_args()
    os.chdir(args.out_dir)
    tree = read_tree(args.tree)
    taxa = get_taxa(tree)
    
    if args.root is True:
        tlist = [args.tip1, args.tip2, args.tip3, args.tip4, args.tip5]
        tip_list = [t for t in tlist if t is not None]
        root_tree(tree, tip_list, taxa)
        if args.write_root is True:
            root_writer(args.tree, tree, args.out_dir)
            
    if args.genus is True:
        genera = get_genera(taxa)
        gdicts = genus_dict(taxa, genera)
        
    if args.write_tips is True:
        if args.genus is True:
            write_map_file_genus(gdicts)
        else:
            write_map_file_tip(taxa)
            
    if args.map:
        fname = args.tree.split('/')[-1].replace('.txt','')
        task_list = parse_mapfile(args.map, taxa)
        for t in task_list:
            if args.support is False:
                test_monophyly(t[0], t[1], tree)
            elif args.support is True:
                test_monophyly_support(t[0], t[1], tree)
                
        flist = sorted([f for f in os.listdir('.') if f.endswith('_results.txt')])
        if len(flist) >= int(1):
            with open('All_Groups_results.txt', 'a') as fh_out:
                with open(flist[0], 'r') as fh1:
                    fh_out.write(fh1.read())
                for f in flist[1:]:
                    with open(f, 'r') as fh2:
                        lines = fh2.readlines()
                        for l in lines[1:]:
                            fh_out.write(l)
        
if __name__ == '__main__':
    main()

