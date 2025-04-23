import trankit


#category = 'customized-mwt'
category = 'customized-mwt-ner'
save_dir = './amharic(allcomponents)_1300_pipeline'


# Paths to training data
#train_txt_fpath = './amh_att-ud-train.txt'
#dev_txt_fpath = './amh_att-ud-dev.txt'
#train_conllu_fpath = './amh_att-ud-train.conllu'
#dev_conllu_fpath = './amh_att-ud-dev.conllu'

train_txt_fpath = './amh_att-ud-1300-train.txt'
dev_txt_fpath = './amh_att-ud-1300-dev.txt'

train_conllu_fpath = './amh_att-ud-1300-train.conllu'
dev_conllu_fpath = './amh_att-ud-1300-train.conllu'

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
        #'max_epoch': 20  # Add hyperparameters
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
        #'max_epoch': 10
    }
)
mw_splitter_trainer.train()

# -------------------------------------------------
# Train Dependency Parser (use 'posdep')
# -------------------------------------------------
parser_trainer = trankit.TPipeline(
    training_config={
        'category': category,
        'task': 'posdep',  # Use 'posdep' for dependency parsing
        'save_dir': save_dir,
        'train_conllu_fpath': train_conllu_fpath,
        'dev_conllu_fpath': dev_conllu_fpath,
        #'max_epoch': 30
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
        #'max_epoch': 15
    }
)
lemmatizer_trainer.train()





# import trankit

# category = 'customized-mwt'

# # change all names when training with a different config, e.g. without the upgrade
# save_dir = './amharic(allcomponents)_1300_pipeline'


# train_txt_fpath = './amh_att-ud-train.txt'
# dev_txt_fpath = './amh_att-ud-dev.txt'

# train_conllu_fpath = './amh_att-ud-train.conllu'
# dev_conllu_fpath = './amh_att-ud-dev.conllu'



# # initialize a trainer for the task
# tokenizer_trainer = trankit.TPipeline(
#     training_config={
#     'category': category, # pipeline category
#     'task': 'tokenize', # task name
#     'save_dir': save_dir, # directory for saving trained model
#     'train_txt_fpath': train_txt_fpath, #raw text file
#     'train_conllu_fpath': train_conllu_fpath, # annotations file in CONLLU format for training
#     'dev_txt_fpath': dev_txt_fpath, # raw text file
#     'dev_conllu_fpath': dev_conllu_fpath # annotations file in CONLLU format for development
#     }
# )

# # # start training
# tokenizer_trainer.train()

# # # initialize a trainer for the task
# mw_splitter_trainer = trankit.TPipeline(
#     training_config={
#     'category': category, # pipeline category
#     'task': 'mwt', # task name
#     'save_dir': save_dir, # directory for saving trained model
#     'train_conllu_fpath': train_conllu_fpath, # annotations file in CONLLU format  for training
#     'dev_conllu_fpath': dev_conllu_fpath # annotations file in CONLLU format for development
#     }
# )

# # # start training
# mw_splitter_trainer.train()


# # # initialize a trainer for the task
# parser_trainer = trankit.TPipeline(
#     training_config={
#     'category': category, # pipeline category
#     'task': 'posdep', # task name
#     'save_dir': save_dir, # directory for saving trained model
#     'train_conllu_fpath': train_conllu_fpath, # annotations file in CONLLU format  for training
#     'dev_conllu_fpath': dev_conllu_fpath # annotations file in CONLLU format for development
#     }
# )

# parser_trainer.train()

# # #initialize a trainer for the task
# lemmatizer_trainer = trankit.TPipeline(
#     training_config={
#     'category': category,  # pipeline category
#     'task': 'lemmatize', # task name
#     'save_dir': save_dir, # directory for saving trained model
#     'train_conllu_fpath': train_conllu_fpath, # annotations file in CONLLU format  for training
#     'dev_conllu_fpath': dev_conllu_fpath # annotations file in CONLLU format for development
#     }
# )

# # start training
# lemmatizer_trainer.train()















# import trankit

