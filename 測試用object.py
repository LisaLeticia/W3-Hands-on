resultDICT = {"Subject":" ","Object":" ","Verb":" "}
lines = "私（わたし）がリンゴを食べます"
if "が" in lines:
            x = lines.split("が")[0]
            resultDICT["Subject"] = x
else:
            pass

if "を" in lines:
            x = (lines.split("が")[1]).split("を")[0]
            resultDICT["Object"] = x
elif "に" in lines:
            x = (lines.split("が")[1]).split("に")[0]
            resultDICT["Object"] = x
else:
            pass
      
print(resultDICT)