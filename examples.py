# examples of dictionaries 

# expression


input_dict = {
    
    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_expression',
    
    # REQUIRED!
    # avaiable of vector types (ssAAV / scAAV / lentiviral / regular)
    'vector_type':'ssAAV',
    
    # REQUIRED!
    # avaiable of vector functions (expression / rnai)
    # in this case 'vector_function':'expression'
    'vector_function':'expression',
    
    # REQUIRED!
    # avaiavle options (human / mouse / both)
    # 'both' - creating vector function adjusted for both species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # list of coding sequences (CDS) provided to make expression from the vector
    # the CSD sequences the user can obtain from ...
    # amount of sequences is not restricted as the user must remember that the length of whole vector is limited
    # excide the relevant vector size can decrease vector working
    # if the user wants to not include any sequences only fluorescent_tag, provide ['']
    # sequences orientation 5' ---> 3' - sense
    'sequences':['ATGGCGATGAGCAGCGGCGGCAGTGGTGGCGGCGTCCCGGAGCAGGAGGATTCCGTGCTGTTCCGGCGCGGCACAGGCCAGAGCGATGATTCTGACATTTGGGATGATACAGCACTGATAAAAGCATATGATAAAGCTGTGGCTTCATTTAAGCATGCTCTAAAGAATGGTGACATTTGTGAAACTTCGGGTAAACCAAAAACCACACCTAAAAGAAAACCTGCTAAGAAGAATAAAAGCCAAAAGAAGAATACTGCAGCTTCCTTACAACAGTGGAAAGTTGGGGACAAATGTTCTGCCATTTGGTCAGAAGACGGTTGCATTTACCCAGCTACCATTGCTTCAATTGATTTTAAGAGAGAAACCTGTGTTGTGGTTTACACTGGATATGGAAATAGAGAGGAGCAAAATCTGTCCGATCTACTTTCCCCAATCTGTGAAGTAGCTAATAATATAGAACAAAATGCTCAAGAGAATGAAAATGAAAGCCAAGTTTCAACAGATGAAAGTGAGAACTCCAGGTCTCCTGGAAATAAATCAGATAACATCAAGCCCAAATCTGCTCCATGGAACTCTTTTCTCCCTCCACCACCCCCCATGCCAGGGCCAAGACTGGGACCAGGAAAGCCAGGTCTAAAATTCAATGGCCCACCACCGCCACCGCCACCACCACCACCCCACTTACTATCATGCTGGCTGCCTCCATTTCCTTCTGGACCACCAATAATTCCCCCACCACCTCCCATATGTCCAGATTCTCTTGATGATGCTGATGCTTTGGGAAGTATGTTAATTTCATGGTACATGAGTGGCTATCATACTGGCTATTATATGTTTCCTGAGGCCTCCCTAAAAGCCGAGCAGATGCCAGCACCATGCTTCCTGTAA',
                 'ATGGCGATGAGCAGCGGCGGCAGTGGTGGCGGCGTCCCGGAGCAGGAGGATTCCGTGCTGTTCCGGCGCGGCACAGGCCAGAGCGATGATTCTGACATTTGGGATGATACAGCACTGATAAAAGCATATGATAAAGCTGTGGCTTCATTTAAGCATGCTCTAAAGAATGGTGACATTTGTGAAACTTCGGGTAAACCAAAAACCACACCTAAAAGAAAACCTGCTAAGAAGAATAAAAGCCAAAAGAAGAATACTGCAGCTTCCTTACAACAGTGGAAAGTTGGGGACAAATGTTCTGCCATTTGGTCAGAAGACGGTTGCATTTACCCAGCTACCATTGCTTCAATTGATTTTAAGAGAGAAACCTGTGTTGTGGTTTACACTGGATATGGAAATAGAGAGGAGCAAAATCTGTCCGATCTACTTTCCCCAATCTGTGAAGTAGCTAATAATATAGAACAAAATGCTCAAGAGAATGAAAATGAAAGCCAAGTTTCAACAGATGAAAGTGAGAACTCCAGGTCTCCTGGAAATAAATCAGATAACATCAAGCCCAAATCTGCTCCATGGAACTCTTTTCTCCCTCCACCACCCCCCATGCCAGGGCCAAGACTGGGACCAGGAAAGCCAGGTCTAAAATTCAATGGCCCACCACCGCCACCGCCACCACCACCACCCCACTTACTATCATGCTGGCTGCCTCCATTTCCTTCTGGACCACCAATAATTCCCCCACCACCTCCCATATGTCCAGATTCTCTTGATGATGCTGATGCTTTGGGAAGTATGTTAATTTCATGGTACATGAGTGGCTATCATACTGGCTATTATATGTTTCCTGAGGCCTCCCTAAAAGCCGAGCAGATGCCAGCACCATGCTTCCTGTAA'],
    # list of names of coding sequences
    # amount of names should be equal with amount of sequences
    # if provided no sequences, provide ['']
    'sequences_names':['SMN1','SMN2'],
    
    # REQUIRED!
    # sequence of provided promoter
    # name and sequence the user can take from metadata['promoters'] (load_metadata())
    # for coding sequences the user should choose the promoter of coding genes (metadata['promoters']['type'] == 'coding')
    # sequence orientation 5' ---> 3' - sense
    'promoter_sequence':'GGGCTGGAAGCTACCTTTGACATCATTTCCTCTGCGAATGCATGTATAATTTCTACAGAACCTATTAGAAAGGATCACCCAGCCTCTGCTTTTGTACAACTTTCCCTTAAAAAACTGCCAATTCCACTGCTGTTTGGCCCAATAGTGAGAACTTTTTCCTGCTGCCTCTTGGTGCTTTTGCCTATGGCCCCTATTCTGCCTGCTGAAGACACTCTTGCCAGCATGGACTTAAACCCCTCCAGCTCTGACAATCCTCTTTCTCTTTTGTTTTACATGAAGGGTCTGGCAGCCAAAGCAATCACTCAAAGTTCAAACCTTATCATTTTTTGCTTTGTTCCTCTTGGCCTTGGTTTTGTACATCAGCTTTGAAAATACCATCCCAGGGTTAATGCTGGGGTTAATTTATAACTAAGAGTGCTCTAGTTTTGCAATACAGGACATGCTATAAAAATGGAAAGAT',
    # REQUIRED!
    # name of provided promoter sequence
    'promoter_name':'TBG',
    
    # POSSIBLE!
    # sequence of provided enhancer
    # name and sequence the user can take from metadata['regulators'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'regulator_sequence':'CGATAATCAACCTCTGGATTACAAAATTTGTGAAAGATTGACTGGTATTCTTAACTATGTTGCTCCTTTTACGCTATGTGGATACGCTGCTTTAATGCCTTTGTATCATGCTATTGCTTCCCGTATGGCTTTCATTTTCTCCTCCTTGTATAAATCCTGGTTGCTGTCTCTTTATGAGGAGTTGTGGCCCGTTGTCAGGCAACGTGGCGTGGTGTGCACTGTGTTTGCTGACGCAACCCCCACTGGTTGGGGCATTGCCACCACCTGTCAGCTCCTTTCCGGGACTTTCGCTTTCCCCCTCCCTATTGCCACGGCGGAACTCATCGCCGCCTGCCTTGCCCGCTGCTGGACAGGGGCTCGGCTGTTGGGCACTGACAATTCCGTGGTGTTGTCGGGGAAGCTGACGTCCTTTCCATGGCTGCTCGCCTGTGTTGCCACCTGGATTCTGCGCGGGACGTCCTTCTGCTACGTCCCTTCGGCCCTCAATCCAGCGGACCTTCCTTCCCGCGGCCTGCTGCCGGCTCTGCGGCCTCTTCCGCGTCTTCGCCTTCGCCCTCAGACGAGTCGGATCTCCCTTTGGGCCGCCTCCCCGCATCGG',
    # POSSIBLE!
    # name of provided enhancer sequence
    'regulator_name':'WPRE',
    
    # REQUIRED!
    # sequence of provided polyA signal
    # name and sequence the user can take from metadata['polya_seq'] (load_metadata())
    'polya_sequence':'CAGACATGATAAGATACATTGATGAGTTTGGACAAACCACAACTAGAATGCAGTGAAAAAAATGCTTTATTTGTGAAATTTGTGATGCTATTGCTTTATTTGTAACCATTATAAGCTGCAATAAACAAGTTAACAACAACAATTGCATTCATTTTATGTTTCAGGTTCAGGGGGAGGTGTGGGAGGTTTTTTAAAGCAAGTAAAACCTCTACAAATGTGGTA',
    # REQUIRED!
    # name of provided polyA signal sequence
    'polya_name':'SV40_late',
    
    
    # REQUIRED if more than one sequence of transcripts!
    # sequences of provided linkers
    # number of linkers_sequences should be equal number of sequences (transcripts) - 1. One linker for each pair of sequences.
    # name and sequence the user can take from metadata['linkers'] (load_metadata())
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    # sequence orientation 5' ---> 3' - sense
    'linkers_sequences':['GGAAGCGGAGAGGGCAGGGGAAGTCTTCTAACATGCGGGGACGTGGAGGAAAATCCCGGCCCC'],
    # REQUIRED if more than one sequence!
    # names of provided linkers
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    'linkers_names':['T2A'],
    
    # POSSIBLE!
    # sequence of provided fluorescent tag
    # name and sequence the user can take from metadata['fluorescent_tag'] (load_metadata())
    # if the user does not need fluorescent tag, provide ''
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_sequence':'ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTAA',
    # POSSIBLE!
    # name of provided fluorescent tag
    # if the user does not need fluorescent tag, provide ''
    'fluorescence_name':'EGFP',
    
    # WARNING! If the user wants to use an additional promoter for the fluorescent tag expression, provide data for fluorescence_promoter_sequence & fluorescence_polya_sequence!
    
    # POSSIBLE!
    # sequence of provided fluorescence promoter
    # name and sequence the user can take from metadata['promoters'] (load_metadata())
    # if the user does not need additional promoter for fluorescent tag, provide ''
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_promoter_sequence':'CTCGACATTGATTATTGACTAGTTATTAATAGTAATCAATTACGGGGTCATTAGTTCATAGCCCATATATGGAGTTCCGCGTTACATAACTTACGGTAAATGGCCCGCCTGGCTGACCGCCCAACGACCCCCGCCCATTGACGTCAATAATGACGTATGTTCCCATAGTAACGCCAATAGGGACTTTCCATTGACGTCAATGGGTGGAGTATTTACGGTAAACTGCCCACTTGGCAGTACATCAAGTGTATCATATGCCAAGTACGCCCCCTATTGACGTCAATGACGGTAAATGGCCCGCCTGGCATTATGCCCAGTACATGACCTTATGGGACTTTCCTACTTGGCAGTACATCTACGTATTAGTCATCGCTATTACCATGGTCGAGGTGAGCCCCACGTTCTGCTTCACTCTCCCCATCTCCCCCCCCTCCCCACCCCCAATTTTGTATTTATTTATTTTTTAATTATTTTGTGCAGCGATGGGGGCGGGGGGGGGGGGGGGGCGCGCGCCAGGCGGGGCGGGGCGGGGCGAGGGGCGGGGCGGGGCGAGGCGGAGAGGTGCGGCGGCAGCCAATCAGAGCGGCGCGCTCCGAAAGTTTCCTTTTATGGCGAGGCGGCGGCGGCGGCGGCCCTATAAAAAGCGAAGCGCGCGGCGGGCGGGAGTCGCTGCGCGCTGCCTTCGCCCCGTGCCCCGCTCCGCCGCCGCCTCGCGCCGCCCGCCCCGGCTCTGACTGACCGCGTTACTCCCACAGGTGAGCGGGCGGGACGGCCCTTCTCCTCCGGGCTGTAATTAGCGCTTGGTTTAATGACGGCTTGTTTCTTTTCTGTGGCTGCGTGAAAGCCTTGAGGGGCTCCGGGAGGGCCCTTTGTGCGGGGGGAGCGGCTCGGGGGGTGCGTGCGTGTGTGTGTGCGTGGGGAGCGCCGCGTGCGGCTCCGCGCTGCCCGGCGGCTGTGAGCGCTGCGGGCGCGGCGCGGGGCTTTGTGCGCTCCGCAGTGTGCGCGAGGGGAGCGCGGCCGGGGGCGGTGCCCCGCGGTGCGGGGGGGGCTGCGAGGGGAACAAAGGCTGCGTGCGGGGTGTGTGCGTGGGGGGGTGAGCAGGGGGTGTGGGCGCGTCGGTCGGGCTGCAACCCCCCCTGCACCCCCCTCCCCGAGTTGCTGAGCACGGCCCGGCTTCGGGTGCGGGGCTCCGTACGGGGCGTGGCGCGGGGCTCGCCGTGCCGGGCGGGGGGTGGCGGCAGGTGGGGGTGCCGGGCGGGGCGGGGCCGCCTCGGGCCGGGGAGGGCTCGGGGGAGGGGCGCGGCGGCCCCCGGAGCGCCGGCGGCTGTCGAGGCGCGGCGAGCCGCAGCCATTGCCTTTTATGGTAATCGTGCGAGAGGGCGCAGGGACTTCCTTTGTCCCAAATCTGTGCGGAGCCGAAATCTGGGAGGCGCCGCCGCACCCCCTCTAGCGGGCGCGGGGCGAAGCGGTGCGGCGCCGGCAGGAAGGAAATGGGCGGGGAGGGCCTTCGTGCGTCGCCGCGCCGCCGTCCCCTTCTCCCTCTCCAGCCTCGGGGCTGTCCGCGGGGGGACGGCTGCCTTCGGGGGGGACGGGGCAGGGCGGGGTTCGGCTTCTGGCGTGTGACCGGCGGCTCTAGAGCCTCTGCTAACCATGTTCATGCCTTCTTCTTTTTCCTACAGCTCCTGGGCAACGTGCTGGTTATTGTGCTGTCTCATCATTTTGGCAAAGAATTG',
    # POSSIBLE!
    # name of provided fluorescence promoter
    # if the user does not need additional promoter for fluorescent tag, provide ''
    'fluorescence_promoter_name':'CAG',
    
    # POSSIBLE!
    # sequence of provided fluorescence polyA signal
    # name and sequence the user can take from metadata['polya_seq'] (load_metadata())
    # if the user does not need additional promoter for fluorescent tag, provide ''
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_polya_sequence':'CTGTGCCTTCTAGTTGCCAGCCATCTGTTGTTTGCCCCTCCCCCGTGCCTTCCTTGACCCTGGAAGGTGCCACTCCCACTGTCCTTTCCTAATAAAATGAGGAAATTGCATCGCATTGTCTGAGTAGGTGTCATTCTATTCTGGGGGGTGGGGTGGGGCAGGACAGCAAGGGGGAGGATTGGGAAGAGAATAGCAGGCATGCTGGGGA',
    # POSSIBLE!
    # name of provided fluorescence polyA signal
    # if the user does not need additional promoter for fluorescent tag, provide ''
    'fluorescence_polya_name':'bGH',
    
    
    # WARNING! If provided sequences for transcripts (> 0) and do not need additional promoter for fluorescent tag, provide fluorescence_linker_sequence
    
    # POSSIBLE!
    # sequence of provided fluorescence tag linker
    # name and sequence the user can take from metadata['linkers'] (load_metadata())
    # if the user has provided additional promoter, so the fluorescence_linker_sequence is not needed, provide ''
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_linker_sequence':'GGAAGCGGAGAGGGCAGGGGAAGTCTTCTAACATGCGGGGACGTGGAGGAAAATCCCGGCCCC',
    # POSSIBLE!
    # name of provided fluorescence tag linker
    # if the user has provided additional promoter, so the fluorescence_linker_sequence is not needed, provide ''
    'fluorescence_linker_name':'T2A',
    
    # REQUIRED!
    # sequence of provided selection marker
    # name and sequence the user can take from metadata['selection_markers'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'selection_marker_sequence':'ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGAAGCCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAA',
    # REQUIRED!
    # name of provided selection marker
    'selection_marker_name':'Ampicillin',
    
    # POSSIBLE!
    # restriction enzymes protection of transcript sequences
    # enzymes the user can take from metadata['restriction'] (load_metadata())
    # if do not need any restriction places protection, provide an empty list []
    'restriction_list':['RsaI', 'MnlI', 'AciI', 'AluI', 'BmrI'],
    
    # REQUIRED!
    # available options (True / False)
    # decision; if the user wants the transcription sequences optimized based on the provided species
    'optimize':True
}




