
f = open("inputSTR.txt", "r", encoding="utf-8")  #讀取data(要和code放在同一個資料夾)
#inputSTR = f.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
list = f.readlines()  #讀取檔案並自動分行

#for lines in list:
    #print(lines)

def extractObject(inputLIST):
     
    jstring = "田中さんが車を運転します。" #測試句子一
    a = "先生が生徒に教えます。"          #測試句子二
    
    print(jstring.split("が")[0])                   #subject
    print(jstring.split("を")[1])                   #verb
    print((jstring.split("が")[1]).split("を")[0])  #object
    #print(a.split("に")[1])
    
    jstring = "田中さんが車を運転します。"
    if "を" in line:
        print((jstring.split("が")[1]).split("を")[0])
    if "に" in a:
        print((a.split("が")[1]).split("に")[0])
        

#objects    
for lines in list:
    if "を" in lines:
        print((lines.split("が")[1]).split("を")[0])    
    elif "に" in lines:
        print((lines.split("が")[1]).split("に")[0])
    else:
        pass
    
    
    #subject = jstring.split("が")[0]
    #verb = jstring.split("を")[1]
    #object =extractObject(jstring)




    
        
        

