f = open("inputSTR.txt", "r", encoding = "utf-8")       
List = f.readlines()

resultDICT = {"Subject": " ","Object": " ","Verb": " "}

def caseparse(inputSTR):
    extractSubject(inputSTR)
    extractObject(inputSTR)
    extractVerb(inputSTR)


def extractSubject(inputSTR):
    if "が" in inputSTR:
        x = inputSTR.split("が")[0]
        resultDICT["Subject"] = x           #新增主詞字典
    else:
        pass
    return resultDICT                      #得到主詞字典回傳
           
    
def extractObject(inputSTR):       
    if "を" in inputSTR:
        x = (inputSTR.split("が")[1]).split("を")[0]      #新增受詞字典
        resultDICT["Object"] = x
    elif "に" in inputSTR:
        x = (inputSTR.split("が")[1]).split("に")[0]      #新增受詞字典
        resultDICT["Object"] = x
    elif "を" or "に" not in inputSTR:     #無受詞的句子
        x = " " 
        resultDICT["Object"] = x      
    else:
        pass
    return  resultDICT                     #得到受詞字典回傳
 
    
def extractVerb(inputSTR):
    if "を" in inputSTR:
        x = (inputSTR.split("を")[1]).split("ます")[0]     #新增動詞字典
        resultDICT["Verb"] = x
    elif "に" in inputSTR:
        x = (inputSTR.split("に")[1]).split("ます")[0]
        resultDICT["Verb"] = x
    elif "を" or "に" not in inputSTR:
        x = (inputSTR.split("が")[1]).split("ます")[0]     
        resultDICT["Verb"] = x      
    else:
        pass
    return  resultDICT                   #得到動詞字典回傳
    


if __name__ == "__main__":
    corpusList = List


for i in List[0:20]:
    inputSTR = i

    caseparse(inputSTR)            #呼叫functions
    print(resultDICT)     #最後呈現結果
