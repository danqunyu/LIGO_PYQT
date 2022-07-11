import pandas as pd

# path = r"C:\Users\danqun\Desktop\test.xlsx"
# df = pd.read_excel(path, keep_default_na=None)

names = {'x': 'xx', 'y': 'yy', 'z': 'zz', 's': 'ss', 'o': 'oo'}
des = {'xx': "a,b,c", 'yy': "a,b,c,d", 'zz': "a,b", 'ss': "a,b,c,d,e,f", 'oo': "a,b,c,p"}
argValues = {'x': '1,2,3', 'y': '1,2,3,4', 'z': '1,2,', 's': '1,2,3,4,5', 'o': '1,2,3,9'}

columsNames = ['Names', 'TestMethod', 'Arg0', 'Arg1', 'Arg2', 'Arg3', 'Arg4', 'Arg5', 'Arg6', 'Arg7', 'Arg8']
df = pd.DataFrame(columns=columsNames)

df['Names'] = names.keys()
df['TestMethod'] = names.values()

for item in des.items():
    df.loc[df['TestMethod'] == item[0], 'Arg0'] = item[1]

colReplace = list(set(df.columns).difference(['Names', 'TestMethod', 'Arg0']))
colReplace.sort()
for item in argValues.items():
    valueReplace = item[1].split(',')
    df.loc[df['Names'] == item[0], colReplace] = valueReplace + [''] * (len(colReplace) - len(valueReplace))
print(df)