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
    elif wordClass == "object":
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
    for i in ("る", "う", "くる", "す", "を"):
        if wordSTR+i in ",".join(refLIST):
            pass
        else:
            resultBOOL = False
    return resultBOOL

def subjectChecker(wordSTR, refLIST):
    '''
    subjectChecker() checks if the wordSTR is a subject with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is an subject)
        False => boolean (the wordSTR is not a subject)
    '''


    if wordSTR.endswith("y"):
        wordSTRstem = wordSTR[:-1]+"i"
    else:
        wordSTRstem = wordSTR

    counter = 0
    if wordSTRstem in ",".join(refLIST):
        counter = counter + 1

    for i in ("er", "est", "ly"):
        if wordSTRstem+i in ",".join(refLIST):
            counter = counter + 1
        else:
            pass

    if counter >= 2:
        resultBOOL = True
    else:
        resultBOOL = False

    return resultBOOL

def objectChecker(wordSTR, refLIST):
    '''
    objectChecker() checks if the wordSTR is an object with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is an object)
        False => boolean (the wordSTR is not an object)
    '''
   
       resultBOOL = True
    for i in ("s", ""):
        if " {}{} ".format(wordSTR, i) in " , ".join(refLIST):
            break
        elif " a {} ".format(wordSTR) in " , ".join(refLIST):
            break
        elif " an {} ".format(wordSTR) in " , ".join(refLIST):
            break
        elif " the {} ".format(wordSTR) in " , ".join(refLIST):
            break
        else:
            resultBOOL = False
    return resultBOOL