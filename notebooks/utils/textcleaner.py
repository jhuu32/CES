import re
import nltk
import string
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer('french')

punctationRegEx = re.compile('(\.|\!|\?|:|;|,|\")')
numberRegEx = re.compile("([0-9]+)")


def cleanText(text, cleanStopWords, useStemming=False, removePunctuation=True):
    '''clean the text with stopWords, stemming and custom reg expressions techniques '''
    # lower case
    text = text.lower()
    
    # substitute acronym and repetitive characters by its more canonical equivalent token
    text = re.sub("qu'", "que ", text)
    text = re.sub("qu ", "que ", text)
    text = re.sub("n°", "numéro ", text)
    text = re.sub("bcp", "beaucoup", text)
    text = re.sub("s.v.p", "s'il vous plait", text)    
    text = re.sub("tt ", "tout ", text)    
    text = re.sub("\+", " et ", text)
    
    text = re.sub(r"([^\s])[?]", r"\1 ?", text) # sticky question mark: add a space
    text = re.sub(r"(\?|\.|!){2,5}", r"\1 ", text) # repertitive characters => keep one representative
    
    
    text = re.sub("", "", text)    
    
    # expand separators / special characters
    text = re.sub("®|™|°|\/|-|\*|•|=|\(|\)|%|\{|\}", " ", text)
    
    # remove the contractions: eg: l’, m’, ...
    text = re.sub("(\s[a-zA-Z][’|\'])", " ", text)    
    text = re.sub("^([a-zA-Z][’|\'])", "", text)    
    
    # remove numbers
    text = numberRegEx.sub("", text)
        
    ## remove puncuation
    if removePunctuation:
        text = punctationRegEx.sub(" ", text)
    
    # convert words to lower case and split them    
    if not cleanStopWords is None:
        text = text.split()
        text = [w for w in text if not w in cleanStopWords]
        text = " ".join(text)    
    
    if useStemming:
        text = text.split()        
        stemmedWords = [stemmer.stem(word) for word in text]
        text = " ".join(stemmedWords)

    # compact successive space character
    text = re.sub("([\s]+)", " ", text)
    
    if len(text) == 0:
        text = " "
        
    return text