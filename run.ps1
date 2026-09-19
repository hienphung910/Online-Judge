# Build va chay PTIT Online Judge - giao dien console (Windows PowerShell)
#   .\run.ps1             -> menu tuong tac (can dang nhap, can MySQL)
#   .\run.ps1 --demo      -> tu dong cham loat bai nop mau (khong can MySQL)
#   .\run.ps1 --selftest  -> cham va doi chieu voi verdict ky vong (khong can MySQL)
#   .\run.ps1 --no-db     -> menu tuong tac DAY DU nhung luu trong RAM (khong can MySQL)
#   .\run.ps1 --apitest   -> chay bo kiem thu tich hop tren CSDL *_test

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# Hien thi tieng Viet dung tren console
chcp 65001 > $null

# ---- [1/4] Kiem tra Java ---------------------------------------------------
if (-not (Get-Command javac -ErrorAction SilentlyContinue)) {
    Write-Host "Khong tim thay javac. Cai JDK 11+ roi chay lai." -ForegroundColor Red
    exit 1
}

# ---- [2/4] Thu vien MySQL Connector/J -------------------------------------
# Uu tien Maven (neu may co cai); khong co thi tai thang tu Maven Central.
# Tai xong mot lan la cac lan sau chay offline duoc.
$MysqlVersion = "8.4.0"
$MysqlJar = "lib\mysql-connector-j-$MysqlVersion.jar"
if (-not (Test-Path $MysqlJar)) {
    Write-Host "[2/4] Chuan bi MySQL Connector/J $MysqlVersion..." -ForegroundColor Cyan
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
            Write-Host "Hay tai file jar do vao thu muc lib\ roi chay lai, hoac cai Maven va chay: mvn compile" -ForegroundColor Yellow
            exit 1
        }
    }
}

$Classpath = "out;lib\*"

# ---- [3/4] Bien dich -------------------------------------------------------
Write-Host "[3/4] Bien dich ma nguon..." -ForegroundColor Cyan
$sources = Get-ChildItem -Recurse -Filter *.java -Path src | ForEach-Object { $_.FullName }
if (Test-Path out) { Remove-Item -Recurse -Force out }
javac -encoding UTF-8 -cp "lib\*" -d out $sources
if ($LASTEXITCODE -ne 0) { Write-Host "Bien dich that bai." -ForegroundColor Red; exit 1 }

# ---- [4/4] Kiem tra cau hinh MySQL ----------------------------------------
# --demo, --selftest va --no-db chay hoan toan trong bo nho nen khong can MySQL.
$NeedsDatabase = -not ($args -contains "--demo" -or $args -contains "--selftest" `
                       -or $args -contains "--no-db")
if ($NeedsDatabase -and -not $env:OJ_DB_URL -and -not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "Chua cau hinh MySQL." -ForegroundColor Yellow
    Write-Host "  1. Tao CSDL : mysql -u root -p < database/mysql/01_create_database.sql"
    Write-Host "  2. Cau hinh : Copy-Item .env.example .env  roi sua OJ_DB_* trong .env"
    Write-Host "     (hoac dat bien moi truong OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD)"
    Write-Host ""
    Write-Host "Khong co MySQL van chay duoc:" -ForegroundColor DarkGray
    Write-Host "  .\run.ps1 --selftest   (cham bai nop mau roi doi chieu verdict)" -ForegroundColor DarkGray
    Write-Host "  .\run.ps1 --no-db      (menu day du tinh nang, du lieu nam trong RAM)" -ForegroundColor DarkGray
    exit 1
}

Write-Host "[4/4] Chay chuong trinh...`n" -ForegroundColor Cyan
# Luu y: PowerShell se cat doi tham so -Dfile.encoding=UTF-8 neu khong boc dau ngoac kep
java "-Dfile.encoding=UTF-8" -cp $Classpath com.ptit.oj.Main $args
exit $LASTEXITCODE
