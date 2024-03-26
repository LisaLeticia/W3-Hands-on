f = open("inputSTR.txt", "r", encoding="utf-8")        #讀取data(要和code放在同一個資料夾)
inputstr = f.read().replace('\n', " ")        #讓input等於讀取進來的資料，將分行用空格取代
inputstr1 = inputstr.replace('。', " ")       #用空格取代"。"
List = inputstr1.split("  ")        #字串分割成列表
#print(List)       #成功分割為['私（わたし）がリンゴを食べます', '彼（かれ）が本を読みます', ....]=>設命名為"List"





resultDICT = {"Subject": " ","Object": " ","Verb": " "}

def caseparse(inputSTR, refList=List):
    if inputSTR in List:
        pass
    elif inputSTR.endswith("。"):              #防未刪掉句號用
        inputSTR = inputSTR.split("。")[0]
        pass
        return
    else:
        print("該句可能不存在於List中，但可嘗試尋找SOV")


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
    else:
        pass
    return  resultDICT                   #得到動詞字典回傳
    


if __name__ == "__main__":
    corpusList = List

    for i in List[0:20]:
        inputSTR = i
        caseparse(inputSTR)            #呼叫functions
        extractSubject(inputSTR)
        extractObject(inputSTR)
        extractVerb(inputSTR)
        
        print(resultDICT)     #最後呈現結果
