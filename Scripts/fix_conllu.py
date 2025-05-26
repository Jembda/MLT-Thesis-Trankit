def ensure_empty_line(filepath):
    with open(filepath, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        if lines and not lines[-1].strip():  # If the last line is already empty, do nothing
            return
        f.write("\n")  # Append an empty line

# Paths to your CoNLL-U files
train_file = "/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-train.conllu"
dev_file = "/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-dev.conllu"

# Fix both files
ensure_empty_line(train_file)
ensure_empty_line(dev_file)

print("Empty line added to CoNLL-U files if needed.")
