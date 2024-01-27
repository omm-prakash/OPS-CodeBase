from utils import Time

import os

from tokenizers import Tokenizer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.normalizers import Lowercase
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from datasets import load_dataset, get_dataset_split_names, get_dataset_config_names

dataset_name = 'opus_books' #config['dataset-name'] 
config_name = 'en-fr' #config['config']
# path = os.path.join(os.getcwd(), 'data', config['source-lang-path'])

def get_data(dataset, language):
        for data in dataset:
                yield data['translation'][language] 

print('\nStarting data loading..')
tm1 = Time()
tm1.start('data loading')
print('>> The Hugging-Face dataset used:',dataset_name)

configs = get_dataset_config_names(dataset_name)
print('>> Avilable translations from English:',[x for x in configs if x[:2]=='en'])
print('>> Avilable splits in the dataset:',get_dataset_split_names(dataset_name, config_name))

print('\nDownloading dataset..')
tm2 = Time()
tm2.start('download data')
dataset = load_dataset(dataset_name, config_name, split=['train'], cache_dir='./data')
tm2.end()
print(dataset[0][10]['translation']['en'])
print(dataset[0][10]['translation']['fr'])
print('>> Number of translation samples:', dataset[0].num_rows)
tm1.end()

tokenizer = Tokenizer(WordLevel(unk_token='[UNK]'))
tokenizer.normalizer = Lowercase()
tokenizer.pre_tokenizer = Whitespace()
trainer = WordLevelTrainer(show_progress=True, min_frequency=2, special_tokens=['[UNK]','[PAD]','[SOS]','[EOS]'])
trainer.train_from_iterator(get_data(dataset, 'en'), trainer, length=dataset[0].num_rows)

tokenizer.save(path, pretty=True)

