from jbst import seq_tools as st
import RNA
import pandas as pd

data = pd.read_excel('mef.xlsx')

################################################################################
for i in data['sequence_var']:
    print(i)
    
    sequence = st.clear_sequence(data.loc[data['sequence_var'] == i, 'sequence'].values[0])
    
    _, dot = st.predict_structure(sequence, 
                      anty_sequence = '',
                      height=None, 
                      width=None, 
                      dis_alpha = 0.15, 
                      seq_force = 27, 
                      pair_force = 3, 
                      show_plot = True)
    
    energy = RNA.eval_structure_simple(sequence, dot)
    
    data.loc[data['sequence_var'] == i, 'dot'] = dot
    data.loc[data['sequence_var'] == i, 'MEF'] = energy



data.to_excel('full_data.xlsx')


##################################################################################



