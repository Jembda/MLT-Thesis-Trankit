import trankit

trankit.download_missing_files(
	category='customized-ner',
	save_dir='./amharic_1000_pipeline',
	embedding_name='xlm-roberta-base',
	language='english'
)
