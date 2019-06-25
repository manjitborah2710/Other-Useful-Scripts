import pandas as pd
df=pd.read_csv("book1.csv")

st=""
for i in range(len(df)):
    s="<tr>\n\t"
    s=s+"<td><b>"+str(df.loc[i]["Method"])+"</b></td>\n\t"
    if str(df.loc[i]["Parameters"])!='nan':
        s=s+"<td>"+str(df.loc[i]["Parameters"])+"</td>\n\t"
    else:
        s=s+"<td>"+""+"</td>\n\t"
    s=s+"<td><b>"+str(df.loc[i]["Return Value"])+"</b></td>\n\t"
    s=s+"<td>"+str(df.loc[i]["Description"])+"</td>\n"
    s=s+"</tr>\n"
    st=st+s

f=open("a.txt","w")
f.write(st)
f.close()
