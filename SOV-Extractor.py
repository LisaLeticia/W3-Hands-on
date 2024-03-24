f = open("inputSTR.txt", "r", encoding="utf-8")  #讀取data(要和code放在同一個資料夾)
inputSTR = f.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
inputSTR1 = inputSTR.replace('。', " ") #用空格取代"。"
List = inputSTR1.split("  ")  #字串分割成列表
#print(List) #成功分割為['私（わたし）がリンゴを食べます', '彼（かれ）が本を読みます', ....]=>設命名為"List"

resultDICT = {"Subject": " ","Object": " ","Verb": " "}

#def caseparse(List):
 #     for lines in List:
  #          if lines == True:
   #               pass
    #        else:
     #             print("輸入錯誤")


def extractSubject(inputSTR):
      if "が" in inputSTR:
            x = inputSTR.split("が")[0]
            resultDICT["Subject"] = x
      else:
            pass
      return resultDICT
    
    
    
    
    
    
def extractObject(inputSTR):       #按照此格式改寫成S和V的def extractor
      if "を" in inputSTR:
            x = (inputSTR.split("が")[1]).split("を")[0]
            resultDICT["Object"] = x
      elif "に" in inputSTR:
            x = (inputSTR.split("が")[1]).split("に")[0]
            resultDICT["Object"] = x
      else:
            pass
      return  resultDICT                     #得到受詞字典回傳
    
    
    

#def extractVerb(inputSTR):
    
    


if __name__ == "__main__":
    corpusList = List
    
inputSTR = "私（わたし）がリンゴを食べます。"
#caseparse(inputSTR)
#extractSubject(inputSTR)
#extractObject(inputSTR)
#extractVerb(inputSTR)
#resultDICT = extractVerb(inputSTR).update(extractObject(inputSTR).update(extractSubject(inputSTR)))  #最後呈現的字典
resultDICT = extractObject(inputSTR)
print(resultDICT)