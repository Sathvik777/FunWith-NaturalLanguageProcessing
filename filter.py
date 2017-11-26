from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

test_sentence = "This a Test proving NLTK stopping words work, a the an my our and, should not be printed"



def filter_sentence_with_stop_words():
    #Setting language to english
    stop_words = set(stopwords.words("english"))

    words_from_example_sentnce = word_tokenize(test_sentence)

    words_after_filter_stop_words = []

    for w in words_from_example_sentnce:
        if w not in stop_words:
            words_after_filter_stop_words.append(w)


    # Fancy one lineer if you like, I do not very much for learning
    #words_after_filter_stop_words = [w for w in words_from_example_sentnce if not w in stop_words]

    print(words_after_filter_stop_words)


if __name__ == "__main__":
    filter_sentence_with_stop_words()