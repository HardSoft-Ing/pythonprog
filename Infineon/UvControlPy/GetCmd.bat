@echo off
:GET_CMD
if not exist file.txt goto GET_CMD
rem echo file found, content is:
type file.txt
del file.txt
goto GET_CMD