@ECHO OFF
c_ %* 2> %userprofile%\temp
SET ret=%ERRORLEVEL%
SET /p VAR=<%userprofile%\temp
DEL temp

IF %ret% == 1 (
    cd %VAR%
)