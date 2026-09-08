@echo off
:GET_INP:
set /P cmd=Enter a Text:
echo cmd: %cmd% > file.txt
goto GET_INP