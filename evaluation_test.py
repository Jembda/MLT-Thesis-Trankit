import trankit 

 # ------------------------------------------------
 # Evaluate on Test Set 1
 # ------------------------------------------------
test_conllu_fpath = './amh_att-ud-1000-test.conllu'  
evaluator = trankit.TPipeline(
 category= Amharic,
 load_from=save_dir
 )
#  Evaluate the trained pipeline on the test set
results = evaluator.evaluate(test_conllu_fpath)
print("Test Evaluation Results:")
print(results)






#pipeline = trankit.Pipeline(
#    lang='am',  # ISO 639-1 code for Amharic
#    cache_dir='./amharic_1000_pipeline',  # directory with your trained model
#    gpu=True
#)

#with open(test_txt_fpath, 'r', encoding='utf-8') as f:
#    raw_text = f.read()

# Process the text
#output = pipeline(raw_text)

# To get CoNLL-U formatted output
#print(pipeline.tokenize(raw_text, return_conllu=True))


# ------------------------------------------------
# Evaluate on Test Set
# ------------------------------------------------

# # Define the language and pipeline cache directory
# category = 'amharic'  
# amharic_1000_pipeline = './amharic_1000_pipeline'  # path to trained model

# # Load the test text
# test_txt_fpath = './amh_att-ud-1000-test.txt'

# with open(test_txt_fpath, 'r', encoding='utf-8') as f:
#     raw_text = f.read()

# # Initialize the trained pipeline
# pipeline = trankit.Pipeline(lang=category, cache_dir=amharic_1000_pipeline, use_gpu=True)

# # Run prediction
# output = pipeline(text=raw_text)

# # Print output
# print(output)



# # import trankit

# # ------------------------------------------------
# # Evaluate on Test Set
# # ------------------------------------------------
# test_txt_fpath = './amh_att-ud-1000-test.txt'

# # Load trained pipeline - fix parameters
# pipeline = trankit.Pipeline(
#     lang='amharic',  
#     cache_dir='./amharic_1000_pipeline',  # directory containing trained model
#     #gpu=True  
# )

# with open(test_txt_fpath, 'r', encoding='utf-8') as f:
#     raw_text = f.read()

# # Process the text content (not file path)
# output = pipeline(raw_text)

# # To print/store results in CoNLL-U format:
# print(pipeline.tokenize(raw_text, return_conllu=True))