#RNAi

input_dict = {
    
    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_RNAi',
    
    # REQUIRED!
    # avaiable of vector types (ssAAV / scAAV / lentiviral / regular)
    'vector_type':'ssAAV',
      
    # REQUIRED!
    # avaiable of vector functions (expression / rnai)
    # in this case 'vector_function':'rnai'
    'vector_function':'rnai',
    
    # REQUIRED!
    # avaiavle options (human / mouse / both)
    # 'both' - creating vector function adjusted for both species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # REQUIRED!
    # sequence of provided non-coding promoter
    # name and sequence the user can take from metadata['promoters'] (load_metadata())
    # for coding sequences the user should choose the promoter of non-coding genes (metadata['promoters']['type'] == 'non-coding')
    'promoter_ncrna_name':'U6',
    # sequence orientation 5' ---> 3' - sense
    'promoter_ncrna_sequence':'GAGGGCCTATTTCCCATGATTCCTTCATATTTGCATATACGATACAAGGCTGTTAGAGAGATAATTGGAATTAATTTGACTGTAAACACAAAGATATTAGTACAAAATACGTGACGTAGAAAGTAATAATTTCTTGGGTAGTTTGCAGTTTTAAAATTATGTTTTAAAATGGACTATCATATGCTTACCGTAACTTGAAAGTATTTCGATTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC',
    
    
    # POSSIBLE!
    # sequence of custom RNAi, which can be provided by user
    # if provided, then the algorithm of RNAi estimation is off
    # if empt '' the algorithm share the best possible RNAi based on 'rnai_gene_name'
    # sequence orientation 5' ---> 3' - sense
    'rnai_sequence':'',
    
    # REQUIRED!
    # name of the target gene for the RNAi searching algorithm (gene name for Homo sapien or Mus musculus)
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    'rnai_gene_name':'PAX3',
    
    # REQUIRED!
    # sequence of the loop to create the structure of the hairpin of shRNA or siRNA depending on the loop sequence
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    # sequence orientation 5' ---> 3' - sense
    'loop_sequence':'TAGTGAAGCCACAGATGTAC',
    
    # WARNING! If the user wants to add additional CDS sequences to parallel transcript expression with silencing by RNAi in one vector; provide sequences, linkers_sequences, promoter_sequence, etc.
    
    # list of coding sequences (CDS) provided to make expression from the vector
    # the CSD sequences the user can obtain from ...
    # amount of sequences is not restricted as the user must remember that the length of whole vector is limited
    # excide the relevant vector size can decrease vector working
    # if the user wants to not include any sequences only fluorescent_tag, provide ['']
    # sequences orientation 5' ---> 3' - sense
    'sequences':['ATGGCGATGAGCAGCGGCGGCAGTGGTGGCGGCGTCCCGGAGCAGGAGGATTCCGTGCTGTTCCGGCGCGGCACAGGCCAGAGCGATGATTCTGACATTTGGGATGATACAGCACTGATAAAAGCATATGATAAAGCTGTGGCTTCATTTAAGCATGCTCTAAAGAATGGTGACATTTGTGAAACTTCGGGTAAACCAAAAACCACACCTAAAAGAAAACCTGCTAAGAAGAATAAAAGCCAAAAGAAGAATACTGCAGCTTCCTTACAACAGTGGAAAGTTGGGGACAAATGTTCTGCCATTTGGTCAGAAGACGGTTGCATTTACCCAGCTACCATTGCTTCAATTGATTTTAAGAGAGAAACCTGTGTTGTGGTTTACACTGGATATGGAAATAGAGAGGAGCAAAATCTGTCCGATCTACTTTCCCCAATCTGTGAAGTAGCTAATAATATAGAACAAAATGCTCAAGAGAATGAAAATGAAAGCCAAGTTTCAACAGATGAAAGTGAGAACTCCAGGTCTCCTGGAAATAAATCAGATAACATCAAGCCCAAATCTGCTCCATGGAACTCTTTTCTCCCTCCACCACCCCCCATGCCAGGGCCAAGACTGGGACCAGGAAAGCCAGGTCTAAAATTCAATGGCCCACCACCGCCACCGCCACCACCACCACCCCACTTACTATCATGCTGGCTGCCTCCATTTCCTTCTGGACCACCAATAATTCCCCCACCACCTCCCATATGTCCAGATTCTCTTGATGATGCTGATGCTTTGGGAAGTATGTTAATTTCATGGTACATGAGTGGCTATCATACTGGCTATTATATGTTTCCTGAGGCCTCCCTAAAAGCCGAGCAGATGCCAGCACCATGCTTCCTGTAA'],
    # list of names of coding sequences
    # amount of names should be equal with amount of sequences
    # if provided no sequences, provide ['']
    'sequences_names':['SMN1'],
    
    # REQUIRED if more than one sequence of transcripts!
    # sequences of provided linkers
    # number of linkers_sequences should be equal number of sequences (transcripts) - 1. One linker for each pair of sequences.
    # name and sequence the user can take from metadata['linkers'] (load_metadata())
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    'linkers_sequences':[],
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # names of provided linkers
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    'linkers_names':[],
    
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # sequence of provided promoter
    # name and sequence the user can take from metadata['promoters'] (load_metadata())
    # for coding sequences the user should choose the promoter of coding genes (metadata['promoters']['type'] == 'coding')
    # sequence orientation 5' ---> 3' - sense
    'promoter_sequence':'GGGCTGGAAGCTACCTTTGACATCATTTCCTCTGCGAATGCATGTATAATTTCTACAGAACCTATTAGAAAGGATCACCCAGCCTCTGCTTTTGTACAACTTTCCCTTAAAAAACTGCCAATTCCACTGCTGTTTGGCCCAATAGTGAGAACTTTTTCCTGCTGCCTCTTGGTGCTTTTGCCTATGGCCCCTATTCTGCCTGCTGAAGACACTCTTGCCAGCATGGACTTAAACCCCTCCAGCTCTGACAATCCTCTTTCTCTTTTGTTTTACATGAAGGGTCTGGCAGCCAAAGCAATCACTCAAAGTTCAAACCTTATCATTTTTTGCTTTGTTCCTCTTGGCCTTGGTTTTGTACATCAGCTTTGAAAATACCATCCCAGGGTTAATGCTGGGGTTAATTTATAACTAAGAGTGCTCTAGTTTTGCAATACAGGACATGCTATAAAAATGGAAAGAT',
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # name of provided promoter sequence
    'promoter_name':'TBG',
    
    
    # POSSIBLE if transcript sequence occure, if not empty string ''!
    # sequence of provided enhancer
    # name and sequence the user can take from metadata['regulators'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'regulator_sequence':'CGATAATCAACCTCTGGATTACAAAATTTGTGAAAGATTGACTGGTATTCTTAACTATGTTGCTCCTTTTACGCTATGTGGATACGCTGCTTTAATGCCTTTGTATCATGCTATTGCTTCCCGTATGGCTTTCATTTTCTCCTCCTTGTATAAATCCTGGTTGCTGTCTCTTTATGAGGAGTTGTGGCCCGTTGTCAGGCAACGTGGCGTGGTGTGCACTGTGTTTGCTGACGCAACCCCCACTGGTTGGGGCATTGCCACCACCTGTCAGCTCCTTTCCGGGACTTTCGCTTTCCCCCTCCCTATTGCCACGGCGGAACTCATCGCCGCCTGCCTTGCCCGCTGCTGGACAGGGGCTCGGCTGTTGGGCACTGACAATTCCGTGGTGTTGTCGGGGAAGCTGACGTCCTTTCCATGGCTGCTCGCCTGTGTTGCCACCTGGATTCTGCGCGGGACGTCCTTCTGCTACGTCCCTTCGGCCCTCAATCCAGCGGACCTTCCTTCCCGCGGCCTGCTGCCGGCTCTGCGGCCTCTTCCGCGTCTTCGCCTTCGCCCTCAGACGAGTCGGATCTCCCTTTGGGCCGCCTCCCCGCATCGG',
    # POSSIBLE if transcript sequence occure, if not empty string ''!
    # name of provided enhancer sequence
    'regulator_name':'WPRE',
    
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # sequence of provided polyA signal
    # name and sequence the user can take from metadata['polya_seq'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'polya_sequence':'CAGACATGATAAGATACATTGATGAGTTTGGACAAACCACAACTAGAATGCAGTGAAAAAAATGCTTTATTTGTGAAATTTGTGATGCTATTGCTTTATTTGTAACCATTATAAGCTGCAATAAACAAGTTAACAACAACAATTGCATTCATTTTATGTTTCAGGTTCAGGGGGAGGTGTGGGAGGTTTTTTAAAGCAAGTAAAACCTCTACAAATGTGGTA',
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # name of provided polyA singla sequence
    'polya_name':'SV40_late',
    
    # POSSIBLE!
    # sequence of provided fluorescent tag
    # name and sequence the user can take metadata['fluorescent_tag'] (load_metadata())
    # if the user does not need fluorescent tag, provide ''
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_sequence':'ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTAA',
    # POSSIBLE!
    # name of provided fluorescent tag
    # if the user does not need fluorescent tag, provide ''
    'fluorescence_name':'EGFP',
    
    
    # WARNING! If provided sequences for transcripts (> 0) and do not need additional promoter for fluorescent tag, provide fluorescence_linker_sequence
    
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # sequence of provided fluorescence tag linker
    # name and sequence the user can take from metadata['linkers'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'fluorescence_linker_sequence':'GGAAGCGGAGAGGGCAGGGGAAGTCTTCTAACATGCGGGGACGTGGAGGAAAATCCCGGCCCC',
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # name of provided fluorescence tag linker
    'fluorescence_linker_name':'T2A',
    
    
    # REQUIRED!
    # sequence of provided selection marker
    # name and sequence the user can take from from metadata['selection_markers'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'selection_marker_sequence':'ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGAAGCCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAA',
    # REQUIRED!
    # name of provided selection marker
    'selection_marker_name':'Ampicillin',
    
    # POSSIBLE!
    # restriction enzymes protection of transcript sequences
    # enzymes the user can take from metadata['restriction'] (load_metadata())
    # if the user does not need any restriction places protection, provide empty list []
    'restriction_list':['RsaI', 'MnlI', 'AciI', 'AluI', 'BmrI'],
    
       
    # REQUIRED!
    # available options (True / False)
    # decision; if the user wants the transcription sequences optimized based on the provided species
    # if the user has omitted the additional transcript sequences, provide False
    'optimize':True

}  



