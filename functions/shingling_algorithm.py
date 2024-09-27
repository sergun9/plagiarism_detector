import re
import nltk
from nltk.tokenize import word_tokenize
# from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('russian'))



def preprocess_text(text: str):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    tokens = text.split()

    return remove_stopwords(tokens)



def remove_stopwords(tokens):
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens



def ngrams(tokens, size):
    ngrams = []
    for char in range(len(tokens)):
        if (len(tokens)-char) < size:
            break
        list_shingle = tokens[char:char+size]
        str_shingle = ' '.join(list_shingle)
        ngrams.append(str_shingle)
    return ngrams



if __name__ == "__main__":
    text = "Казанский инновационный университет имени В.Г. Тимирясова (КИУ)—негосударственный вуз Татарстана и Поволжья. "
    print(ngrams(preprocess_text(text), 5))


