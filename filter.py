import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union

#PorterStemmer is one of pre-trained stemmer NLTK provides 
from nltk.stem import PorterStemmer, WordNetLemmatizer

test_sentence = "This a Test proving NLTK stopping words work, a the an my our and, should not be printed"

steamm_test_words = ["sathvik", "sathviking", "sathivker"]

def filter_sentence_with_stop_words(sentence):
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

#Chunking data based on string Type (According to NLTK)
def chunk_data(taged_words):
    chuck_grammar = "Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"
    chuck_parser = nltk.RegexpParser(chuck_grammar) 
    chucked_data = chuck_parser.parse(taged_words)
    chucked_data.draw() 




def unSupervisedML_tokenizer(test_set, train_set):
    punkTSent_tokenizer = PunktSentenceTokenizer(train_set)
    tokenized_set = punkTSent_tokenizer.tokenize(test_set)
    try:
        for w in tokenized_set:
            words_taged = nltk.word_tokenize(w)
            positive_tages = nltk.pos_tag(words_taged)
            chunk_data(positive_tages)

    except Exception as e:
        print(str(e))


def stemming_a_word(word):
    print("actual word "+word)
    ps = PorterStemmer()
    print("stemmed word "+ps.stem(word))


def stemming_word_with_WordNet(word):
    print("actual word "+word)
    word_net = WordNetLemmatizer()
    """
    WordNetLemmatizer
    arg-1 : word
    arg-2 : noun, verb, adjective etc.. eg: (pos ="v")
    """

    print("stemmed word "+word_net.stem(word))



def named_entity_recognition(taged_words):
    named_entity_chunk = nltk.ne_chunk()
    named_entity_chunk.draw()




if __name__ == "__main__":
    filter_sentence_with_stop_words(test_sentence)
    for word in steamm_test_words:
        stemming_a_word(word)