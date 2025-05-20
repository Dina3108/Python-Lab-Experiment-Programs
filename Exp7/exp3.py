import string
def unique_words(sentence):
    un=sentence.lower()
    uc="".join(c if c not in string.punctuation else " " for c in un)
    us=uc.split()
    uw=set(us)
    return len(uw)
sen=input("Enter Sentence: ")
print("No of Unique Words in the Sentence: ",unique_words(sen))