#transcription - RNAi

input_dict = {
    
    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_invitro_transcription_RNAi',
    
    # REQUIRED!
    # avaiable of vector types (transcription)
    'vector_type':'transcription',
    
    # REQUIRED!
    # avaiable of vector functions (expression / rnai)
    # in this case 'vector_function':'rnai'
    'vector_function':'rnai',
    
    # REQUIRED!
    # avaiavle options (human / mouse / both)
    # 'both' - creating vector function adjusted for both species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # POSSIBLE!
    # sequence of custom RNAi, which can be provided by user
    # if provided, then the algorithm of RNAi estimation is off
    # if empt '' the algorithm share the best possible RNAi based on 'rnai_gene_name'
    # sequence orientation 5' ---> 3' - sense
    'rnai_sequence':'',
    
    # REQUIRED!
    # name of the target gene for the RNAi searching algorithm (gene name for Homo sapien or Mus musculus)
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    'rnai_gene_name':'KIT',
    
    # REQUIRED!
    # sequence of the loop to create the structure of the hairpin of shRNA or siRNA depending on the loop sequence
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    # sequence orientation 5' ---> 3' - sense
    'loop_sequence':'TAGTGAAGCCACAGATGTAC',
    
    # REQUIRED!
    # sequence of provided selection marker
    # name and sequence the user can take from from metadata['selection_markers'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'selection_marker_sequence':'ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGAAGCCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAA',
    # REQUIRED!
    # name of provided selection marker
    'selection_marker_name':'Ampicillin'
}


#transcription - mRNA

