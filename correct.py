import os
import shutil
import config
import glob
from pathlib import Path

cwd = os.getcwd()

#wsdl
for path in Path(cwd).rglob('*.wsdl'):
    WSDLFileName = path.name
    WSDLPath=path
    p = path

f = open(p, 'r')
outFile = open(str(p.parent)+"\\New"+WSDLFileName,"wt")
Lines = f.readlines()
for line in Lines:
    if config.OperationList[0] in line and "<wsdl:message" in line:
        splittedList = list(line.split("<wsdl:message"))
        splittedList = ["<wsdl:message"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i

    if config.OperationList[0] in line and "<wsdl:operation" in line:
        splittedList = list(line.split("<wsdl:operation"))
        splittedList = ["<wsdl:operation"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i
    outFile.write(line)

f.close()
outFile.close()
print("wsdl ok")

#xsd
for path in Path(cwd).rglob('*V1.xsd'):
    XSDFileName = path.name
    XSDPath = path
    p = path

f = open(p, 'r')
outFile = open(str(p.parent)+"\\New"+XSDFileName,"wt")
Lines = f.readlines()
for line in Lines:
    if config.OperationList[0][:1].upper()+config.OperationList[0][1:] in line and "<xsd:complexType" in line:
        splittedList = list(line.split("<xsd:complexType"))
        splittedList = ["<xsd:complexType"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                j=j[:1].upper()+j[1:]
                if j in i:
                    line = i

    outFile.write(line)

f.close()
outFile.close()
print("xsd ok")

#schema
for path in Path(cwd).rglob('*InlineSchema1.xsd'):
    SCHEMAFileName = path.name
    SCHEMAPath = path
    p = path

f = open(p, 'r')
outFile = open(str(p.parent)+"\\New"+SCHEMAFileName,"wt")
Lines = f.readlines()
for line in Lines:
    if config.OperationList[0] in line and "<xsd:element" in line:
        splittedList = list(line.split("<xsd:element"))
        splittedList = ["<xsd:element"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i

    outFile.write(line)

f.close()
outFile.close()
print("schema ok")


#msgflow
for path in Path(cwd).rglob('*V1.msgflow'):
    MSGFLOWFileName = path.name
    MSGFLOWPath = path
    p = path

f = open(p, 'r')
outFile = open(str(p.parent)+"\\New"+MSGFLOWFileName,"wt")
Lines = f.readlines()
for line in Lines:
    if config.OperationList[0] in line and "xmlns:" in line:
        splittedList = list(line.split("xmlns:"))
        splittedList = ["xmlns:"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i

    if config.OperationList[0] in line and "<nodes" in line:
        splittedList = list(line.split("<nodes"))
        splittedList = ["<nodes"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i

    if "<connections" in line:
        line=""

    outFile.write(line)

f.close()
outFile.close()
print("msgflow ok")

#Descriptor
for path in Path(cwd).rglob('*service.descriptor'):
    DESCRIPTORFileName = path.name
    DESCRIPTORPath = path
    p = path

f = open(p, 'r')
outFile = open(str(p.parent)+"\\New"+DESCRIPTORFileName,"wt")
Lines = f.readlines()
for line in Lines:
    if config.OperationList[0] in line and "<ns2:operation" in line:
        splittedList = list(line.split("<ns2:operation"))
        splittedList = ["<ns2:operation"+x for x in splittedList if len(x) > 10]
        for i in splittedList:
            for j in config.OperationList:
                if j in i:
                    line = i

    outFile.write(line)

f.close()
outFile.close()
print("descriptor ok")

print("-----")
print("Check new Created files :")
print(str(WSDLPath.parent)+"\\New"+WSDLFileName)
print(str(XSDPath.parent)+"\\New"+XSDFileName)
print(str(SCHEMAPath.parent)+"\\New"+SCHEMAFileName)
print(str(MSGFLOWPath.parent)+"\\New"+MSGFLOWFileName)
print(str(DESCRIPTORPath.parent)+"\\New"+DESCRIPTORFileName)
print("-----")
print("If it's all right, press y and enter to replace old files with new files")
risp = input("Replace? (y/n)")
if risp == "y":
    try:
        os.makedirs(str(os.getcwd())+"\\Backup", exist_ok=True)
        files = glob.glob(str(os.getcwd())+"\\Backup\\*")
        for f in files:
            os.remove(f)
        os.rename(WSDLPath, str(os.getcwd())+"\\Backup\\"+WSDLFileName+".backup")
        os.rename(XSDPath, str(os.getcwd())+"\\Backup\\"+XSDFileName+".backup")
        os.rename(SCHEMAPath, str(os.getcwd())+"\\Backup\\"+SCHEMAFileName+".backup")
        os.rename(MSGFLOWPath, str(os.getcwd())+"\\Backup\\"+MSGFLOWFileName+".backup")
        os.rename(DESCRIPTORPath, str(os.getcwd())+"\\Backup\\"+DESCRIPTORFileName+".backup")
        print("Backup done")
    except:
        print("Couldn't backup files.")

    for path in Path(cwd).rglob('New*.*'):
        os.rename(path,str(path).replace("New",""))
    print("Replaced.")
else:
    print("Remember that now you have duplicated files. Use DeleteAllNewFiles.py to remove them.")
    print("Exit")
