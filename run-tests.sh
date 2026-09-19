#!/usr/bin/env bash
# Chay TOAN BO kiem thu cua project (Linux / macOS):
#   1. bien dich backend Java
#   2. --selftest : cham lai bo bai nop mau va doi chieu verdict ky vong (khong can MySQL)
#   3. --apitest  : kiem thu tich hop MySQL + dang nhap + phan quyen + quan tri de bai
#   4. npm run build : bao dam frontend van bien dich duoc
#
# Buoc --apitest can bo bien moi truong RIENG tro toi mot CSDL co ten ket thuc
# bang _test (vi du online_judge_test). Neu chua cau hinh, buoc do se duoc bo qua.
set -uo pipefail
cd "$(dirname "$0")"

MYSQL_VERSION="8.4.0"
MYSQL_JAR="lib/mysql-connector-j-${MYSQL_VERSION}.jar"
MYSQL_URL="https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/${MYSQL_VERSION}/mysql-connector-j-${MYSQL_VERSION}.jar"

if ! command -v javac > /dev/null 2>&1; then
    echo "Khong tim thay javac. Cai JDK 11+ roi chay lai."
    exit 1
fi

if [ ! -f "$MYSQL_JAR" ]; then
    echo "[0/4] Chuan bi MySQL Connector/J ${MYSQL_VERSION}..."
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
        echo "Khong tai duoc $MYSQL_URL - hay tai thu cong vao lib/ roi chay lai."
        exit 1
    fi
fi

FAILURES=0

echo
echo "[1/4] Bien dich backend Java..."
rm -rf out
SOURCES="$(mktemp)"
trap 'rm -f "$SOURCES"' EXIT
find src -name "*.java" > "$SOURCES"
if ! javac -encoding UTF-8 -cp "lib/*" -d out "@$SOURCES"; then
    echo "  => Bien dich that bai."
    exit 1
fi
echo "  => Bien dich backend: DAT"

echo
echo "[2/4] Kiem thu bo cham (--selftest, khong can MySQL)..."
if java -Dfile.encoding=UTF-8 -cp "out:lib/*" com.ptit.oj.Main --selftest; then
    echo "  => Bo cham: DAT"
else
    FAILURES=$((FAILURES + 1))
    echo "  => Bo cham: LOI"
fi

echo
echo "[3/4] Kiem thu tich hop MySQL (--apitest)..."
if [ -z "${OJ_TEST_DB_URL:-}" ] && [ ! -f .env ]; then
    echo "  => BO QUA: chua dat OJ_TEST_DB_URL / OJ_TEST_DB_USER / OJ_TEST_DB_PASSWORD"
    echo "     (cp .env.example .env roi dien, CSDL phai co ten ket thuc bang _test)"
else
    if java -Dfile.encoding=UTF-8 -cp "out:lib/*" com.ptit.oj.Main --apitest; then
        echo "  => Kiem thu tich hop: DAT"
    else
        FAILURES=$((FAILURES + 1))
        echo "  => Kiem thu tich hop: LOI"
    fi
fi

echo
echo "[4/4] Build frontend..."
if command -v npm > /dev/null 2>&1; then
    (
        cd frontend
        [ -d node_modules ] || npm install --no-fund --no-audit
        npm run build
    )
    if [ $? -eq 0 ]; then
        echo "  => Build frontend: DAT"
    else
        FAILURES=$((FAILURES + 1))
        echo "  => Build frontend: LOI"
    fi
else
    echo "  => Bo qua (khong tim thay npm)"
fi

echo
if [ "$FAILURES" -eq 0 ]; then
    echo "TAT CA KIEM THU DEU DAT."
else
    echo "CO $FAILURES buoc kiem thu THAT BAI."
fi
exit "$FAILURES"