input_dict = {
    
    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_invitro_transcription_mRNA',
    
    # REQUIRED!
    # avaiable of vector types (transcription)
    'vector_type':'transcription',
    
    # REQUIRED!
    # avaiable of vector functions (expression / rnai)
    # in this case 'vector_function':'mrna'
    'vector_function':'mrna',
    
    # REQUIRED!
    # avaiavle options (human / mouse / both)
    # 'both' - creating vector function adjusted for both species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # REQUIRED!
    # list of coding sequences (CDS) provided to make expression from the vector
    # the CSD sequences the user can obtain from ...
    # amount of sequences is not restricted as the user must remember that the length of whole vector is limited
    # excide the relevant vector size can decrease vector working
    # sequences orientation 5' ---> 3' - sense
    'sequences':['ATGGCGATGAGCAGCGGCGGCAGTGGTGGCGGCGTCCCGGAGCAGGAGGATTCCGTGCTGTTCCGGCGCGGCACAGGCCAGAGCGATGATTCTGACATTTGGGATGATACAGCACTGATAAAAGCATATGATAAAGCTGTGGCTTCATTTAAGCATGCTCTAAAGAATGGTGACATTTGTGAAACTTCGGGTAAACCAAAAACCACACCTAAAAGAAAACCTGCTAAGAAGAATAAAAGCCAAAAGAAGAATACTGCAGCTTCCTTACAACAGTGGAAAGTTGGGGACAAATGTTCTGCCATTTGGTCAGAAGACGGTTGCATTTACCCAGCTACCATTGCTTCAATTGATTTTAAGAGAGAAACCTGTGTTGTGGTTTACACTGGATATGGAAATAGAGAGGAGCAAAATCTGTCCGATCTACTTTCCCCAATCTGTGAAGTAGCTAATAATATAGAACAAAATGCTCAAGAGAATGAAAATGAAAGCCAAGTTTCAACAGATGAAAGTGAGAACTCCAGGTCTCCTGGAAATAAATCAGATAACATCAAGCCCAAATCTGCTCCATGGAACTCTTTTCTCCCTCCACCACCCCCCATGCCAGGGCCAAGACTGGGACCAGGAAAGCCAGGTCTAAAATTCAATGGCCCACCACCGCCACCGCCACCACCACCACCCCACTTACTATCATGCTGGCTGCCTCCATTTCCTTCTGGACCACCAATAATTCCCCCACCACCTCCCATATGTCCAGATTCTCTTGATGATGCTGATGCTTTGGGAAGTATGTTAATTTCATGGTACATGAGTGGCTATCATACTGGCTATTATATGTTTCCTGAGGCCTCCCTAAAAGCCGAGCAGATGCCAGCACCATGCTTCCTGTAA'],
    # REQUIRED!
    # list of names of coding sequences
    # amount of names should be equal with amount of sequences
    # if provided no sequences, provide ['']
    'sequences_names':['SMN1'],
    
    # REQUIRED if more than one sequence of transcripts!
    # sequences of provided linkers
    # number of linkers_sequences should be equal number of sequences (transcripts) - 1. One linker for each pair of sequences.
    # name and sequence the user can take from metadata['linkers'] (load_metadata())
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    # sequence orientation 5' ---> 3' - sense
    'linkers_sequences':[],
    # REQUIRED if transcript sequence occure, if not empty string ''!
    # names of provided linkers
    # if the number of transcript sequences is equal 1 then provide empty list []
    # if the user wants to not provide any linkers between the transcript sequences, provide an empty string '' for each pair of transcripts where the user wants to avoid linker; empty strings '' provide inside the list ['']
    'linkers_names':[],
    
    # REQUIRED!
    # sequence of provided 5`UTR
    # name and sequence the user can take from from metadata['utr5'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'utr5_sequence':'GGGCTGGAAGCTACCTTTGACATCATTTCCTCTGCGAATGCATGTATAATTTCTACAGAACCTATTAGAAAGGATCACCCAGCCTCTGCTTTTGTACAACTTTCCCTTAAAAAACTGCCAATTCCACTGCTGTTTGGCCCAATAGTGAGAACTTTTTCCTGCTGCCTCTTGGTGCTTTTGCCTATGGCCCCTATTCTGCCTGCTGAAGACACTCTTGCCAGCATGGACTTAAACCCCTCCAGCTCTGACAATCCTCTTTCTCTTTTGTTTTACATGAAGGGTCTGGCAGCCAAAGCAATCACTCAAAGTTCAAACCTTATCATTTTTTGCTTTGTTCCTCTTGGCCTTGGTTTTGTACATCAGCTTTGAAAATACCATCCCAGGGTTAATGCTGGGGTTAATTTATAACTAAGAGTGCTCTAGTTTTGCAATACAGGACATGCTATAAAAATGGAAAGAT',
    # REQUIRED!
    # name of provided 5`UTR
    'utr5_name':'TBG',
    
    # REQUIRED!
    # sequence of provided 3`UTR
    # name and sequence the user can take from from metadata['utr3'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'utr3_sequence':'CAGACATGATAAGATACATTGATGAGTTTGGACAAACCACAACTAGAATGCAGTGAAAAAAATGCTTTATTTGTGAAATTTGTGATGCTATTGCTTTATTTGTAACCATTATAAGCTGCAATAAACAAGTTAACAACAACAATTGCATTCATTTTATGTTTCAGGTTCAGGGGGAGGTGTGGGAGGTTTTTTAAAGCAAGTAAAACCTCTACAAATGTGGTA',
    # REQUIRED!
    # name of provided 3`UTR
    'utr3_name':'SV40_late',
    
    # REQUIRED!
    # number (integer) of A repeat in the polyA tail
    'polya_tail_x':50,
    
    # REQUIRED!
    # sequence of provided selection marker
    # name and sequence the user can take from from metadata['selection_markers'] (load_metadata())
    # sequence orientation 5' ---> 3' - sense
    'selection_marker_sequence':'ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGAAGCCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAA',
    # REQUIRED!
    # name of provided selection marker
    'selection_marker_name':'Ampicillin',
    
    # POSSIBLE!
    # restriction enzymes protection of transcript sequences
    # enzymes the user can take from metadata['restriction'] (load_metadata())
    # if the user does not need any restriction places protection, provide empty list []
    'restriction_list':['RsaI', 'MnlI', 'AciI', 'AluI', 'BmrI'],
    
    # REQUIRED!
    # available options (True / False)
    # decision; if the user wants the transcription sequences optimized based on the provided species
    'optimize':True

}


#de novo - mRNA

input_dict = {

    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_mRNA',
    
    # REQUIRED!
    # avaiable options (human / mouse / rat / both (mouse + human) / both2 (rat + human) / multi (mouse + rat + human))
    # 'both / both2 / multi' - creating vector function adjusted for all species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # REQUIRED!
    # string of coding sequence (CDS) provided to optimize sequence
    # sequences orientation 5' ---> 3' - sense
    'sequence':'ATGTTAACTAGTGGACTTGTAGTAAGCAACATGTTCTCCTATCATCTCGCAGCCTTGGGACTCATGCCGTCATTCCAGATGGAAGGGCGAGGTCGAGTTAATCAGCTAGGAGGTGTTTTCATTAATGGACGGCCACTGCCCAACCATATACGACTGAAGATTGTCGAGCTAGCGGCCCAGGGCGTCCGTCCGTGCGTCATCAGTAGACAGCTGCGGGTGTCACATGGCTGTGTCAGTAAAATACTCCAACGATATCAAGAAACCGGAAGTATCCGACCTGGGGTTATTGGCGGAAGTAAACCAAGGGTCGCAACTCCGGAAGTTGAGAAAAAGATAGAACAATACAAAAAAGATAATCCGGGAATTTTCAGTTGGGAGATTCGGGATCGGCTGCTGAAGGAGGGGATTTGTGACCGCAGCACCGTGCCAAGTGTGAGCTCCATCAGTCGAGTATTACGGAGCAGGTTCCAGAAATGTGATTCTGATGACAATGACAATGACAATGACAATGAGGACGACGATGGCGATGACGGCAGTAACAGTAGTGTGGCAGACAGGTCTGTTAACTTCTCTGTCAGCGGTCTGCTGTCCGACAATAAAAGCGACAAAAGCGACAACGATTCCGATTGTGAATCAGAGCCGGGGCTATCTGTAAAACGGAAGCAACGCCGCAGTCGAACTACTTTCACCGCGGAGCAGTTGGAGGAACTGGAAAGAGCCTTTGAACGAACTCACTATCCGGATATATATACGCGAGAGGAATTAGCACAAAGAACAAAGCTAACCGAGGCAAGAGTCCAAGTATGGTTTAGTAACCGAAGAGCGAGATGGCGGAAACAGATGGGTAGCAATCAGCTGACAGCCTTGAACAGTATATTACAAGTGCCACAGGGTATGGGAACGCCCTCTTATATGCTGCACGAGCCTGGGTATCCACTCTCACATAATGCAGACAATCTTTGGCATAGATCGTCTATGGCCCAGTCATTACAGTCATTTGGTCAGACAATAAAACCAGAGAATTCCTACGCCGGTCTTATGGAAAACTATTTATCTCATTCATCACAGCTTCATGGTCTTCCTACACATAGTTCATCCGATCCCCTCTCATCCACTTGGTCATCTCCCGTGTCCACTTCCGTTCCTGCGCTAGGATACACGCCATCTAGTGGCCATTACCATCATTACTCTGATGTCACCAAAAGTACTCTTCATTCATATAACGCTCATATTCCTTCAGTCACAAACATGGAGAGATGTTCAGTTGATGACAGTTTGGTTGCTTTACGTATGAAGTCACGTGAGCATTCCGCCGCTCTCAGTTTGATGCAGGTGGCAGACAACAAAATGGCTACCTCATTTTGA',
    
    # REQUIRED!
    # name of coding sequence
    'sequence_name':'SMN1',
    
    # OPTIONAL!
    # restriction enzymes protection of transcript sequence
    # if the user does not need any restriction places protection, provide empty list []
    'restriction_list':['RsaI', 'MnlI', 'AciI', 'AluI', 'BmrI'],
    
    # REQUIRED!
    # available options (True / False)
    # decision; if the user wants the transcription sequence optimized based on the provided species
    'optimize':True,
    
    # REQUIRED; if optimize == True!
    # user-defined percent of GC% content in predicted/optimized sequence
    'transcript_GC':58,
    
    # REQUIRED; if optimize == True!
    # user-defined maximum number of consecutive repeats of a single nucleotide (A, C, T(U), G) in the predicted/optimized sequence, eg. AAAAAA
    'poly_len':7
    
}


#de novo - siRNA

