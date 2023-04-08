import importDXF
import Part
import sys
import os

def convert(file_path):
    importDXF.insert(file_path,"con")

    __objs__=[]
    __objs__.append(FreeCAD.getDocument("con").getObject("Shape"))

    Part.export(__objs__, file_path[:-4] + ".stp")

def batch_convert(path):
    files = []
    for file in os.listdir(path):
        if file.endswith('.dxf'):
            files.append(file)

    for f in files:
        print(f)
        convert(path + f)

path = sys.argv[2]

if os.path.isdir(path):
    batch_convert(path)
elif os.path.isfile(path):
    convert(path)
