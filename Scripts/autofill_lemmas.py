import re

def autofill_lemmas(conllu_file, output_file):
    with open(conllu_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    
    for line in lines:
        if line.startswith('#') or line.strip() == '':
            updated_lines.append(line)
            continue
        
        columns = line.split('\t')
        if len(columns) > 2 and columns[2] == '_':  # Lemma column is empty ('_')
            columns[2] = columns[1]  # Copy form into lemma
        updated_lines.append('\t'.join(columns))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

# Example usage
autofill_lemmas('amh_att-ud-1300(raw).conllu', 'amh_att-ud-1302(raw).conllu')
