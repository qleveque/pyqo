@ECHO OFF
c_ %* 2> %userprofile%\temp
SET r=%ERRORLEVEL%
SET /p VAR=<%userprofile%\temp
DEL %userprofile%\temp
echo non
IF "%r%"=="1" (
	echo oui
	cd /d %VAR%
)