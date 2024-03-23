f = open("inputSTR.txt", "r", encoding="utf-8")  #讀取data(要和code放在同一個資料夾)
inputSTR = f.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
inputSTR1 = inputSTR.replace('。', " ") #用空格取代"。"
List = inputSTR1.split("  ")  #字串分割成列表
#print(List) #成功分割為['私（わたし）がリンゴを食べます', '彼（かれ）が本を読みます', ....]=>設命名為"List"


def caseparse(List):
    resultDICT = {"Subject":" ","Object":" ","Verb":" "}  #最後呈現的字典
    
def extractObject(List):       #按照此格式改寫成S和V的def extractor
    for lines in List:
        if "を" in lines:
            x = (lines.split("が")[1]).split("を")[0]
            resultDICT["Object"] = x
        elif "に" in lines:
            x = (lines.split("が")[1]).split("に")[0]
            resultDICT["Object"] = x
        else:
            pass
        
print()