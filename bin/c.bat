@ECHO OFF
d %* -e > %userprofile%\temp
SET "VAR="
SET /p VAR=<%userprofile%\temp
DEL %userprofile%\temp
SET r=%ERRORLEVEL%
IF "%r%"=="0" (
    cd /d "%VAR%"
)
