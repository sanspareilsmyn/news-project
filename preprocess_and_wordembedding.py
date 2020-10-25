import pathlib
import os
import re
import tensorflow as tf
import tensorflow_hub as hub

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
    print("Task Finished!")
    print(str(count) + " text files")
    
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
3. Word Embedding by using pretrained model (Token based text embedding trained on English Google News 7B corpus.)
'''''''''''''''

embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
embedding_layer = hub.KerasLayer(embedding, input_shape=[],
                            dtype=tf.string, trainable=True)

# Test code
test_string = tf.keras.preprocessing.text.text_to_word_sequence(articles[0])
print(embedding_layer(test_string))