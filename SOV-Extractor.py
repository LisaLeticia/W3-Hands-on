#!/usr/bin/env python3         #檔頭重要!
# -*- coding:utf-8 -*-



def caseparse(inputSTR):
    '''
    caseparse() is the function to call other functions (extractSubject, extractObject, and extractVerb)
    
    input:
        inputSTR => string: the string of List to be tested.
    output:
        call other functions.
    '''
    extractSubject(inputSTR)
    extractObject(inputSTR)
    extractVerb(inputSTR)


def extractSubject(inputSTR):
    '''
    extractSubject() is the function to split the subject out of a string.
    
    input:
        inputSTR => string: the string of List to be tested.
    output:
        add and return new value of subject to resultDICT.
    '''
    if "が" in inputSTR:
        x = inputSTR.split("が")[0]
        resultDICT["Subject"] = x           #新增主詞字典
    else:
        print("Please check your sentence. ")
    return resultDICT                      #得到主詞字典回傳
           
    
def extractObject(inputSTR):       
    '''
    extractObject() is the function to split the object out of a string.
    
    input:
        inputSTR => string: the string of List to be tested.
    output:
        add and return new value of object to resultDICT.
    '''
    if "を" in inputSTR:
        x = (inputSTR.split("が")[1]).split("を")[0]      #新增受詞字典
        resultDICT["Object"] = x
    elif "に" in inputSTR:
        x = (inputSTR.split("が")[1]).split("に")[0]      #新增受詞字典
        resultDICT["Object"] = x
    else:
        x = "No object " 
        resultDICT["Object"] = x        
    return  resultDICT                     #得到受詞字典回傳
 
    
def extractVerb(inputSTR):
    '''
    extractSubject() is the function to split the verb out of a string.
    
    input:
        inputSTR => string: the string of List to be tested.
    output:
        add and return new value of verb to resultDICT.
    '''    
    if "を" in inputSTR:
        x = (inputSTR.split("を")[1]).split("ます")[0]     #新增動詞字典
        resultDICT["Verb"] = x
    elif "に" in inputSTR:
        x = (inputSTR.split("に")[1]).split("ます")[0]
        resultDICT["Verb"] = x 
    else:
        x = (inputSTR.split("が")[1]).split("ます")[0]     
        resultDICT["Verb"] = x           
    return  resultDICT                   #得到動詞字典回傳
    


if __name__ == "__main__":
    
    with open("inputSTR.txt", "r", encoding = "utf-8") as f:   #讀檔放於程式進入點後，需縮排。(原本放檔頭後、function前，但讀檔非function，分隔太遠不好讀。感謝建議!)
        List = f.readlines()
    resultDICT = {"Subject": " ","Object": " ","Verb": " "}

    corpusList = List

    for i in List[0:len(List)]:      #在程式進入點後的for迴圈應縮排，程式較易讀(感謝建議!)
        inputSTR = i

        caseparse(inputSTR)            #呼叫functions
        print("Sentence: ", i, "\n", "resultDICT=", resultDICT, "\n")     #最後呈現結果

