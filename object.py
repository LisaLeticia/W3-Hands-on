
f = open("inputSTR.txt", "r", encoding="utf-8")  #讀取data(要和code放在同一個資料夾)
#inputSTR = f.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
#這裡我們應該可以再討論要不要調整，這是Emily他們那組的作法(而且現在跑不過去QQ)
#whole_list = inputSTR.split('。 ')  #幫切好的資料取名為whole_list
list = f.readlines()

for lines in list:
    print(lines)

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
        

    
for lines in list:
    if "を" in lines:
        print((lines.split("が")[1]).split("を")[0])    
    elif "に" in lines:
        print((lines.split("が")[1]).split("に")[0])    
    
    
    #subject = jstring.split("が")[0]
    #verb = jstring.split("を")[1]
    #object =extractObject(jstring)




    
        
        

