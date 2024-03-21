
f = open("inputSTR.txt", "r")  #讀取data(要和code放在同一個資料夾)
inputSTR = data.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
#這裡我們應該可以再討論要不要調整，這是Emily他們那組的作法(而且現在跑不過去QQ)
whole_list = inputSTR.split('。 ')  #幫切好的資料取名為whole_list

def extractObject(inputLIST):
     
    jstring = "田中さんが車を運転します。" #測試句子一
    a = "先生が生徒に教えます。"          #測試句子二
    
    print(jstring.split("が")[0])                   #subject
    print(jstring.split("を")[1])                   #verb
    print((jstring.split("が")[1]).split("を")[0])  #object
    #print(a.split("に")[1])
    
    jstring = "田中さんが車を運転します。"
    if "を" in jstring:
        print((jstring.split("が")[1]).split("を")[0])
    if "に" in a:
        print((a.split("が")[1]).split("に")[0])
        

    
for i in whole_list:
    jstring = i
    #subject = jstring.split("が")[0]
    #verb = jstring.split("を")[1]
    object =extractObject(jstring)




    
        
        

