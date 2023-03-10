from core.config import *
# from file_config import *


from gensim.models import Word2Vec
import csv

def vectorize_csv_with_w2v(file_path):
    with open(f"../{file_path}", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        sentences = list(csv_reader)

    # Train Word2Vec model
    model = Word2Vec(sentences, min_count=1)

    vectors = []
    for sentence in sentences:
        vector = sum([model.wv[word] for word in sentence if word in model.wv.key_to_index])
        vectors.append(vector)
    print(vectors)
    return vectors
