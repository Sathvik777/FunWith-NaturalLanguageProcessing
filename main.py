import nltk
# Download nltk data sets.
from nltk.corpus import state_union
import filter

# Uncomment this if you need to download NLTK data set
#nltk.download()

steamm_test_words = ["sathvik", "sathviking", "sathivker"]
for word in steamm_test_words:
    filter.stemming_a_word(word)

test_set = state_union.raw("2006-GWBush.txt")
train_set = state_union.raw("2005-GWBush.txt")
filter.unSupervisedML_tokenizer(test_set,train_set)