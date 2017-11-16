#This script will make the ocr data from somali.txt indexable
#f = open("somali.txt", "r")

#class used to store words in a document
class SomWord:
    definition = ""
    word = ""
    def appendToDefinition(self, appending):
        self.definition += appending

# class used to store documents in memory, i.e. each page of the dictionary
class SomDocument:
    words = []
    def addWord(self, word): #add a word to the document
        self.words.insert(word)
    def appendToLastWord(self, description):
        """This function append a description to the last word of the document.
        Returns false if there is no word in document"""
        if(len(self.words) == 0):
            return False
        else:
            self.words[-1].appendToDefinition(description)
            return True


with open('somali.txt') as f:
    lines = f.readlines()