input_dict = {
    
    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_siRNA',
    
    # REQUIRED!
    # avaiable options (human / mouse / rat / both (mouse + human) / both2 (rat + human) / multi (mouse + rat + human))
    # 'both / both2 / multi' - creating vector function adjusted for all species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # REQUIRED!
    # type of RNAi (defined by user)
    # avaiable options 'sh' - for shRNA and 'sirna' for siRNA
    'rnai_type':'sirna',
    
    # OPTIONAL!
    # sequence of custom RNAi, which can be provided by user
    # if provided, then the algorithm of RNAi estimation is off
    # if empt '' the algorithm share the best possible RNAi based on 'rnai_gene_name'
    # sequence orientation 5' ---> 3' - sense
    'rnai_sequence':'',
    
    # REQUIRED; if rnai_sequence is empty!
    # length of RNAi (defined by user)
    # recomended range: 20–25
    'rnai_length':20,
    
    # OPTIONAL; if rnai_sequence is empty!
    # overhang sequence of RNAi sequence 3' end (defined by user)
    # recomended 'UU'
    'overhang_3_prime':'UU',
    
    # REQUIRED!
    # name of the target gene for the RNAi searching algorithm (gene name for Homo sapien / Mus musculus / Rattus norvegicus)
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    'rnai_gene_name':'KIT',
    
    # REQUIRED, if rnai_type = 'sh'!
    # sequence of the loop to create the structure of the hairpin of shRNA 
    # sequence orientation 5' ---> 3' - sense
    'loop_sequence':''
}


#de novo - shRNA

input_dict = {

    # REQUIRED!
    # name of current project (defined by user)
    'project_name':'test_shRNA',
    
    # REQUIRED!
    # avaiable options (human / mouse / rat / both (mouse + human) / both2 (rat + human) / multi (mouse + rat + human))
    # 'both / both2 / multi' - creating vector function adjusted for all species taking into consideration most adjustments for Homo sapiens
    'species':'human',
    
    # REQUIRED!
    # type of RNAi (defined by user)
    # avaiable options 'sh' - for shRNA and 'sirna' for siRNA
    'rnai_type':'sh',
    
    # OPTIONAL!
    # sequence of custom RNAi, which can be provided by user
    # if provided, then the algorithm of RNAi estimation is off
    # if empt '' the algorithm share the best possible RNAi based on 'rnai_gene_name'
    # sequence orientation 5' ---> 3' - sense
    'rnai_sequence':'',
    
    # REQUIRED; if rnai_sequence is empty!
    # length of RNAi (defined by user)
    # recomended range: 20–25
    'rnai_length':20,
    
    # OPTIONAL; if rnai_sequence is empty!
    # overhang sequence of RNAi sequence 3' end (defined by user)
    # recomended 'UU'
    'overhang_3_prime':'UU',
    
    # REQUIRED!
    # name of the target gene for the RNAi searching algorithm (gene name for Homo sapien / Mus musculus / Rattus norvegicus)
    # algorithm is working when the rnai_sequence is empty ''
    # if the user defines 'rnai_sequence' this 'rnai_gene_name' is just a name for a user-supplied sequence
    'rnai_gene_name':'KIT',
    
    # REQUIRED, if rnai_type = 'sh'!
    # sequence of the loop to create the structure of the hairpin of shRNA 
    # sequence orientation 5' ---> 3' - sense
    'loop_sequence':'TAGTGAAGCCACAGATGTAC'
}



# > example FASTA for vector plot <

# # test_expression_ssAAV_expression_8717nc

