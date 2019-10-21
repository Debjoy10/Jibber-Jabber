import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


nltk.pos_tag("Machine Learning is great".split())

from nltk.stem.porter import PorterStemmer
porter_stemmer=PorterStemmer()

print(porter_stemmer.stem('wolves'))

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('wolves'))

s="Albert Einstein was born on March 14,1879"
tags=nltk.pos_tag(s.split())
print(tags)

nltk.ne_chunk(tags).draw()
print(nltk.ne_chunk(tags))
