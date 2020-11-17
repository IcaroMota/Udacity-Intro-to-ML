#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    print(type(content))
    words = ""
    
    stemmer = SnowballStemmer("english")
    
    
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans("", "", string.punctuation))

        ### project part 2: comment out the line below
        words = text_string.lstrip().rstrip().replace("  ", " ").split(" ")
        
        steam_words = [stemmer.stem(word) for word in words]
        
        steam_phrase = steam_words[0]
        steam_words.remove(steam_phrase)
        
        for i in range(len(steam_words)):
            steam_phrase = steam_phrase + ' ' + steam_words[i]

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        




    return steam_phrase

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print (text)



if __name__ == '__main__':
    main()

