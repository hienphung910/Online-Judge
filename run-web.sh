#!/usr/bin/env bash
# Build backend Java + frontend React roi mo giao dien web (Linux / macOS).
#   ./run-web.sh         -> http://localhost:8080
#   ./run-web.sh 9000    -> doi cong
#   ./run-web.sh --no-db -> KHONG can MySQL, du lieu nam trong RAM
#
# Mac dinh che do nay CAN MySQL: hay tao CSDL va cau hinh .env truoc (xem README).
# Them --no-db thi bo qua MySQL hoan toan: day du tinh nang nhung tai khoan va lich
# su nop bai mat khi tat may chu (de bai van doc/ghi o data/problems/).
# Lan dau chay tren Linux nho cap quyen thuc thi: chmod +x run-web.sh run.sh
set -euo pipefail
cd "$(dirname "$0")"

PORT=8080
NO_DB=""
for arg in "$@"; do
    case "$arg" in
        --no-db)     NO_DB="--no-db" ;;
        [0-9]*)      PORT="$arg" ;;
        *) echo "Tham so khong hieu: $arg (chi nhan so cong hoac --no-db)"; exit 1 ;;
    esac
done
MYSQL_VERSION="8.4.0"
MYSQL_JAR="lib/mysql-connector-j-${MYSQL_VERSION}.jar"
MYSQL_URL="https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/${MYSQL_VERSION}/mysql-connector-j-${MYSQL_VERSION}.jar"

# ---- [1/5] Kiem tra Java ---------------------------------------------------
if ! command -v javac > /dev/null 2>&1; then
    echo "Khong tim thay javac. Cai JDK 11+ roi chay lai."
    echo "  Ubuntu/Debian : sudo apt install default-jdk"
    echo "  Fedora        : sudo dnf install java-latest-openjdk-devel"
    echo "  macOS         : brew install openjdk"
    exit 1
fi

# ---- [2/5] Thu vien MySQL Connector/J -------------------------------------
if [ ! -f "$MYSQL_JAR" ]; then
    echo "[2/5] Chuan bi MySQL Connector/J ${MYSQL_VERSION}..."
    mkdir -p lib
    if command -v mvn > /dev/null 2>&1; then
        mvn -q dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime || true
    fi
    if [ ! -f "$MYSQL_JAR" ]; then
        if command -v curl > /dev/null 2>&1; then
            curl -fsSL -o "$MYSQL_JAR" "$MYSQL_URL" || true
        elif command -v wget > /dev/null 2>&1; then
            wget -q -O "$MYSQL_JAR" "$MYSQL_URL" || true
        fi
    fi
    if [ ! -f "$MYSQL_JAR" ]; then
        echo "Khong tai duoc $MYSQL_URL - hay tai thu cong vao thu muc lib/ roi chay lai."
        exit 1
    fi
fi

# ---- [3/5] Bien dich backend ----------------------------------------------
echo "[3/5] Bien dich backend Java..."
rm -rf out
SOURCES="$(mktemp)"
trap 'rm -f "$SOURCES"' EXIT
find src -name "*.java" > "$SOURCES"
javac -encoding UTF-8 -cp "lib/*" -d out "@$SOURCES"

# ---- [4/5] Build frontend --------------------------------------------------
echo "[4/5] Build frontend..."
if ! command -v npm > /dev/null 2>&1; then
    echo "Khong tim thay npm. Cai Node.js (https://nodejs.org) roi chay lai."
    echo "Van co the dung giao dien console: ./run.sh"
    exit 1
fi
(
    cd frontend
    [ -d node_modules ] || npm install --no-fund --no-audit
    npm run build
)

# ---- [5/5] Kiem tra cau hinh MySQL roi chay --------------------------------
if [ -z "$NO_DB" ] && [ -z "${OJ_DB_URL:-}" ] && [ ! -f .env ]; then
    echo
    echo "Chua cau hinh MySQL - giao dien web bat buoc phai co CSDL."
    echo "  1. Tao CSDL : mysql -u root -p < database/mysql/01_create_database.sql"
    echo "  2. Cau hinh : cp .env.example .env  roi sua OJ_DB_* trong .env"
    echo "     (hoac export OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD)"
    echo
    echo "Khong co MySQL van chay duoc: ./run-web.sh --no-db"
    echo
    exit 1
fi

echo "[5/5] Mo may chu tai http://localhost:$PORT ..."
if [ -z "$NO_DB" ]; then
    echo "  Lan chay dau tien se tao bang trong MySQL va in mat khau admin ra terminal."
else
    echo "  Che do --no-db: du lieu nam trong RAM, mat khau admin in ra moi lan chay."
fi
echo
# exec de Ctrl+C di truc tiep vao tien trinh Java (shutdown hook dung may chu gon gang)
if [ -n "$NO_DB" ]; then
    exec java -Dfile.encoding=UTF-8 -cp "out:lib/*" com.ptit.oj.Main "--serve=$PORT" --no-db
fi
exec java -Dfile.encoding=UTF-8 -cp "out:lib/*" com.ptit.oj.Main "--serve=$PORT"
