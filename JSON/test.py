import json

f=open('test.json');
myjson=f.read()
print("JSON=" + myjson )
mypy=json.loads(myjson)
marcadores=mypy['marcadores']
for m in marcadores:
    print("longitude=" + str(m['longitude']) )

