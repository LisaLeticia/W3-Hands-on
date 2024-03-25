str1 = "私（わたし）がリンゴを食べます。"
str2 = "が"
#print (str1[:str1.index(str2)])   #主詞


str3 = "を"
print(str1[str1.index(str2):str1.index(str3)])   #受詞butがリンゴ

#print(str1[str1.index(str3):])  #動詞butを食べます。