# # initialize a trainer for the task
# trainer = trankit.TPipeline(
#     training_config={
#     'category': 'customized-mwt-ner', # pipeline category
#     'task': 'posdep', # task name
#     'save_dir': './amh(13.04.2025)_parser_dir', # directory for saving trained model
#     #'train_conllu_fpath': './amh_att-ud-train.conllu', # annotations file in CONLLU format  for training
#     'train_conllu_fpath':'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-train.conllu',
#     #'dev_conllu_fpath': './amh_att-ud-dev.conllu' # annotations file in CONLLU format for development
#     'dev_conllu_fpath': '/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-dev.conllu'
#     }
# )

# # start training
# trainer.train()






# import trankit
# import transformers
# transformers.logging.set_verbosity_error()
# from torch.optim import AdamW


# # initialize a trainer for the task
# trainer = trankit.TPipeline(
#     training_config={
#     'category': 'customized-mwt', # pipeline category
#     'task': 'posdep', # task name
#     #'save_dir': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_parser_dir', # directory for saving trained model
#     #'train_conllu_fpath': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-train.conllu', # annotations file in CONLLU format  for training
#     #'dev_conllu_fpath': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-dev.conllu' # annotations file in CONLLU format for development

#     #'save_dir': r'C:\Users\Min Dator\UD_Amharic-ATT\amh_parser_dir',
#     #'train_conllu_fpath': r'C:\Users\Min Dator\UD_Amharic-ATT\amh_att-ud-train.conllu',
#     #'dev_conllu_fpath': r'C:\Users\Min Dator\UD_Amharic-ATT\amh_att-ud-dev.conllu'

#     'save_dir': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_1300_parser_dir',
#     'train_conllu_fpath': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-train.conllu',
#     'dev_conllu_fpath': r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/amh_att-ud-dev.conllu',

#     }
# )

# # start training
# trainer.train()







#import os
#import random

# def read_conllu_sentences(input_file):
#     """Reads a CoNLL-U file and returns a list of sentences."""
#     if not os.path.exists(input_file):
#         print(f"ERROR: File not found - {input_file}")
#         return []
    
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     sentences = []
#     current_sentence = []
    
#     for line in lines:
#         line = line.rstrip()
#         if line:  # Non-empty line
#             current_sentence.append(line)
#         else:  # Empty line (sentence boundary)
#             if current_sentence:
#                 sentences.append('\n'.join(current_sentence))
#                 current_sentence = []
    
#     # Add the last sentence if file doesn't end with a newline
#     if current_sentence:
#         sentences.append('\n'.join(current_sentence))
    
#     return sentences

# def split_and_save_conllu(input_file, train_file, dev_file, test_file, 
#                           train_ratio=0.8, dev_ratio=0.1, test_ratio=0.1):
#     # Validate the ratios sum to 1.0
#     assert abs((train_ratio + dev_ratio + test_ratio) - 1.0) < 1e-9, "Ratios must sum to 1.0"

#     sentences = read_conllu_sentences(input_file)
#     if not sentences:
#         print("ERROR: No valid sentences found.")
#         return
    
#     random.shuffle(sentences)  # Shuffle in-place

#     total = len(sentences)
    
#     train_size = int(total * train_ratio)
#     dev_size = int(total * dev_ratio)
#     test_size = total - train_size - dev_size  # Ensure all sentences are used

#     train = sentences[:train_size]
#     dev = sentences[train_size:train_size + dev_size]
#     test = sentences[train_size + dev_size:]

#     # Save files with proper CoNLL-U formatting
#     for data, path in [(train, train_file), (dev, dev_file), (test, test_file)]:
#         if data:  # Only write non-empty splits
#             with open(path, 'w', encoding='utf-8') as f:
#                 f.write('\n\n'.join(data) + '\n')  # Ensure trailing newline

#     print(f"✅ Split complete: {len(train)} train, {len(dev)} dev, {len(test)} test sentences.")


# # Corrected file paths
# input_path = r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/am_att-ud-test.conllu'
# output_dir = r'/mnt/c/Users/Min Dator/UD_Amharic-ATT/'

# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# split_and_save_conllu(
#     input_file=input_path,
#     train_file=os.path.join(output_dir, "amh_att-ud-train.conllu"),
#     dev_file=os.path.join(output_dir, "amh_att-ud-dev.conllu"),
#     test_file=os.path.join(output_dir, "amh_att-ud-test.conllu")
# )
