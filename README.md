Raid-X
======

Zero byte mirroring for Windows.

![Properties](/screenshot.png)

Idea inspired from <a href= "https://github.com/iCHAIT/Python-Scripts/tree/master/OS%20X%20Mirror">iCHAIT's </a> and <a href="https://github.com/dufferzafar/Python-Scripts/tree/master/0xMirror"> dufferzafar's </a> 0xMirror, with some changes.
(The repo works for macs, so head there for non-windows solutions)

1. The script traverses the File system, and creates an empty directory structure.
2. Files in the structure are represented as .txt files, with some basic information relating to them inside said .txt file.
3. Information available inside txt files is customisable.
4. User customisable on which drives to map.
5. GUI built in PyQt4.

Note: Still in development. Requires the pywin32 module (available on sourceforge).
