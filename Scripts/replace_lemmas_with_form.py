import argparse

def process_conllu(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Preserve original line endings exactly
            stripped = line.rstrip('\n')
            
            if line.startswith('#'):
                outfile.write(line)  # Write comments with original newline
            elif not stripped.strip():  # Empty line (preserve original newline(s))
                outfile.write(line)  # Keep original line ending
            else:
                parts = stripped.split('\t')
                if len(parts) == 10:  # Only process valid token lines
                    if parts[2] == '-':
                        parts[2] = parts[1]  # Replace lemma with FORM
                    # Rebuild line with original newline character(s)
                    rebuilt = '\t'.join(parts) + '\n'
                    outfile.write(rebuilt)
                else:
                    outfile.write(line)  # Write malformed lines as-is

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace lemma values "-" with FORM in CONLLU file while preserving formatting')
    parser.add_argument('input', help='Input CONLLU file')
    parser.add_argument('output', help='Output CONLLU file')
    args = parser.parse_args()
    process_conllu(args.input, args.output)

#Usage
# python3 fix_conllu_lemmas.py input.conllu output.conllu


# ######Alternative

# import argparse

# def process_conllu(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:
#         for line in infile:
#             stripped_line = line.rstrip('\n')
#             if stripped_line.startswith('#'):
#                 outfile.write(line)
#                 continue
#             if not stripped_line.strip():
#                 outfile.write('\n')
#                 continue
#             parts = stripped_line.split('\t')
#             if len(parts) != 10:
#                 outfile.write(line)
#                 continue
#             lemma = parts[2]
#             if lemma == '-':
#                 parts[2] = parts[1]
#             modified_line = '\t'.join(parts) + '\n'
#             outfile.write(modified_line)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Replace lemma values "-" with FORM in CONLLU file.')
#     parser.add_argument('input', help='Input CONLLU file')
#     parser.add_argument('output', help='Output CONLLU file')
#     args = parser.parse_args()
#     process_conllu(args.input, args.output)

# #Usage : python script.py input.conllu output.conllu 
# # python3 replace_lemmas_with_form.py amh_att-ud-1302(raw).conllu amh_att-ud-1302(lemmareplaced).conllu 



# # def replace_lemmas_with_form(input_path, output_path):
# #     with open(input_path, 'r', encoding='utf-8') as infile, \
# #          open(output_path, 'w', encoding='utf-8') as outfile:
        
# #         for line in infile:
# #             # Preserve comments and empty lines
# #             if line.startswith("#") or line.strip() == "":
# #                 outfile.write(line)
# #                 continue
            
# #             parts = line.strip().split('\t')
            
# #             # Make sure it's a token line with at least 10 fields
# #             if len(parts) == 10:
# #                 form = parts[1]
# #                 lemma = parts[2]
# #                 if lemma == "-":
# #                     parts[2] = form  # Replace lemma with FORM
# #                 line = '\t'.join(parts) + '\n'

# #             outfile.write(line)

# # # Example usage:
# # replace_lemmas_with_form('amh_att-ud-1300(raw).conllu', 'output_lemma_replaced.conllu')
