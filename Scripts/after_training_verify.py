import trankit

trankit.verify_customized_pipeline(
    category='customized-mwt-ner', # pipeline category
    save_dir='./amharic_1300_pipeline', # directory used for saving models in previous steps
    embedding_name='xlm-roberta-base' # embedding version that we use for training our customized pipeline, by default, it is `xlm-roberta-base`
)
