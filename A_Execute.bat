@echo off
setlocal

:: Get the directory of the batch file
for %%i in ("%~dp0.") do set "current_dir=%%~fi"

:: Create a new directory for storing files
set "destination_dir=%current_dir%\JPG_Files"
mkdir "%destination_dir%" 2>nul

:: Search for files starting with "PRDR" in the current directory
for %%F in ("%current_dir%\PRDR*") do (
    copy "%%F" "%destination_dir%\%%~nxF.jpg" >nul
    echo File "%%~nxF" copied and moved to "%destination_dir%" folder.
)

pause
