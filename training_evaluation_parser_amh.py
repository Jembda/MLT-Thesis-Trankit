import trankit

# ----------------------------------
# Configuration
# ----------------------------------
#category = 'customized-mwt-ner'  # Using NER variant since we're evaluating lemmatization
category = 'customized-mwt'
save_dir = './amharic_1000_pipeline'

# Training data paths
train_txt_fpath = './amh_att-ud-1000-train.txt'
dev_txt_fpath = './amh_att-ud-1000-dev.txt'
train_conllu_fpath = './amh_att-ud-1000-train.conllu'
dev_conllu_fpath = './amh_att-ud-1000-dev.conllu'

# Test data paths
test_txt_fpath = './amh_att-ud-1000-test.txt'  
test_conllu_fpath = './amh_att-ud-1000-test.conllu'  

# -------------------------------------------
# Tokenizer Training & Evaluation
# -------------------------------------------
tokenizer_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'tokenize',
        'save_dir': save_dir,
        'train_txt_fpath': train_txt_fpath,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_txt_fpath': dev_txt_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        'max_epoch': 20,  # Increased epochs for better convergence
        'batch_size': 32,
        'char_level': True,  # Essential for Ge'ez script
        'learning_rate': 5e-5,
        'max_seqlen': 200  
    }
)
tokenizer_trainer.train()

# Tokenizer Evaluation
tokenizer = trankit.TPipeline(lang=category, cache_dir=save_dir)
tokenize_results = tokenizer.evaluate(test_conllu_fpath, task='tokenize')
print('\nTokenizer Test Results:')
print(f"Token F1: {tokenize_results['token']['f1']:.2%}")
print(f"Sentence Accuracy: {tokenize_results['sent']['acc']:.2%}")

# -----------------------------------------
# MWT Training & Evaluation
# -----------------------------------------
mw_splitter_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'mwt',
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        'max_epoch': 20,
        'batch_size': 16,
        'learning_rate': 2e-5
    }
)
mw_splitter_trainer.train()

# MWT Evaluation
mwt_evaluator = trankit.TPipeline(lang=category, cache_dir=save_dir)
mwt_results = mwt_evaluator.evaluate(test_conllu_fpath, task='mwt')
print('\nMWT Test Results:')
print(f"MWT F1: {mwt_results['mwt']['f1']:.2%}")

# ------------------------------------------------
# Dependency Parser Training & Evaluation
# ------------------------------------------------
parser_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'posdep',
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        'max_epoch': 20,
        'batch_size': 16,
        'learning_rate': 3e-5,
        'embed_dim': 512,
        'hidden_dim': 512
    }
)
parser_trainer.train()

# Parser Evaluation
parser = trankit.TPipeline(lang=category, cache_dir=save_dir)
depparse_results = parser.evaluate(test_conllu_fpath, task='posdep')
print('\nDependency Parsing Test Results:')
print(f"UAS: {depparse_results['uas']:.2%}")
print(f"LAS: {depparse_results['las']:.2%}")


# ------------------------------------------------
# Lemmatizer Training & Evaluation
# ------------------------------------------------
lemmatizer_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'lemmatize',
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 50,
        'batch_size': 32,
        'learning_rate': 1e-5,
        'lemma_beam_size': 3
    }
)
lemmatizer_trainer.train()

# Lemmatizer Evaluation
lemmatizer = trankit.TPipeline(lang=category, cache_dir=save_dir)
lemma_results = lemmatizer.evaluate(test_conllu_fpath, task='lemmatize')
print('\nLemmatization Test Results:')
print(f"Lemma Accuracy: {lemma_results['lemma']['acc']:.2%}")


# ---------------------------------------------
# Final Pipeline Verification
# ---------------------------------------------
print("\n\nFinal Pipeline Test:")
pipeline = trankit.Pipeline(lang=category, cache_dir=amharic_1000_pipeline)

# # Test with a sample sentence (needs to be replaced with actual Amharic text input)
# sample_text = "የኢትዮጵያ ብሔራዊ መዝሙር በሁሉም የሀገሪቱ ክፍሎች ይሰማል።"
# processed = pipeline(sample_text)
# print(processed)
