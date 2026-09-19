@echo off
REM Build va chay PTIT Online Judge - giao dien console (Command Prompt)
REM   run.bat            -> menu tuong tac (can dang nhap, can MySQL)
REM   run.bat --demo     -> tu dong cham loat bai nop mau (khong can MySQL)
REM   run.bat --selftest -> cham va doi chieu verdict ky vong (khong can MySQL)
REM   run.bat --no-db    -> menu day du tinh nang nhung luu trong RAM (khong can MySQL)
REM   run.bat --apitest  -> chay bo kiem thu tich hop tren CSDL *_test

chcp 65001 > nul
cd /d "%~dp0"

set MYSQL_VERSION=8.4.0
set MYSQL_JAR=lib\mysql-connector-j-%MYSQL_VERSION%.jar

REM ---- [1/4] Kiem tra Java --------------------------------------------------
where javac > nul 2>&1
if errorlevel 1 (
    echo Khong tim thay javac. Cai JDK 11+ roi chay lai.
    exit /b 1
)

REM ---- [2/4] Thu vien MySQL Connector/J -------------------------------------
if not exist "%MYSQL_JAR%" (
    echo [2/4] Chuan bi MySQL Connector/J %MYSQL_VERSION%...
    if not exist lib mkdir lib
    where mvn > nul 2>&1
    if not errorlevel 1 call mvn -q dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
)
if not exist "%MYSQL_JAR%" (
    where curl > nul 2>&1
    if not errorlevel 1 curl -sSL -o "%MYSQL_JAR%" "https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/%MYSQL_VERSION%/mysql-connector-j-%MYSQL_VERSION%.jar"
)
if not exist "%MYSQL_JAR%" (
    powershell -NoProfile -Command "try { Invoke-WebRequest -Uri 'https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/%MYSQL_VERSION%/mysql-connector-j-%MYSQL_VERSION%.jar' -OutFile '%MYSQL_JAR%' -UseBasicParsing } catch { exit 1 }"
)
if not exist "%MYSQL_JAR%" (
    echo Khong tai duoc MySQL Connector/J.
    echo Hay tai mysql-connector-j-%MYSQL_VERSION%.jar vao thu muc lib\ roi chay lai.
    exit /b 1
)

REM ---- [3/4] Bien dich ------------------------------------------------------
echo [3/4] Bien dich ma nguon...
if exist out rmdir /s /q out
if exist sources.txt del sources.txt
dir /s /b src\*.java > sources.txt
javac -encoding UTF-8 -cp "lib\*" -d out @sources.txt
del sources.txt
if errorlevel 1 (
    echo Bien dich that bai.
    exit /b 1
)

REM ---- [4/4] Kiem tra cau hinh MySQL ----------------------------------------
REM --demo, --selftest va --no-db chay hoan toan trong bo nho nen khong can MySQL.
set NEEDS_DB=1
echo %* | findstr /C:"--demo" /C:"--selftest" /C:"--no-db" > nul && set NEEDS_DB=0
if "%NEEDS_DB%"=="1" if "%OJ_DB_URL%"=="" if not exist .env (
    echo.
    echo Chua cau hinh MySQL.
    echo   1. Tao CSDL : mysql -u root -p ^< database/mysql/01_create_database.sql
    echo   2. Cau hinh : copy .env.example .env  roi sua OJ_DB_* trong .env
    echo      ^(hoac dat bien moi truong OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD^)
    echo.
    echo Khong co MySQL van chay duoc:
    echo   run.bat --selftest   ^(cham bai nop mau roi doi chieu verdict^)
    echo   run.bat --no-db      ^(menu day du tinh nang, du lieu nam trong RAM^)
    exit /b 1
)

echo [4/4] Chay chuong trinh...
echo.
java -Dfile.encoding=UTF-8 -cp "out;lib\*" com.ptit.oj.Main %*