# >5`ITR_start:1_stop:130_length:130 visible=True
# CTGCGCGCTCGCTCGCTCACTGAGGCCGCCCGGGCAAAGCCCGGGCGTCGGGCGACCTTTGGTCGCCCGGCCTCAGTGAGCGAGCGAGCGCGCAGAGAGGGAGTGGCCAACTCCATCACTAGGGGTTCCT
# >backbone_element_start:131_stop:157_length:27 visible=False
# TCTAGACAACTTTGTATAGAAAAGTTG
# >Promoter:TBG_start:158_stop:617_length:460 visible=True
# GGGCTGGAAGCTACCTTTGACATCATTTCCTCTGCGAATGCATGTATAATTTCTACAGAACCTATTAGAAAGGATCACCCAGCCTCTGCTTTTGTACAACTTTCCCTTAAAAAACTGCCAATTCCACTGCTGTTTGGCCCAATAGTGAGAACTTTTTCCTGCTGCCTCTTGGTGCTTTTGCCTATGGCCCCTATTCTGCCTGCTGAAGACACTCTTGCCAGCATGGACTTAAACCCCTCCAGCTCTGACAATCCTCTTTCTCTTTTGTTTTACATGAAGGGTCTGGCAGCCAAAGCAATCACTCAAAGTTCAAACCTTATCATTTTTTGCTTTGTTCCTCTTGGCCTTGGTTTTGTACATCAGCTTTGAAAATACCATCCCAGGGTTAATGCTGGGGTTAATTTATAACTAAGAGTGCTCTAGTTTTGCAATACAGGACATGCTATAAAAATGGAAAGAT
# >backbone_element_start:618_stop:641_length:24 visible=False
# CAAGTTTGTACAAAAAAGCAGGCT
# >Kozak_sequence_start:642_stop:647_length:6 visible=True
# GCCACC
# >SEQ1:SMN1_start:648_stop:1532_length:885 visible=True
# ATGGCTATGTCTAGCGGAGGCTCTGGAGGAGGAGTTCCTGAACAGGAGGACTCTGTGCTGTTCCGGAGGGGCACAGGACAAAGCGATGACAGCGACATCTGGGACGACACAGCTCTGATTAAGGCCTACGACAAGGCCGTGGCCAGCTTCAAGCACGCCCTGAAGAACGGCGACATCTGCGAGACCAGCGGAAAGCCTAAAACCACCCCTAAGAGAAAGCCTGCTAAAAAGAACAAGAGCCAGAAGAAGAACACCGCTGCCAGCCTGCAGCAGTGGAAGGTGGGCGACAAGTGCAGCGCCATTTGGAGCGAGGACGGATGTATCTACCCTGCCACAATCGCCAGCATCGACTTCAAGCGGGAGACCTGCGTGGTGGTGTATACCGGCTACGGCAACAGGGAAGAGCAGAACCTGAGCGACCTGCTGAGCCCTATTTGCGAGGTGGCCAATAACATCGAGCAGAACGCCCAGGAGAACGAGAACGAGAGCCAGGTGAGCACCGACGAGAGCGAGAACAGCCGGAGCCCCGGCAATAAGAGCGACAACATCAAGCCCAAGAGCGCCCCCTGGAACTCTTTCCTGCCCCCCCCCCCCCCCATGCCTGGACCTAGATTGGGACCTGGAAAACCTGGACTGAAATTCAACGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCATTTGCTGTCTTGTTGGCTGCCCCCCTTCCCTTCTGGACCCCCCATTATCCCCCCCCCCCCCCCCATCTGTCCTGATTCTCTGGACGACGCCGATGCTTTGGGCTCTATGCTGATCTCTTGGTATATGAGCGGCTACCACACCGGCTACTACATGTTCCCCGAGGCCAGCCTGAAGGCCGAGCAGATGCCCGCTCCTTGTTTTCTG
# >SEQ2:SMN2_start:1533_stop:2420_length:888 visible=True
# ATGGCTATGTCTAGCGGAGGCTCTGGAGGAGGAGTTCCTGAACAGGAGGACTCTGTGCTGTTCCGGAGGGGCACAGGACAAAGCGATGACAGCGACATCTGGGACGACACAGCTCTGATTAAGGCCTACGACAAGGCCGTGGCCAGCTTCAAGCACGCCCTGAAGAACGGCGACATCTGCGAGACCAGCGGAAAGCCTAAAACCACCCCTAAGAGAAAGCCTGCTAAAAAGAACAAGAGCCAGAAGAAGAACACCGCTGCCAGCCTGCAGCAGTGGAAGGTGGGCGACAAGTGCAGCGCCATTTGGAGCGAGGACGGATGTATCTACCCTGCCACAATCGCCAGCATCGACTTCAAGCGGGAGACCTGCGTGGTGGTGTATACCGGCTACGGCAACAGGGAAGAGCAGAACCTGAGCGACCTGCTGAGCCCTATTTGCGAGGTGGCCAATAACATCGAGCAGAACGCCCAGGAGAACGAGAACGAGAGCCAGGTGAGCACCGACGAGAGCGAGAACAGCCGGAGCCCCGGCAATAAGAGCGACAACATCAAGCCCAAGAGCGCCCCCTGGAACTCTTTCCTGCCCCCCCCCCCCCCCATGCCTGGACCTAGATTGGGACCTGGAAAACCTGGACTGAAATTCAACGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCATTTGCTGTCTTGTTGGCTGCCCCCCTTCCCTTCTGGACCCCCCATTATCCCCCCCCCCCCCCCCATCTGTCCTGATTCTCTGGACGACGCCGATGCTTTGGGCTCTATGCTGATCTCTTGGTATATGAGCGGCTACCACACCGGCTACTACATGTTCCCCGAGGCCAGCCTGAAGGCCGAGCAGATGCCCGCTCCTTGTTTTCTGTGA
# >PolyA_signal:SV40_late_start:2421_stop:2642_length:222 visible=True
# CAGACATGATAAGATACATTGATGAGTTTGGACAAACCACAACTAGAATGCAGTGAAAAAAATGCTTTATTTGTGAAATTTGTGATGCTATTGCTTTATTTGTAACCATTATAAGCTGCAATAAACAAGTTAACAACAACAATTGCATTCATTTTATGTTTCAGGTTCAGGGGGAGGTGTGGGAGGTTTTTTAAAGCAAGTAAAACCTCTACAAATGTGGTA
# >2nd_promoter:CAG_start:2643_stop:4375_length:1733 visible=True
# CTCGACATTGATTATTGACTAGTTATTAATAGTAATCAATTACGGGGTCATTAGTTCATAGCCCATATATGGAGTTCCGCGTTACATAACTTACGGTAAATGGCCCGCCTGGCTGACCGCCCAACGACCCCCGCCCATTGACGTCAATAATGACGTATGTTCCCATAGTAACGCCAATAGGGACTTTCCATTGACGTCAATGGGTGGAGTATTTACGGTAAACTGCCCACTTGGCAGTACATCAAGTGTATCATATGCCAAGTACGCCCCCTATTGACGTCAATGACGGTAAATGGCCCGCCTGGCATTATGCCCAGTACATGACCTTATGGGACTTTCCTACTTGGCAGTACATCTACGTATTAGTCATCGCTATTACCATGGTCGAGGTGAGCCCCACGTTCTGCTTCACTCTCCCCATCTCCCCCCCCTCCCCACCCCCAATTTTGTATTTATTTATTTTTTAATTATTTTGTGCAGCGATGGGGGCGGGGGGGGGGGGGGGGCGCGCGCCAGGCGGGGCGGGGCGGGGCGAGGGGCGGGGCGGGGCGAGGCGGAGAGGTGCGGCGGCAGCCAATCAGAGCGGCGCGCTCCGAAAGTTTCCTTTTATGGCGAGGCGGCGGCGGCGGCGGCCCTATAAAAAGCGAAGCGCGCGGCGGGCGGGAGTCGCTGCGCGCTGCCTTCGCCCCGTGCCCCGCTCCGCCGCCGCCTCGCGCCGCCCGCCCCGGCTCTGACTGACCGCGTTACTCCCACAGGTGAGCGGGCGGGACGGCCCTTCTCCTCCGGGCTGTAATTAGCGCTTGGTTTAATGACGGCTTGTTTCTTTTCTGTGGCTGCGTGAAAGCCTTGAGGGGCTCCGGGAGGGCCCTTTGTGCGGGGGGAGCGGCTCGGGGGGTGCGTGCGTGTGTGTGTGCGTGGGGAGCGCCGCGTGCGGCTCCGCGCTGCCCGGCGGCTGTGAGCGCTGCGGGCGCGGCGCGGGGCTTTGTGCGCTCCGCAGTGTGCGCGAGGGGAGCGCGGCCGGGGGCGGTGCCCCGCGGTGCGGGGGGGGCTGCGAGGGGAACAAAGGCTGCGTGCGGGGTGTGTGCGTGGGGGGGTGAGCAGGGGGTGTGGGCGCGTCGGTCGGGCTGCAACCCCCCCTGCACCCCCCTCCCCGAGTTGCTGAGCACGGCCCGGCTTCGGGTGCGGGGCTCCGTACGGGGCGTGGCGCGGGGCTCGCCGTGCCGGGCGGGGGGTGGCGGCAGGTGGGGGTGCCGGGCGGGGCGGGGCCGCCTCGGGCCGGGGAGGGCTCGGGGGAGGGGCGCGGCGGCCCCCGGAGCGCCGGCGGCTGTCGAGGCGCGGCGAGCCGCAGCCATTGCCTTTTATGGTAATCGTGCGAGAGGGCGCAGGGACTTCCTTTGTCCCAAATCTGTGCGGAGCCGAAATCTGGGAGGCGCCGCCGCACCCCCTCTAGCGGGCGCGGGGCGAAGCGGTGCGGCGCCGGCAGGAAGGAAATGGGCGGGGAGGGCCTTCGTGCGTCGCCGCGCCGCCGTCCCCTTCTCCCTCTCCAGCCTCGGGGCTGTCCGCGGGGGGACGGCTGCCTTCGGGGGGGACGGGGCAGGGCGGGGTTCGGCTTCTGGCGTGTGACCGGCGGCTCTAGAGCCTCTGCTAACCATGTTCATGCCTTCTTCTTTTTCCTACAGCTCCTGGGCAACGTGCTGGTTATTGTGCTGTCTCATCATTTTGGCAAAGAATTG
# >Fluorescent_tag:EGFP_start:4376_stop:5095_length:720 visible=True
# ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAGTAA
# >backbone_element_start:5096_stop:5125_length:30 visible=False
# ACCCAGCTTTCTTGTACAAAGTGGGAATTC
# >Enhancer:WPRE_start:5126_stop:5723_length:598 visible=True
# CGATAATCAACCTCTGGATTACAAAATTTGTGAAAGATTGACTGGTATTCTTAACTATGTTGCTCCTTTTACGCTATGTGGATACGCTGCTTTAATGCCTTTGTATCATGCTATTGCTTCCCGTATGGCTTTCATTTTCTCCTCCTTGTATAAATCCTGGTTGCTGTCTCTTTATGAGGAGTTGTGGCCCGTTGTCAGGCAACGTGGCGTGGTGTGCACTGTGTTTGCTGACGCAACCCCCACTGGTTGGGGCATTGCCACCACCTGTCAGCTCCTTTCCGGGACTTTCGCTTTCCCCCTCCCTATTGCCACGGCGGAACTCATCGCCGCCTGCCTTGCCCGCTGCTGGACAGGGGCTCGGCTGTTGGGCACTGACAATTCCGTGGTGTTGTCGGGGAAGCTGACGTCCTTTCCATGGCTGCTCGCCTGTGTTGCCACCTGGATTCTGCGCGGGACGTCCTTCTGCTACGTCCCTTCGGCCCTCAATCCAGCGGACCTTCCTTCCCGCGGCCTGCTGCCGGCTCTGCGGCCTCTTCCGCGTCTTCGCCTTCGCCCTCAGACGAGTCGGATCTCCCTTTGGGCCGCCTCCCCGCATCGG
# >backbone_element_start:5724_stop:5753_length:30 visible=False
# GAATTCCTAGAGCTCGCTGATCAGCCTCGA
# >2nd_polyA_signal:bGH_start:5754_stop:5961_length:208 visible=True
# CTGTGCCTTCTAGTTGCCAGCCATCTGTTGTTTGCCCCTCCCCCGTGCCTTCCTTGACCCTGGAAGGTGCCACTCCCACTGTCCTTTCCTAATAAAATGAGGAAATTGCATCGCATTGTCTGAGTAGGTGTCATTCTATTCTGGGGGGTGGGGTGGGGCAGGACAGCAAGGGGGAGGATTGGGAAGAGAATAGCAGGCATGCTGGGGA
# >backbone_element_start:5962_stop:5968_length:7 visible=False
# GGGCCGC
# >3`ITR_start:5969_stop:6098_length:130 visible=True
# CTGCGCGCTCGCTCGCTCACTGAGGCCGCCCGGGCAAAGCCCGGGCGTCGGGCGACCTTTGGTCGCCCGGCCTCAGTGAGCGAGCGAGCGCGCAGAGAGGGAGTGGCCAACTCCATCACTAGGGGTTCCT
# >backbone_element_start:6099_stop:7025_length:927 visible=False
# CTGCCTGCAGGGGCGCCTGATGCGGTATTTTCTCCTTACGCATCTGTGCGGTATTTCACACCGCATACGTCAAAGCAACCATAGTACGCGCCCTGTAGCGGCGCATTAAGCGCGGCGGGGGTGGTGGTTACGCGCAGCGTGACCGCTACACTTGCCAGCGCCTTAGCGCCCGCTCCTTTCGCTTTCTTCCCTTCCTTTCTCGCCACGTTCGCCGGCTTTCCCCGTCAAGCTCTAAATCGGGGGCTCCCTTTAGGGTTCCGATTTAGTGCTTTACGGCACCTCGACCCCAAAAAACTTGATTTGGGTGATGGTTCACGTAGTGGGCCATCGCCCTGATAGACGGTTTTTCGCCCTTTGACGTTGGAGTCCACGTTCTTTAATAGTGGACTCTTGTTCCAAACTGGAACAACACTCAACTCTATCTCGGGCTATTCTTTTGATTTATAAGGGATTTTGCCGATTTCGGTCTATTGGTTAAAAAATGAGCTGATTTAACAAAAATTTAACGCGAATTTTAACAAAATATTAACGTTTACAATTTTATGGTGCACTCTCAGTACAATCTGCTCTGATGCCGCATAGTTAAGCCAGCCCCGACACCCGCCAACACCCGCTGACGCGCCCTGACGGGCTTGTCTGCTCCCGGCATCCGCTTACAGACAAGCTGTGACCGTCTCCGGGAGCTGCATGTGTCAGAGGTTTTCACCGTCATCACCGAAACGCGCGAGACGAAAGGGCCTCGTGATACGCCTATTTTTATAGGTTAATGTCATGATAATAATGGTTTCTTAGACGTCAGGTGGCACTTTTCGGGGAAATGTGCGCGGAACCCCTATTTGTTTATTTTTCTAAATACATTCAAATATGTATCCGCTCATGAGACAATAACCCTGATAAATGCTTCAATAATATTGAAAAAGGAAGAGT
# >Resistance:Ampicillin_start:7026_stop:7886_length:861 visible=True
# ATGAGTATTCAACATTTCCGTGTCGCCCTTATTCCCTTTTTTGCGGCATTTTGCCTTCCTGTTTTTGCTCACCCAGAAACGCTGGTGAAAGTAAAAGATGCTGAAGATCAGTTGGGTGCACGAGTGGGTTACATCGAACTGGATCTCAACAGCGGTAAGATCCTTGAGAGTTTTCGCCCCGAAGAACGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGCGCGGTATTATCCCGTATTGACGCCGGGCAAGAGCAACTCGGTCGCCGCATACACTATTCTCAGAATGACTTGGTTGAGTACTCACCAGTCACAGAAAAGCATCTTACGGATGGCATGACAGTAAGAGAATTATGCAGTGCTGCCATAACCATGAGTGATAACACTGCGGCCAACTTACTTCTGACAACGATCGGAGGACCGAAGGAGCTAACCGCTTTTTTGCACAACATGGGGGATCATGTAACTCGCCTTGATCGTTGGGAACCGGAGCTGAATGAAGCCATACCAAACGACGAGCGTGACACCACGATGCCTGTAGCAATGGCAACAACGTTGCGCAAACTATTAACTGGCGAACTACTTACTCTAGCTTCCCGGCAACAATTAATAGACTGGATGGAGGCGGATAAAGTTGCAGGACCACTTCTGCGCTCGGCCCTTCCGGCTGGCTGGTTTATTGCTGATAAATCTGGAGCCGGTGAGCGTGGAAGCCGCGGTATCATTGCAGCACTGGGGCCAGATGGTAAGCCCTCCCGTATCGTAGTTATCTACACGACGGGGAGTCAGGCAACTATGGATGAACGAAATAGACAGATCGCTGAGATAGGTGCCTCACTGATTAAGCATTGGTAA
# >backbone_element_start:7887_stop:8056_length:170 visible=False
# CTGTCAGACCAAGTTTACTCATATATACTTTAGATTGATTTAAAACTTCATTTTTAATTTAAAAGGATCTAGGTGAAGATCCTTTTTGATAATCTCATGACCAAAATCCCTTAACGTGAGTTTTCGTTCCACTGAGCGTCAGACCCCGTAGAAAAGATCAAAGGATCTTC
# >pUC_ori_start:8057_stop:8645_length:589 visible=True
# TTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAACAAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTTCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCGTCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAA
# >backbone_element_start:8646_stop:8717_length:72 visible=False
# AACGCCAGCAACGCGGCCTTTTTACGGTTCCTGGCCTTTTGCTGGCCTTTTGCTCACATGTCCTGCAGGCAG



