@echo off
REM Chay TOAN BO kiem thu cua project (Command Prompt):
REM   1. bien dich backend Java
REM   2. --selftest : cham lai bo bai nop mau va doi chieu verdict ky vong (khong can MySQL)
REM   3. --apitest  : kiem thu tich hop MySQL + dang nhap + phan quyen + quan tri de bai
REM   4. npm run build : bao dam frontend van bien dich duoc
REM
REM Buoc --apitest can bo bien moi truong RIENG tro toi mot CSDL co ten ket thuc
REM bang _test (vi du online_judge_test). Chua cau hinh thi buoc do se bi bo qua.

chcp 65001 > nul
cd /d "%~dp0"
setlocal enabledelayedexpansion

set MYSQL_VERSION=8.4.0
set MYSQL_JAR=lib\mysql-connector-j-%MYSQL_VERSION%.jar
set FAILURES=0

where javac > nul 2>&1
if errorlevel 1 (echo Khong tim thay javac. Cai JDK 11+ roi chay lai. & exit /b 1)

if not exist "%MYSQL_JAR%" (
    echo [0/4] Chuan bi MySQL Connector/J %MYSQL_VERSION%...
    if not exist lib mkdir lib
    where mvn > nul 2>&1
    if not errorlevel 1 call mvn -q dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
)
if not exist "%MYSQL_JAR%" (
    where curl > nul 2>&1
    if not errorlevel 1 curl -sSL -o "%MYSQL_JAR%" "https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/%MYSQL_VERSION%/mysql-connector-j-%MYSQL_VERSION%.jar"
)
if not exist "%MYSQL_JAR%" (
    echo Khong tai duoc MySQL Connector/J. Hay tai vao thu muc lib\ roi chay lai.
    exit /b 1
)

echo.
echo [1/4] Bien dich backend Java...
if exist out rmdir /s /q out
if exist sources.txt del sources.txt
dir /s /b src\*.java > sources.txt
javac -encoding UTF-8 -cp "lib\*" -d out @sources.txt
del sources.txt
if errorlevel 1 (echo   =^> Bien dich that bai. & exit /b 1)
echo   =^> Bien dich backend: DAT

echo.
echo [2/4] Kiem thu bo cham ^(--selftest, khong can MySQL^)...
java -Dfile.encoding=UTF-8 -cp "out;lib\*" com.ptit.oj.Main --selftest
if errorlevel 1 (set /a FAILURES+=1 & echo   =^> Bo cham: LOI) else (echo   =^> Bo cham: DAT)

echo.
echo [3/4] Kiem thu tich hop MySQL ^(--apitest^)...
if "%OJ_TEST_DB_URL%"=="" if not exist .env (
    echo   =^> BO QUA: chua dat OJ_TEST_DB_URL / OJ_TEST_DB_USER / OJ_TEST_DB_PASSWORD
    goto :skip_apitest
)
java -Dfile.encoding=UTF-8 -cp "out;lib\*" com.ptit.oj.Main --apitest
if errorlevel 1 (set /a FAILURES+=1 & echo   =^> Kiem thu tich hop: LOI) else (echo   =^> Kiem thu tich hop: DAT)
:skip_apitest

echo.
echo [4/4] Build frontend...
where npm > nul 2>&1
if errorlevel 1 (
    echo   =^> Bo qua ^(khong tim thay npm^)
) else (
    pushd frontend
    if not exist node_modules call npm install --no-fund --no-audit
    call npm run build
    if errorlevel 1 (popd & set /a FAILURES+=1 & echo   =^> Build frontend: LOI) else (popd & echo   =^> Build frontend: DAT)
)

echo.
if "!FAILURES!"=="0" (echo TAT CA KIEM THU DEU DAT.) else (echo CO !FAILURES! buoc kiem thu THAT BAI.)
exit /b !FAILURES!
