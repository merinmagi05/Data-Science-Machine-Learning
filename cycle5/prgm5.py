import nltk
from nltk import ngrams
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize,word_tokenize
text1="The data give satisfies the requirement for model generation.This is used in Data Science Lab"
print("Sentence tokenization:")
print(sent_tokenize(text1))
print("Word tokenization:")
print(word_tokenize(text1))
text=word_tokenize(text1)
text2=[word for word in text if word not in stopwords.words('english')]
print("")
print("Removing stop words:")
print(text2)
print("")
print("n grams:")
unigrams=ngrams(text2,3)
for grams in unigrams:
    print(grams)
