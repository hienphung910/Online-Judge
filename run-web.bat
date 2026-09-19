@echo off
REM Build backend Java + frontend React roi mo giao dien web tai http://localhost:8080
REM   run-web.bat          -> can MySQL (tao CSDL va cau hinh .env truoc, xem README)
REM   run-web.bat --no-db  -> KHONG can MySQL, du lieu nam trong RAM
chcp 65001 > nul
cd /d "%~dp0"

REM --no-db: bo qua MySQL hoan toan, du lieu chi nam trong RAM.
set NO_DB=
echo %* | findstr /C:"--no-db" > nul && set NO_DB=--no-db

set MYSQL_VERSION=8.4.0
set MYSQL_JAR=lib\mysql-connector-j-%MYSQL_VERSION%.jar

REM ---- [1/5] Kiem tra Java --------------------------------------------------
where javac > nul 2>&1
if errorlevel 1 (echo Khong tim thay javac. Cai JDK 11+ roi chay lai. & exit /b 1)

REM ---- [2/5] Thu vien MySQL Connector/J -------------------------------------
if not exist "%MYSQL_JAR%" (
    echo [2/5] Chuan bi MySQL Connector/J %MYSQL_VERSION%...
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
    echo Khong tai duoc MySQL Connector/J. Hay tai vao thu muc lib\ roi chay lai.
    exit /b 1
)

REM ---- [3/5] Bien dich backend ----------------------------------------------
echo [3/5] Bien dich backend Java...
if exist out rmdir /s /q out
if exist sources.txt del sources.txt
dir /s /b src\*.java > sources.txt
javac -encoding UTF-8 -cp "lib\*" -d out @sources.txt
del sources.txt
if errorlevel 1 (echo Bien dich Java that bai. & exit /b 1)

REM ---- [4/5] Build frontend --------------------------------------------------
echo [4/5] Build frontend...
where npm > nul 2>&1
if errorlevel 1 (
    echo Khong tim thay npm. Cai Node.js tai https://nodejs.org roi chay lai.
    echo Van co the dung giao dien console: run.bat
    exit /b 1
)
pushd frontend
if not exist node_modules (
    echo   Lan dau: dang cai package...
    call npm install --no-fund --no-audit
)
call npm run build
if errorlevel 1 (popd & echo Build frontend that bai. & exit /b 1)
popd

REM ---- [5/5] Kiem tra cau hinh MySQL roi chay --------------------------------
if not defined NO_DB if "%OJ_DB_URL%"=="" if not exist .env (
    echo.
    echo Chua cau hinh MySQL - giao dien web bat buoc phai co CSDL.
    echo   1. Tao CSDL : mysql -u root -p ^< database/mysql/01_create_database.sql
    echo   2. Cau hinh : copy .env.example .env  roi sua OJ_DB_* trong .env
    echo      ^(hoac dat bien moi truong OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD^)
    echo.
    echo Khong co MySQL van chay duoc: run-web.bat --no-db
    echo.
    exit /b 1
)

echo [5/5] Mo may chu tai http://localhost:8080 ...
if not defined NO_DB echo   Lan chay dau tien se tao bang trong MySQL va in mat khau admin ra terminal.
if defined NO_DB     echo   Che do --no-db: du lieu nam trong RAM, mat khau admin in ra moi lan chay.
echo.
java -Dfile.encoding=UTF-8 -cp "out;lib\*" com.ptit.oj.Main --serve=8080 %NO_DB%
