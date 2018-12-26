
from data import DICTIONARY, LETTER_SCORES, scrabble_scores
dictlist=[]

score=0
TESTWORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

def load_words():
#    Load dictionary into a list and return list
    with open("dictionary.txt","r") as ls:
        for x in ls:
                a=ls.readline().capitalize().splitlines()
                dictlist.append(*a)
        return dictlist
        
    
def calc_word_value(word):
    

    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
      
    return sum(LETTER_SCORES.get(x.upper(),0) for x in word)
            
        
   
                                  
def max_word_value(a=load_words()):
    
    
    lst=[]
    
   
   
    [lst.append((i,calc_word_value(i.capitalize())))  for i in a]
    
   
    z=max([(x[1],x[0]) for x in lst])
    
   
    print(f"the {len(a)} args include:",a [:10])
   
    return z[1]
    
  
     
    #scorelist=calc_word_value()
    #"""Calculate the word with the max value, can receive a list
    #of words as arg, if none provided uses default DICTIONARY"""
        
if __name__ == "__main__":
    import test_wordvalue # run unittests to validate
   
#load_words()
calc_word_value("benzalphenylhydrazon")
#calc_word_value("Hexachlorocyclohexane")
#max_word_value(TESTWORDS,"barbeque")
#max_word_value() #"benzprint(calc_word_value("Hexachlorocyclohexane"))
#load_words()