# Chay TOAN BO kiem thu cua project (Windows PowerShell):
#   1. bien dich backend Java
#   2. --selftest : cham lai bo bai nop mau va doi chieu verdict ky vong (khong can MySQL)
#   3. --apitest  : kiem thu tich hop MySQL + dang nhap + phan quyen + quan tri de bai
#   4. npm run build : bao dam frontend van bien dich duoc
#
# Buoc --apitest can bo bien moi truong RIENG tro toi mot CSDL co ten ket thuc
# bang _test (vi du online_judge_test). Neu chua cau hinh, buoc do se duoc bo qua.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
chcp 65001 > $null

if (-not (Get-Command javac -ErrorAction SilentlyContinue)) {
    Write-Host "Khong tim thay javac. Cai JDK 11+ roi chay lai." -ForegroundColor Red
    exit 1
}

$MysqlVersion = "8.4.0"
$MysqlJar = "lib\mysql-connector-j-$MysqlVersion.jar"
if (-not (Test-Path $MysqlJar)) {
    Write-Host "[0/4] Chuan bi MySQL Connector/J $MysqlVersion..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Force lib | Out-Null
    if (Get-Command mvn -ErrorAction SilentlyContinue) {
        try { mvn -q dependency:copy-dependencies "-DoutputDirectory=lib" "-DincludeScope=runtime" } catch { }
    }
    if (-not (Test-Path $MysqlJar)) {
        $url = "https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/$MysqlVersion/mysql-connector-j-$MysqlVersion.jar"
        try {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
            Invoke-WebRequest -Uri $url -OutFile $MysqlJar -UseBasicParsing
        } catch {
            Write-Host "Khong tai duoc $url" -ForegroundColor Red
            exit 1
        }
    }
}

$failures = 0

Write-Host "`n[1/4] Bien dich backend Java..." -ForegroundColor Cyan
$sources = Get-ChildItem -Recurse -Filter *.java -Path src | ForEach-Object { $_.FullName }
if (Test-Path out) { Remove-Item -Recurse -Force out }
javac -encoding UTF-8 -cp "lib\*" -d out $sources
if ($LASTEXITCODE -ne 0) { Write-Host "  => Bien dich that bai." -ForegroundColor Red; exit 1 }
Write-Host "  => Bien dich backend: DAT" -ForegroundColor Green

Write-Host "`n[2/4] Kiem thu bo cham (--selftest, khong can MySQL)..." -ForegroundColor Cyan
java "-Dfile.encoding=UTF-8" -cp "out;lib\*" com.ptit.oj.Main --selftest
if ($LASTEXITCODE -ne 0) { $failures++; Write-Host "  => Bo cham: LOI" -ForegroundColor Red }
else { Write-Host "  => Bo cham: DAT" -ForegroundColor Green }

Write-Host "`n[3/4] Kiem thu tich hop MySQL (--apitest)..." -ForegroundColor Cyan
if (-not $env:OJ_TEST_DB_URL -and -not (Test-Path ".env")) {
    Write-Host "  => BO QUA: chua dat OJ_TEST_DB_URL / OJ_TEST_DB_USER / OJ_TEST_DB_PASSWORD" -ForegroundColor Yellow
    Write-Host "     (chep .env.example thanh .env roi dien, CSDL phai co ten ket thuc bang _test)" -ForegroundColor DarkGray
} else {
    java "-Dfile.encoding=UTF-8" -cp "out;lib\*" com.ptit.oj.Main --apitest
    if ($LASTEXITCODE -ne 0) { $failures++; Write-Host "  => Kiem thu tich hop: LOI" -ForegroundColor Red }
    else { Write-Host "  => Kiem thu tich hop: DAT" -ForegroundColor Green }
}

Write-Host "`n[4/4] Build frontend..." -ForegroundColor Cyan
if (Get-Command npm -ErrorAction SilentlyContinue) {
    Push-Location frontend
    if (-not (Test-Path node_modules)) { npm install --no-fund --no-audit }
    npm run build
    $buildFailed = $LASTEXITCODE -ne 0
    Pop-Location
    if ($buildFailed) { $failures++; Write-Host "  => Build frontend: LOI" -ForegroundColor Red }
    else { Write-Host "  => Build frontend: DAT" -ForegroundColor Green }
} else {
    Write-Host "  => Bo qua (khong tim thay npm)" -ForegroundColor Yellow
}

Write-Host ""
if ($failures -eq 0) {
    Write-Host "TAT CA KIEM THU DEU DAT." -ForegroundColor Green
} else {
    Write-Host "CO $failures buoc kiem thu THAT BAI." -ForegroundColor Red
}
exit $failures
