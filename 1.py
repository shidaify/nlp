#!/usr/bin/env python
# coding: utf-8

# In[186]:


import re
f = open('corpus.txt','r')            # 返回一个文件对象      
lines = f.readlines()      #读取全部内容 ，并以列表方式返回  
text = []
for line in lines:  
    text.append(line)
print(len(text))


# In[250]:


key1 = r"\(.*(?<=因为).+?(?=所以).+\)"#筛选括号
pattern1 = re.compile(key1)
result_kuohu = [pattern1.findall(t) for t in text]
key4 = r"\(.+\)"
result =[]
num = 0
print(result_kuohu)
for s,t in zip(result_kuohu,text):
    num +=1
    get_ = []
    if s :#贪婪
        key2 = r"[^病](?<=因为).+[^卫生](?=所以)"
        pattern2 = re.compile(key2)
        for p in re.finditer(key2,t):
            pos = p.start() 
            pos_end = p.end()   
            result.append([num,p.group(),[pos,pos_end]])    
        for p in re.finditer(key4,t):
            pos = p.start()+2
            for p2 in re.finditer(key2,s[0]):               
                get_ =[]
                pos_end = p2.end() + pos - 2
                result.append([num,p2.group(),[pos,pos_end]])

    else:
        key3 = r"[^病](?<=因为).+?[^卫生](?=所以)"
        pattern3 = re.compile(key3) 
        for p in re.finditer(key3,t):
            pos = p.start() 
            pos_end = p.end() 
            result.append([num,p.group(),[pos,pos_end]])
    
print(result)


# In[261]:


length = [len(l[1]) for l in result]
space = max(length) + 1
print(length)
out = "{0}\t{1:{4}>6}\t*因为*\t{2:{4}<{3}}\t&所以&  {5}"
print(out.format("行号","前面三个字","全部",space,chr(12288),"后面三个字"))
num = 0
for r in result:
    if r[0] != '*':
        bef = r[2][0]  
        print(bef)
        bef1 = bef - 4 if bef > 4 else 0
        bef2 = bef - 1 if bef > 1 else 0
        aft = r[2][1]
        t = text[r[0]-1]
        print(out.format(r[0],t[bef1:bef2],r[1][1:],space,chr(12288),t[aft+2:aft+5]))


# In[263]:


file_name = open('out.txt','w')
for r in result:
    if r[0] != '*':
        bef = r[2][0]  
        bef1 = bef - 4 if bef > 4 else 0
        bef2 = bef - 1 if bef > 1 else 0
        aft = r[2][1]
        t = text[r[0]-1]
        file_name.write(out.format(r[0],t[bef1:bef2],r[1][1:],space,chr(12288),t[aft+2:aft+5]))
        file_name.write("\n")
file_name.close()