# > example GeneBank for vector notation <

# LOCUS       viral_vector   8717 bp    DNA     circular     11-JUL-2025
# DEFINITION   Synthetic viral plasmid vector.
# FEATURES             Location/Qualifiers
#      misc_feature    1..130
#                      /note="5`ITR"
#      misc_feature    158..617
#                      /note="Promoter:TBG"
#      misc_feature    642..647
#                      /note="Kozak_sequence"
#      misc_feature    648..1532
#                      /note="SEQ1:SMN1"
#      misc_feature    1533..2420
#                      /note="SEQ2:SMN2"
#      misc_feature    2421..2642
#                      /note="PolyA_signal:SV40"
#      misc_feature    2643..4375
#                      /note="2nd_promoter:CAG"
#      misc_feature    4376..5095
#                      /note="Fluorescent_tag:EGFP"
#      misc_feature    5126..5723
#                      /note="Enhancer:WPRE"
#      misc_feature    5754..5961
#                      /note="2nd_polyA_signal:bGH"
#      misc_feature    5969..6098
#                      /note="3`ITR"
#      misc_feature    7026..7886
#                      /note="Resistance:Ampicillin"
#      misc_feature    8057..8645
#                      /note="pUC_ori"

# ORIGIN
#         1 ctgcgcgctc gctcgctcac tgaggccgcc cgggcaaagc ccgggcgtcg ggcgaccttt
#        61 ggtcgcccgg cctcagtgag cgagcgagcg cgcagagagg gagtggccaa ctccatcact
#       121 aggggttcct tctagacaac tttgtataga aaagttgggg ctggaagcta cctttgacat
#       181 catttcctct gcgaatgcat gtataatttc tacagaacct attagaaagg atcacccagc
#       241 ctctgctttt gtacaacttt cccttaaaaa actgccaatt ccactgctgt ttggcccaat
#       301 agtgagaact ttttcctgct gcctcttggt gcttttgcct atggccccta ttctgcctgc
#       361 tgaagacact cttgccagca tggacttaaa cccctccagc tctgacaatc ctctttctct
#       421 tttgttttac atgaagggtc tggcagccaa agcaatcact caaagttcaa accttatcat
#       481 tttttgcttt gttcctcttg gccttggttt tgtacatcag ctttgaaaat accatcccag
#       541 ggttaatgct ggggttaatt tataactaag agtgctctag ttttgcaata caggacatgc
#       601 tataaaaatg gaaagatcaa gtttgtacaa aaaagcaggc tgccaccatg gctatgtcta
#       661 gcggaggctc tggaggagga gttcctgaac aggaggactc tgtgctgttc cggaggggca
#       721 caggacaaag cgatgacagc gacatctggg acgacacagc tctgattaag gcctacgaca
#       781 aggccgtggc cagcttcaag cacgccctga agaacggcga catctgcgag accagcggaa
#       841 agcctaaaac cacccctaag agaaagcctg ctaaaaagaa caagagccag aagaagaaca
#       901 ccgctgccag cctgcagcag tggaaggtgg gcgacaagtg cagcgccatt tggagcgagg
#       961 acggatgtat ctaccctgcc acaatcgcca gcatcgactt caagcgggag acctgcgtgg
#      1021 tggtgtatac cggctacggc aacagggaag agcagaacct gagcgacctg ctgagcccta
#      1081 tttgcgaggt ggccaataac atcgagcaga acgcccagga gaacgagaac gagagccagg
#      1141 tgagcaccga cgagagcgag aacagccgga gccccggcaa taagagcgac aacatcaagc
#      1201 ccaagagcgc cccctggaac tctttcctgc cccccccccc ccccatgcct ggacctagat
#      1261 tgggacctgg aaaacctgga ctgaaattca acggcccccc cccccccccc cccccccccc
#      1321 ccccccattt gctgtcttgt tggctgcccc ccttcccttc tggacccccc attatccccc
#      1381 cccccccccc catctgtcct gattctctgg acgacgccga tgctttgggc tctatgctga
#      1441 tctcttggta tatgagcggc taccacaccg gctactacat gttccccgag gccagcctga
#      1501 aggccgagca gatgcccgct ccttgttttc tgatggctat gtctagcgga ggctctggag
#      1561 gaggagttcc tgaacaggag gactctgtgc tgttccggag gggcacagga caaagcgatg
#      1621 acagcgacat ctgggacgac acagctctga ttaaggccta cgacaaggcc gtggccagct
#      1681 tcaagcacgc cctgaagaac ggcgacatct gcgagaccag cggaaagcct aaaaccaccc
#      1741 ctaagagaaa gcctgctaaa aagaacaaga gccagaagaa gaacaccgct gccagcctgc
#      1801 agcagtggaa ggtgggcgac aagtgcagcg ccatttggag cgaggacgga tgtatctacc
#      1861 ctgccacaat cgccagcatc gacttcaagc gggagacctg cgtggtggtg tataccggct
#      1921 acggcaacag ggaagagcag aacctgagcg acctgctgag ccctatttgc gaggtggcca
#      1981 ataacatcga gcagaacgcc caggagaacg agaacgagag ccaggtgagc accgacgaga
#      2041 gcgagaacag ccggagcccc ggcaataaga gcgacaacat caagcccaag agcgccccct
#      2101 ggaactcttt cctgcccccc ccccccccca tgcctggacc tagattggga cctggaaaac
#      2161 ctggactgaa attcaacggc cccccccccc cccccccccc cccccccccc catttgctgt
#      2221 cttgttggct gccccccttc ccttctggac cccccattat cccccccccc ccccccatct
#      2281 gtcctgattc tctggacgac gccgatgctt tgggctctat gctgatctct tggtatatga
#      2341 gcggctacca caccggctac tacatgttcc ccgaggccag cctgaaggcc gagcagatgc
#      2401 ccgctccttg ttttctgtga cagacatgat aagatacatt gatgagtttg gacaaaccac
#      2461 aactagaatg cagtgaaaaa aatgctttat ttgtgaaatt tgtgatgcta ttgctttatt
#      2521 tgtaaccatt ataagctgca ataaacaagt taacaacaac aattgcattc attttatgtt
#      2581 tcaggttcag ggggaggtgt gggaggtttt ttaaagcaag taaaacctct acaaatgtgg
#      2641 tactcgacat tgattattga ctagttatta atagtaatca attacggggt cattagttca
#      2701 tagcccatat atggagttcc gcgttacata acttacggta aatggcccgc ctggctgacc
#      2761 gcccaacgac ccccgcccat tgacgtcaat aatgacgtat gttcccatag taacgccaat
#      2821 agggactttc cattgacgtc aatgggtgga gtatttacgg taaactgccc acttggcagt
#      2881 acatcaagtg tatcatatgc caagtacgcc ccctattgac gtcaatgacg gtaaatggcc
#      2941 cgcctggcat tatgcccagt acatgacctt atgggacttt cctacttggc agtacatcta
#      3001 cgtattagtc atcgctatta ccatggtcga ggtgagcccc acgttctgct tcactctccc
#      3061 catctccccc ccctccccac ccccaatttt gtatttattt attttttaat tattttgtgc
#      3121 agcgatgggg gcgggggggg ggggggggcg cgcgccaggc ggggcggggc ggggcgaggg
#      3181 gcggggcggg gcgaggcgga gaggtgcggc ggcagccaat cagagcggcg cgctccgaaa
#      3241 gtttcctttt atggcgaggc ggcggcggcg gcggccctat aaaaagcgaa gcgcgcggcg
#      3301 ggcgggagtc gctgcgcgct gccttcgccc cgtgccccgc tccgccgccg cctcgcgccg
#      3361 cccgccccgg ctctgactga ccgcgttact cccacaggtg agcgggcggg acggcccttc
#      3421 tcctccgggc tgtaattagc gcttggttta atgacggctt gtttcttttc tgtggctgcg
#      3481 tgaaagcctt gaggggctcc gggagggccc tttgtgcggg gggagcggct cggggggtgc
#      3541 gtgcgtgtgt gtgtgcgtgg ggagcgccgc gtgcggctcc gcgctgcccg gcggctgtga
#      3601 gcgctgcggg cgcggcgcgg ggctttgtgc gctccgcagt gtgcgcgagg ggagcgcggc
#      3661 cgggggcggt gccccgcggt gcgggggggg ctgcgagggg aacaaaggct gcgtgcgggg
#      3721 tgtgtgcgtg ggggggtgag cagggggtgt gggcgcgtcg gtcgggctgc aaccccccct
#      3781 gcacccccct ccccgagttg ctgagcacgg cccggcttcg ggtgcggggc tccgtacggg
#      3841 gcgtggcgcg gggctcgccg tgccgggcgg ggggtggcgg caggtggggg tgccgggcgg
#      3901 ggcggggccg cctcgggccg gggagggctc gggggagggg cgcggcggcc cccggagcgc
#      3961 cggcggctgt cgaggcgcgg cgagccgcag ccattgcctt ttatggtaat cgtgcgagag
#      4021 ggcgcaggga cttcctttgt cccaaatctg tgcggagccg aaatctggga ggcgccgccg
#      4081 caccccctct agcgggcgcg gggcgaagcg gtgcggcgcc ggcaggaagg aaatgggcgg
#      4141 ggagggcctt cgtgcgtcgc cgcgccgccg tccccttctc cctctccagc ctcggggctg
#      4201 tccgcggggg gacggctgcc ttcggggggg acggggcagg gcggggttcg gcttctggcg
#      4261 tgtgaccggc ggctctagag cctctgctaa ccatgttcat gccttcttct ttttcctaca
#      4321 gctcctgggc aacgtgctgg ttattgtgct gtctcatcat tttggcaaag aattgatggt
#      4381 gagcaagggc gaggagctgt tcaccggggt ggtgcccatc ctggtcgagc tggacggcga
#      4441 cgtaaacggc cacaagttca gcgtgtccgg cgagggcgag ggcgatgcca cctacggcaa
#      4501 gctgaccctg aagttcatct gcaccaccgg caagctgccc gtgccctggc ccaccctcgt
#      4561 gaccaccctg acctacggcg tgcagtgctt cagccgctac cccgaccaca tgaagcagca
#      4621 cgacttcttc aagtccgcca tgcccgaagg ctacgtccag gagcgcacca tcttcttcaa
#      4681 ggacgacggc aactacaaga cccgcgccga ggtgaagttc gagggcgaca ccctggtgaa
#      4741 ccgcatcgag ctgaagggca tcgacttcaa ggaggacggc aacatcctgg ggcacaagct
#      4801 ggagtacaac tacaacagcc acaacgtcta tatcatggcc gacaagcaga agaacggcat
#      4861 caaggtgaac ttcaagatcc gccacaacat cgaggacggc agcgtgcagc tcgccgacca
#      4921 ctaccagcag aacaccccca tcggcgacgg ccccgtgctg ctgcccgaca accactacct
#      4981 gagcacccag tccgccctga gcaaagaccc caacgagaag cgcgatcaca tggtcctgct
#      5041 ggagttcgtg accgccgccg ggatcactct cggcatggac gagctgtaca agtaaaccca
#      5101 gctttcttgt acaaagtggg aattccgata atcaacctct ggattacaaa atttgtgaaa
#      5161 gattgactgg tattcttaac tatgttgctc cttttacgct atgtggatac gctgctttaa
#      5221 tgcctttgta tcatgctatt gcttcccgta tggctttcat tttctcctcc ttgtataaat
#      5281 cctggttgct gtctctttat gaggagttgt ggcccgttgt caggcaacgt ggcgtggtgt
#      5341 gcactgtgtt tgctgacgca acccccactg gttggggcat tgccaccacc tgtcagctcc
#      5401 tttccgggac tttcgctttc cccctcccta ttgccacggc ggaactcatc gccgcctgcc
#      5461 ttgcccgctg ctggacaggg gctcggctgt tgggcactga caattccgtg gtgttgtcgg
#      5521 ggaagctgac gtcctttcca tggctgctcg cctgtgttgc cacctggatt ctgcgcggga
#      5581 cgtccttctg ctacgtccct tcggccctca atccagcgga ccttccttcc cgcggcctgc
#      5641 tgccggctct gcggcctctt ccgcgtcttc gccttcgccc tcagacgagt cggatctccc
#      5701 tttgggccgc ctccccgcat cgggaattcc tagagctcgc tgatcagcct cgactgtgcc
#      5761 ttctagttgc cagccatctg ttgtttgccc ctcccccgtg ccttccttga ccctggaagg
#      5821 tgccactccc actgtccttt cctaataaaa tgaggaaatt gcatcgcatt gtctgagtag
#      5881 gtgtcattct attctggggg gtggggtggg gcaggacagc aagggggagg attgggaaga
#      5941 gaatagcagg catgctgggg agggccgcct gcgcgctcgc tcgctcactg aggccgcccg
#      6001 ggcaaagccc gggcgtcggg cgacctttgg tcgcccggcc tcagtgagcg agcgagcgcg
#      6061 cagagaggga gtggccaact ccatcactag gggttcctct gcctgcaggg gcgcctgatg
#      6121 cggtattttc tccttacgca tctgtgcggt atttcacacc gcatacgtca aagcaaccat
#      6181 agtacgcgcc ctgtagcggc gcattaagcg cggcgggggt ggtggttacg cgcagcgtga
#      6241 ccgctacact tgccagcgcc ttagcgcccg ctcctttcgc tttcttccct tcctttctcg
#      6301 ccacgttcgc cggctttccc cgtcaagctc taaatcgggg gctcccttta gggttccgat
#      6361 ttagtgcttt acggcacctc gaccccaaaa aacttgattt gggtgatggt tcacgtagtg
#      6421 ggccatcgcc ctgatagacg gtttttcgcc ctttgacgtt ggagtccacg ttctttaata
#      6481 gtggactctt gttccaaact ggaacaacac tcaactctat ctcgggctat tcttttgatt
#      6541 tataagggat tttgccgatt tcggtctatt ggttaaaaaa tgagctgatt taacaaaaat
#      6601 ttaacgcgaa ttttaacaaa atattaacgt ttacaatttt atggtgcact ctcagtacaa
#      6661 tctgctctga tgccgcatag ttaagccagc cccgacaccc gccaacaccc gctgacgcgc
#      6721 cctgacgggc ttgtctgctc ccggcatccg cttacagaca agctgtgacc gtctccggga
#      6781 gctgcatgtg tcagaggttt tcaccgtcat caccgaaacg cgcgagacga aagggcctcg
#      6841 tgatacgcct atttttatag gttaatgtca tgataataat ggtttcttag acgtcaggtg
#      6901 gcacttttcg gggaaatgtg cgcggaaccc ctatttgttt atttttctaa atacattcaa
#      6961 atatgtatcc gctcatgaga caataaccct gataaatgct tcaataatat tgaaaaagga
#      7021 agagtatgag tattcaacat ttccgtgtcg cccttattcc cttttttgcg gcattttgcc
#      7081 ttcctgtttt tgctcaccca gaaacgctgg tgaaagtaaa agatgctgaa gatcagttgg
#      7141 gtgcacgagt gggttacatc gaactggatc tcaacagcgg taagatcctt gagagttttc
#      7201 gccccgaaga acgttttcca atgatgagca cttttaaagt tctgctatgt ggcgcggtat
#      7261 tatcccgtat tgacgccggg caagagcaac tcggtcgccg catacactat tctcagaatg
#      7321 acttggttga gtactcacca gtcacagaaa agcatcttac ggatggcatg acagtaagag
#      7381 aattatgcag tgctgccata accatgagtg ataacactgc ggccaactta cttctgacaa
#      7441 cgatcggagg accgaaggag ctaaccgctt ttttgcacaa catgggggat catgtaactc
#      7501 gccttgatcg ttgggaaccg gagctgaatg aagccatacc aaacgacgag cgtgacacca
#      7561 cgatgcctgt agcaatggca acaacgttgc gcaaactatt aactggcgaa ctacttactc
#      7621 tagcttcccg gcaacaatta atagactgga tggaggcgga taaagttgca ggaccacttc
#      7681 tgcgctcggc ccttccggct ggctggttta ttgctgataa atctggagcc ggtgagcgtg
#      7741 gaagccgcgg tatcattgca gcactggggc cagatggtaa gccctcccgt atcgtagtta
#      7801 tctacacgac ggggagtcag gcaactatgg atgaacgaaa tagacagatc gctgagatag
#      7861 gtgcctcact gattaagcat tggtaactgt cagaccaagt ttactcatat atactttaga
#      7921 ttgatttaaa acttcatttt taatttaaaa ggatctaggt gaagatcctt tttgataatc
#      7981 tcatgaccaa aatcccttaa cgtgagtttt cgttccactg agcgtcagac cccgtagaaa
#      8041 agatcaaagg atcttcttga gatccttttt ttctgcgcgt aatctgctgc ttgcaaacaa
#      8101 aaaaaccacc gctaccagcg gtggtttgtt tgccggatca agagctacca actctttttc
#      8161 cgaaggtaac tggcttcagc agagcgcaga taccaaatac tgttcttcta gtgtagccgt
#      8221 agttaggcca ccacttcaag aactctgtag caccgcctac atacctcgct ctgctaatcc
#      8281 tgttaccagt ggctgctgcc agtggcgata agtcgtgtct taccgggttg gactcaagac
#      8341 gatagttacc ggataaggcg cagcggtcgg gctgaacggg gggttcgtgc acacagccca
#      8401 gcttggagcg aacgacctac accgaactga gatacctaca gcgtgagcta tgagaaagcg
#      8461 ccacgcttcc cgaagggaga aaggcggaca ggtatccggt aagcggcagg gtcggaacag
#      8521 gagagcgcac gagggagctt ccagggggaa acgcctggta tctttatagt cctgtcgggt
#      8581 ttcgccacct ctgacttgag cgtcgatttt tgtgatgctc gtcagggggg cggagcctat
#      8641 ggaaaaacgc cagcaacgcg gcctttttac ggttcctggc cttttgctgg ccttttgctc
#      8701 acatgtcctg caggcag
# //

