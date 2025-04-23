import sys

def extract_text(conllu_file):
    sentences = []
    
    with open(conllu_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Extract text from lines starting with "# text ="
            if line.startswith("# text ="):
                sentence = line.replace("# text =", "").strip()
                sentences.append(sentence)
    
    return " ".join(sentences)

if __name__ == "__main__":
    if len(sys.argv) != 2:
	#print("Usage: python3 extract_text_from_conllu.py amh_att-ud-dev.conllu")
	#print("Usage: python3 extract_text_from_conllu.py amh_att-ud-1302-train.conllu")
	#print("Usage: python3 extract_text_from_conllu.py amh_att-ud-train.conllu")
        print("Usage: python3 extract_text_from_conllu.py amh_att-ud-1300-train.conllu")

        sys.exit(1)
    
    conllu_file = sys.argv[1]
    output_file = conllu_file.replace(".conllu", "_extracted.txt")
    
    paragraph = extract_text(conllu_file)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(paragraph)
    
    print(f"Extracted text saved to {output_file}")
