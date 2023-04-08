# dxf-to-stp-freecadcmd
Convert dxf files to stp using headless FreeCAD

# What is this
A primitive solution to quickly convert .dxf to .stp using FreeCAD command line.

***No error checking, tested on a few personal files on Windows 10 - use at your own risk or better yet just as an idea for your own solution.***

Original intended use: importing Adobe Illustrator vector graphics to [Plasticity](https://www.plasticity.xyz/)

# How to use
Navigate to FreeCAD bin folder.
Run FreeCADCmd.exe with two arguments:
1) path to conv.py from this repo
2) path to a directory with dxf files (converts them all in one go) or a single dxf file

> Single file example: .\FreeCADCmd.exe D:/conv.py D:/path-to-dxf/file.dxf

> Batch convert example: .\FreeCADCmd.exe D:/conv.py D:/path-to-dxf-files/

Outputs in the same directory as source dxf.
