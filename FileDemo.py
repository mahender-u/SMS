'''fp1=open('abc.txt','w')
if fp1:
    print('file is created successfully')
fp1.write("hello good morning hru?")'''

fp2=open('abc.txt','r')
if fp2:
    print('file is opened successfully')
content=fp2.read()
print(content)