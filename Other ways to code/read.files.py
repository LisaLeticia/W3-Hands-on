f = open("inputSTR.txt", "r", encoding="utf-8")        #讀取data(要和code放在同一個資料夾)
#"r"表示開啟的檔案為「唯讀」模式，另有"w":覆寫, "a":續寫
#encoding = "utf-8"是在檔案因為編碼問題無法被讀取時需要補上

inputstr = f.read().replace('\n', " ")        #讓input等於讀取進來的資料，將分行用空格取代
inputstr1 = inputstr.replace('。', " ")       #用空格取代"。"
List = inputstr1.split("  ")        #字串分割成列表
print(List)       #成功分割為['私（わたし）がリンゴを食べます', '彼（かれ）が本を読みます', ....]=>設命名為"List"

List1 = f.readlines() #和以上幾行有相同效果，readlines()自動將讀進來的檔案分行

