#!/usr/bin/env bash
# Build va chay PTIT Online Judge - giao dien console (Linux / macOS).
#   ./run.sh              -> menu tuong tac (can dang nhap, can MySQL)
#   ./run.sh --demo       -> tu dong cham loat bai nop mau (khong can MySQL)
#   ./run.sh --selftest   -> cham va doi chieu voi verdict ky vong (khong can MySQL)
#   ./run.sh --no-db      -> menu tuong tac DAY DU nhung luu trong RAM (khong can MySQL)
#   ./run.sh --apitest    -> chay bo kiem thu tich hop tren CSDL *_test
#   ./run.sh --serve      -> mo REST API (giao dien web thi dung ./run-web.sh)
#
# Lan dau chay tren Linux nho cap quyen thuc thi: chmod +x run.sh
set -euo pipefail
cd "$(dirname "$0")"

MYSQL_VERSION="8.4.0"
MYSQL_JAR="lib/mysql-connector-j-${MYSQL_VERSION}.jar"
MYSQL_URL="https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/${MYSQL_VERSION}/mysql-connector-j-${MYSQL_VERSION}.jar"

# ---- [1/4] Kiem tra Java ---------------------------------------------------
if ! command -v javac > /dev/null 2>&1; then
    echo "Khong tim thay javac. Cai JDK 11+ roi chay lai."
    echo "  Ubuntu/Debian : sudo apt install default-jdk"
    exit 1
fi

# ---- [2/4] Thu vien MySQL Connector/J -------------------------------------
# Uu tien Maven (neu co); khong co thi tai thang tu Maven Central. Tai mot lan
# la cac lan sau chay offline duoc.
if [ ! -f "$MYSQL_JAR" ]; then
    echo "[2/4] Chuan bi MySQL Connector/J ${MYSQL_VERSION}..."
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
        echo "Khong tai duoc $MYSQL_URL"
        echo "Hay tai file jar do vao thu muc lib/ roi chay lai, hoac cai Maven va chay: mvn compile"
        exit 1
    fi
fi

CLASSPATH_ARG="out:lib/*"

# ---- [3/4] Bien dich -------------------------------------------------------
echo "[3/4] Bien dich ma nguon..."
rm -rf out
SOURCES="$(mktemp)"
trap 'rm -f "$SOURCES"' EXIT
find src -name "*.java" > "$SOURCES"
javac -encoding UTF-8 -cp "lib/*" -d out "@$SOURCES"

# ---- [4/4] Kiem tra cau hinh MySQL ----------------------------------------
# --demo, --selftest va --no-db chay hoan toan trong bo nho nen khong can MySQL.
NEEDS_DB=1
for arg in "$@"; do
    case "$arg" in
        --demo|--selftest|--no-db) NEEDS_DB=0 ;;
    esac
done
if [ "$NEEDS_DB" = "1" ] && [ -z "${OJ_DB_URL:-}" ] && [ ! -f .env ]; then
    echo
    echo "Chua cau hinh MySQL."
    echo "  1. Tao CSDL : mysql -u root -p < database/mysql/01_create_database.sql"
    echo "  2. Cau hinh : cp .env.example .env  roi sua OJ_DB_* trong .env"
    echo "     (hoac export OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD)"
    echo
    echo "Khong co MySQL van chay duoc:"
    echo "  ./run.sh --selftest   (cham bai nop mau roi doi chieu verdict)"
    echo "  ./run.sh --no-db      (menu day du tinh nang, du lieu nam trong RAM)"
    exit 1
fi

echo "[4/4] Chay chuong trinh..."
exec java -Dfile.encoding=UTF-8 -cp "$CLASSPATH_ARG" com.ptit.oj.Main "$@"
