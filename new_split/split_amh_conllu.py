import os
import random

def read_conllu_sentences(input_file):
    """Reads a CoNLL-U file and returns a list of sentences."""
    if not os.path.exists(input_file):
        print(f"ERROR: File not found - {input_file}")
        return []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sentences = []
    current_sentence = []
    
    for line in lines:
        line = line.rstrip()
        if line:  # Non-empty line
            current_sentence.append(line)
        else:  # Empty line (sentence boundary)
            if current_sentence:
                sentences.append('\n'.join(current_sentence))
                current_sentence = []
    
    # Add the last sentence if file doesn't end with a newline
    if current_sentence:
        sentences.append('\n'.join(current_sentence))
    
    return sentences

def split_and_save_conllu(input_file, train_file, dev_file, test_file, 
                          train_ratio=0.8, dev_ratio=0.1, test_ratio=0.1):
    # Validate the ratios sum to 1.0
    assert abs((train_ratio + dev_ratio + test_ratio) - 1.0) < 1e-9, "Ratios must sum to 1.0"

    sentences = read_conllu_sentences(input_file)
    if not sentences:
        print("ERROR: No valid sentences found.")
        return
    
    random.shuffle(sentences)  # Shuffle in-place

    total = len(sentences)
    
    train_size = int(total * train_ratio)
    dev_size = int(total * dev_ratio)
    test_size = total - train_size - dev_size  # Ensure all sentences are used

    train = sentences[:train_size]
    dev = sentences[train_size:train_size + dev_size]
    test = sentences[train_size + dev_size:]

    # Save files with proper CoNLL-U formatting
    for data, path in [(train, train_file), (dev, dev_file), (test, test_file)]:
        if data:  # Only write non-empty splits
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(data) + '\n')  # Ensure trailing newline

    print(f"✅ Split complete: {len(train)} train, {len(dev)} dev, {len(test)} test sentences.")


# Corrected file paths
input_path = r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/am_att-ud-test.conllu'
output_dir = r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

split_and_save_conllu(
    input_file=input_path,
    train_file=os.path.join(output_dir, "amh_att-ud-train.conllu"),
    dev_file=os.path.join(output_dir, "amh_att-ud-dev.conllu"),
    test_file=os.path.join(output_dir, "amh_att-ud-test.conllu")
)