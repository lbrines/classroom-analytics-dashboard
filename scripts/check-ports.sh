#!/bin/bash
# check-ports.sh
# Verificar disponibilidad de puertos para Dashboard Educativo

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🔍 Verificando puertos del Dashboard Educativo..."
echo ""

check_port() {
    local port=$1
    local service=$2
    
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${RED}❌ Puerto $port ($service) está en uso${NC}"
        echo "   Proceso usando el puerto:"
        lsof -Pi :$port -sTCP:LISTEN | tail -1
        return 1
    else
        echo -e "${GREEN}✅ Puerto $port ($service) está disponible${NC}"
        return 0
    fi
}

# Verificar puertos principales
all_available=0

check_port 3000 "Frontend" || all_available=1
check_port 8000 "Backend" || all_available=1
check_port 5432 "Database (Opcional)" || true
check_port 6379 "Redis (Opcional)" || true

echo ""
if [ $all_available -eq 0 ]; then
    echo -e "${GREEN}✅ Todos los puertos necesarios están disponibles${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Algunos puertos están en uso${NC}"
    echo ""
    echo "Para liberar puertos:"
    echo "  lsof -ti:8000 | xargs kill -9  # Liberar puerto 8000"
    echo "  lsof -ti:3000 | xargs kill -9  # Liberar puerto 3000"
    exit 1
fi

