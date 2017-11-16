#This script will make the ocr data from somali.txt indexable
#formating to Xml: https://lucene.apache.org/solr/guide/6_6/uploading-data-with-index-handlers.html#UploadingDatawithIndexHandlers-UsingcurltoPerformUpdates

#class used to store words in a document
class SomWord:
    definition = ""
    word = ""

    def __init__(self, str):#init with the text from the line
        parts = str.split(':')
        self.word = parts[0]
        self.definition = parts[1]
        if self.definition.startswith(" "):
            self.definition = self.definition[1:]
        if self.word.endswith(" "):
            self.word = self.word[:-1]

    def appendToDefinition(self, appending):#append the rest of the definition to the word
        if self.definition.endswith(","):
            self.definition += " "
        self.definition += appending

    def processDefinition(self, definition):#process the rest of the definition, so that it can easily be read by a human
        definition = definition.replace("{", "(")
        definition = definition.replace("}", ")")
        return  definition

VALID_START_LINE = 0 #constant indicating that the current line is a new entry
VALID_STARTED_LINE = 1 #constant indicating that the current line has already been started
UNVALID_LINE = 2 #constant indicating that the current line is no valid entry (i.e. page number/ letter)

words = []

#check if the given string is a number
def isNumber(s):
    if(len(s) > 5 or len(s) < 3):
        return False
    try:
        int(s)
        return True
    except ValueError:
        return False

#returns one of the three LINE constants based on what we can do with the line
def typeOfLine(line):
    if ":" in line:
        return VALID_START_LINE
    elif "EnglishIndex" in line:
        return UNVALID_LINE
    elif len(line) > 5:
        return VALID_STARTED_LINE
    elif isNumber(line):
        return UNVALID_LINE
    elif len(line) > 1:
        return  VALID_STARTED_LINE
    else:
        return UNVALID_LINE

#open the file and get all the words sorted
with open('somali.txt') as f:
    lines = f.read().split("\n")
    #lines = f.readlines()
    for line in lines:
        type = typeOfLine(line)
        if type == VALID_START_LINE:
            words.append(SomWord(line))
        elif type == VALID_STARTED_LINE:
            if len(words) is not 0:
                words[-1].appendToDefinition(line)
f.close()

#put all the words into add.txt so we can use curl
toWrite = "<add>\n"
for word in words:
    toWrite += "\t<doc>\n"
    toWrite += "\t\t<field name=\"en\">" + word.word + "</field>\n"
    toWrite += "\t\t<field name=\"so\">" + word.definition + "</field>\n"
    toWrite += "\t</doc>\n"
toWrite += "</add>"
file = open("somAddRequest.txt","w")
file.write(toWrite)
file.close()