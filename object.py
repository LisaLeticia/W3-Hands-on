
f = open("inputSTR.txt", "r", encoding="utf-8")  #讀取data(要和code放在同一個資料夾)
#inputSTR = f.read().replace('\n', " ")  #讓input等於讀取進來的資料，將分行用空格取代
inputSTR = f.readlines()  #讀取檔案並自動分行

#for lines in list:
    #print(lines)
resultDICT = {"Object", }
def extractObject(inputLIST):

    for lines in inputLIST:
        if "を" in lines:
            print((lines.split("が")[1]).split("を")[0])    
        elif "に" in lines:
            print((lines.split("が")[1]).split("に")[0])
        else:
            pass
    return resultDICT
#inputSTR = "田中さんが車を運転します。"

inputList = ["私（わたし）がリンゴを食べます。",
              "彼（かれ）が本を読みます。",
              "私（わたし）が友達を見ます。",
              "彼女（かのじょ）が花を買います。",
              "私（わたし）が犬を飼います。",
              "田中さんが車を運転します。",
              "あなたが手紙を書きます。",
              "先生が生徒に教えます。",
              "子供がお菓子を食べます。",
              "あなたが問題を解決します。",
              "友達がプレゼントを持ってきます。",
              "彼が日本語を話します。",
              "先生が質問に答えます。",
              "私が夕食を作ります。",
              "彼女がピアノを弾きます。",
              "あなたが助けを求めます。",
              "子供が遊びます。",
              "先生が新しい言葉を教えます。",
              "私がお茶を飲みます。",
              "彼がボールを投げます。"]

result = extractObject(inputList)

print()
    
#subject = jstring.split("が")[0]
#verb = jstring.split("を")[1]
#object =extractObject(jstring)

#jstring = "田中さんが車を運転します。" #測試句子一
#a = "先生が生徒に教えます。"          #測試句子二

#print(jstring.split("が")[0])                   #subject
#print(jstring.split("を")[1])                   #verb
#print((jstring.split("が")[1]).split("を")[0])  #object
#print(a.split("に")[1])

#jstring = "田中さんが車を運転します。"
#if "を" in line:
    #print((jstring.split("が")[1]).split("を")[0])
#if "に" in a:
    #print((a.split("が")[1]).split("に")[0])



    
        
        

