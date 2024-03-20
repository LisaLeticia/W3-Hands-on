def main(wordSTR="", wordClass="", refLIST=[]):
    '''
    main() is the main function of this program
    input:
        wordSTR   => string: the word to be tested
        wordClass => string: "verb", "object", "subject"
        refLIST   => list: corpus of reference sentences
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

    if refLIST == []:
        return "Please provide sentences for word class alculation"
    else:
        pass

    if wordClass == "verb":
        resultBOOL = verbChecker(wordSTR, refLIST)
    elif wordClass == "subject":
        resultBOOL = subjectChecker(wordSTR, refLIST)
    else wordClass == "object":
        resultBOOL = objectChecker(wordSTR, refLIST)
    else:
        resultBOOL = prepositionChecker(wordSTR, refLIST)

    return resultBOOL

def verbChecker(wordSTR, refLIST):
    '''
    verbChecker() checks if the wordSTR is a verb with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is a verb)
        False => boolean (the wordSTR is not a verb)
    '''


    resultBOOL = True
    for i in ("ます"):
        if wordSTR+i in ",".join(refLIST):
            pass
    for z in  ("を"):
        if z+wordSTR in ",".join(refLIST):
            pass        
        else:
            resultBOOL = False
    return resultBOOL