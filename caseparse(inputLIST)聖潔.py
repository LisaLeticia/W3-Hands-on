def main(wordSTR="", wordClass="", inputLIST=[]):
    '''
    main() is the main function of this program
    input:
        wordSTR   => string: the word to be tested
        wordClass => string: "verb", "object", "subject"
        inputLIST   => list: corpus of reference sentences
    output:
        True => boolean (the wordSTR belongs to the wordClass)
        False => boolean (the wordSTR does not belong to the wordClass)
    '''
    if wordClass == "":
        return "Please specify a word class. e.g., verb, object, subject"
    else:
        if wordClass in ("verb", "object", "subject"):
            pass
        else:
            return "Please specify a word class. e.g., verb, object, subject"

    if inputLIST == []:
        return "Please provide sentences for word class alculation"
    else:
        pass

    if wordClass == "verb":
        resultBOOL = verbChecker(wordSTR, inputLIST)
    elif wordClass == "subject":
        resultBOOL = subjectChecker(wordSTR, inputLIST)
    else:
        wordClass == "object"
        resultBOOL = objectChecker(wordSTR, inputLIST)

    return resultBOOL

def caseparse(inputLIST):
    extractSubject(inputLIST)
    extractObject(inputLIST)
    extractVerb (inputLIST)
    
def verbChecker(wordSTR, inputLIST):
    '''
    verbChecker() checks if the wordSTR is a verb with the inputLIST as reference.
    input:
        wordSTR => string
        inputLIST => list
    output:
        True  => boolean (the wordSTR is a verb)
        False => boolean (the wordSTR is not a verb)
    '''


    resultBOOL = True
    for i in ("ます"):
        if wordSTR+i in ",".join(inputLIST):
            pass
    for z in  ("を", "に"):
        if z+wordSTR in ",".join(inputLIST):
            pass        
        else:
            resultBOOL = False
    return resultBOOL