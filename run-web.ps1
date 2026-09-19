# Build backend Java + frontend React roi mo giao dien web.
#   .\run-web.ps1            -> http://localhost:8080
#   .\run-web.ps1 -Port 9000 -> doi cong
#   .\run-web.ps1 -NoDb      -> KHONG can MySQL, du lieu nam trong RAM
#
# Mac dinh che do nay CAN MySQL: hay tao CSDL va cau hinh .env truoc (xem README).
# Them -NoDb thi bo qua MySQL hoan toan: day du tinh nang nhung tai khoan va lich
# su nop bai mat khi tat may chu (de bai van doc/ghi o data/problems/).
param([int]$Port = 8080, [switch]$NoDb)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
chcp 65001 > $null

# ---- [1/5] Kiem tra Java ---------------------------------------------------
if (-not (Get-Command javac -ErrorAction SilentlyContinue)) {
    Write-Host "Khong tim thay javac. Cai JDK 11+ roi chay lai." -ForegroundColor Red
    exit 1
}

# ---- [2/5] Thu vien MySQL Connector/J -------------------------------------
$MysqlVersion = "8.4.0"
$MysqlJar = "lib\mysql-connector-j-$MysqlVersion.jar"
if (-not (Test-Path $MysqlJar)) {
    Write-Host "[2/5] Chuan bi MySQL Connector/J $MysqlVersion..." -ForegroundColor Cyan
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
            Write-Host "Hay tai file jar do vao thu muc lib\ roi chay lai." -ForegroundColor Yellow
            exit 1
        }
    }
}

# ---- [3/5] Bien dich backend ----------------------------------------------
Write-Host "[3/5] Bien dich backend Java..." -ForegroundColor Cyan
$sources = Get-ChildItem -Recurse -Filter *.java -Path src | ForEach-Object { $_.FullName }
if (Test-Path out) { Remove-Item -Recurse -Force out }
javac -encoding UTF-8 -cp "lib\*" -d out $sources
if ($LASTEXITCODE -ne 0) { Write-Host "Bien dich Java that bai." -ForegroundColor Red; exit 1 }

# ---- [4/5] Build frontend --------------------------------------------------
Write-Host "[4/5] Build frontend..." -ForegroundColor Cyan
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Host "Khong tim thay npm. Cai Node.js tai https://nodejs.org roi chay lai." -ForegroundColor Red
    Write-Host "Van co the dung giao dien console: .\run.ps1" -ForegroundColor Yellow
    exit 1
}
Push-Location frontend
if (-not (Test-Path node_modules)) {
    Write-Host "  Lan dau: dang cai package (mat khoang 30 giay)..." -ForegroundColor DarkGray
    npm install --no-fund --no-audit
}
npm run build
$buildFailed = $LASTEXITCODE -ne 0
Pop-Location
if ($buildFailed) { Write-Host "Build frontend that bai." -ForegroundColor Red; exit 1 }

# ---- [5/5] Kiem tra cau hinh MySQL roi chay --------------------------------
if (-not $NoDb -and -not $env:OJ_DB_URL -and -not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "Chua cau hinh MySQL - giao dien web bat buoc phai co CSDL." -ForegroundColor Yellow
    Write-Host "  1. Tao CSDL : mysql -u root -p < database/mysql/01_create_database.sql"
    Write-Host "  2. Cau hinh : Copy-Item .env.example .env  roi sua OJ_DB_* trong .env"
    Write-Host "     (hoac dat bien moi truong OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD)"
    Write-Host ""
    Write-Host "Khong co MySQL van chay duoc: .\run-web.ps1 -NoDb" -ForegroundColor DarkGray
    Write-Host ""
    exit 1
}

Write-Host "[5/5] Mo may chu tai http://localhost:$Port ...`n" -ForegroundColor Cyan
# Lan chay dau tien se tao bang trong MySQL va in mat khau admin ra terminal.
# Luu y: PowerShell se cat doi tham so -Dfile.encoding=UTF-8 neu khong boc dau ngoac kep
$JavaArgs = @("--serve=$Port")
if ($NoDb) { $JavaArgs += "--no-db" }
java "-Dfile.encoding=UTF-8" -cp "out;lib\*" com.ptit.oj.Main $JavaArgs
exit $LASTEXITCODE
