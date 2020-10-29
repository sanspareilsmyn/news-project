import pathlib
import os
import re
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer


'''''''''''''''
1. Data Loading
'''''''''''''''

articles_path = "/Users/a1/Desktop/News/dataset/News Articles/"
summaries_path = "/Users/a1/Desktop/News/dataset/Summaries/"
articles_pathlist = list(pathlib.Path(articles_path).iterdir())
summaries_pathlist = list(pathlib.Path(summaries_path).iterdir())

def generate_data(folder):
    data = []
    count = 0
    for file in os.listdir(folder):
        try:
            text = ''
            name = file
            myfile = open(str(folder) + '/' + file, "r")
            text = myfile.read()
            #mylist = [name, text]
            count += 1
            data.append(text)
        except:
            continue
    print(str(count) + " text files loaded!")
    
    return data, count

# We are going to put all articles & summaries in these 2 lists.
articles = []
summaries = []

for article in articles_pathlist:
    data, count = generate_data(article)
    articles.extend(data)

for summary in summaries_pathlist:
    data, count = generate_data(summary)
    summaries.extend(data)

print('Articles # : ' + str(len(articles)))
print('Summaries # : ' + str(len(summaries)))



'''''''''''''''
2. Preprocessing sentences
'''''''''''''''

def preprocess_sentence(w):
    # Replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    w = re.sub(r"[^a-zA-Z?.!,]+", " ", w) 
    # Reducing spaces
    w = re.sub(r'[" "]+', " ", w)
    # lower case
    w = w.lower()
    return w

for i in range(len(articles)):
    articles[i] = preprocess_sentence(articles[i])
    
for i in range(len(summaries)):
    summaries[i] = preprocess_sentence(summaries[i])


'''''''''''''''
3. Word Embedding 
'''''''''''''''

# DataFrame definition(adding 'decoder_input, decoder_target')
articles = pd.DataFrame(articles)
summaries = pd.DataFrame(summaries)
articles_max_len = 20 ### 201029 - For Test! It should be longer when actually training!
summaries_max_len = 5 ### 201029 - For Test! It should be longer when actually training!
data = pd.concat([articles, summaries], axis=1)
data.columns = ['articles', 'summaries']

data['decoder_input'] = data['summaries'].apply(lambda x : 'sostoken ' + x)
data['decoder_target'] = data['summaries'].apply(lambda x: x + 'eostoken')
encoder_input = np.array(data['articles'])
decoder_input = np.array(data['decoder_input'])
decoder_target = np.array(data['decoder_target'])

# Train-test data split
n_of_val = int(len(encoder_input) * 0.1)

encoder_input_train = encoder_input[:-n_of_val]
decoder_input_train = decoder_input[:-n_of_val]
decoder_target_train = decoder_target[:-n_of_val]

encoder_input_test = encoder_input[-n_of_val:]
decoder_input_test = decoder_input[-n_of_val:]
decoder_target_test = decoder_target[-n_of_val:]

print('훈련 데이터의 개수 :', len(encoder_input_train))
print('훈련 레이블의 개수 :', len(decoder_input_train))
print('테스트 데이터의 개수 :', len(encoder_input_test))
print('테스트 레이블의 개수 :', len(decoder_input_test))

# Tokenizing Articles
article_vocab_num = 10000
article_tokenizer = Tokenizer(num_words=article_vocab_num)
article_tokenizer.fit_on_texts(encoder_input_train)

encoder_input_train = article_tokenizer.texts_to_sequences(encoder_input_train)
encoder_input_test = article_tokenizer.texts_to_sequences(encoder_input_test)

# Tokenizing Summaries
summary_vocab_num = 1000
summary_tokenizer = Tokenizer(num_words=summary_vocab_num)
summary_tokenizer.fit_on_texts(decoder_input_train)
summary_tokenizer.fit_on_texts(decoder_target_train)

decoder_input_train = summary_tokenizer.texts_to_sequences(decoder_input_train)
decoder_target_train = summary_tokenizer.texts_to_sequences(decoder_target_train)
decoder_input_test = summary_tokenizer.texts_to_sequences(decoder_input_test)
decoder_target_test = summary_tokenizer.texts_to_sequences(decoder_target_test)

# Padding tokenized data