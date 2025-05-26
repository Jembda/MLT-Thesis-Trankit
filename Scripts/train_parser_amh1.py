import trankit


category = 'customized-mwt'
#category = 'customized-mwt-ner'
save_dir = './amharic_1000_segmented_pipeline'


# Paths to training data
train_txt_fpath = './amh_att-ud-1000-train-segmented.txt'
dev_txt_fpath = './amh_att-ud-1000-train-segmented.txt'
train_conllu_fpath = './amh_att-ud-1000-train.conllu'
dev_conllu_fpath = './amh_att-ud-1000-train.conllu'


# -------------------------------------------------
# Train Tokenizer (requires raw text + CoNLL-U)
# -------------------------------------------------
tokenizer_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'tokenize',
        'save_dir': save_dir,
        'train_txt_fpath': train_txt_fpath,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_txt_fpath': dev_txt_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 20,  # Add hyperparameters
        'char_level': True  # Crucial for Ge'ez script languages
    }
)
tokenizer_trainer.train()

# -------------------------------------------------
# Train Multi-Word Splitter (requires CoNLL-U)
# -------------------------------------------------
mw_splitter_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'mwt',
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 20
    }
)
mw_splitter_trainer.train()

# -------------------------------------------------
# Train Dependency Parser (use 'posdep')
# -------------------------------------------------
parser_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'posdep',  # for dependency parsing
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 20
    }
)
parser_trainer.train()

# -------------------------------------------------
# Train Lemmatizer
# -------------------------------------------------
lemmatizer_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'lemmatize',
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 20
    }
)
lemmatizer_trainer.train()

