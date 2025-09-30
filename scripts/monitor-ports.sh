#!/bin/bash
# monitor-ports.sh
# Monitoreo continuo de puertos del Dashboard Educativo

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "🔍 Monitoreo continuo de puertos - Dashboard Educativo"
echo "   Presiona Ctrl+C para detener"
echo ""

while true; do
    clear
    echo "=== Estado de Puertos - $(date '+%Y-%m-%d %H:%M:%S') ==="
    echo ""
    
    # Frontend
    if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${GREEN}✅ Puerto 3000 (Frontend): ACTIVO${NC}"
        lsof -Pi :3000 -sTCP:LISTEN | tail -1
    else
        echo -e "${RED}❌ Puerto 3000 (Frontend): INACTIVO${NC}"
    fi
    
    echo ""
    
    # Backend
    if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${GREEN}✅ Puerto 8000 (Backend): ACTIVO${NC}"
        lsof -Pi :8000 -sTCP:LISTEN | tail -1
    else
        echo -e "${RED}❌ Puerto 8000 (Backend): INACTIVO${NC}"
    fi
    
    echo ""
    echo "=== Health Check ==="
    
    # Verificar Backend Health
    if curl -s http://localhost:8000/api/v1/health/health >/dev/null 2>&1; then
        echo -e "${GREEN}✅ Backend Health: OK${NC}"
    else
        echo -e "${RED}❌ Backend Health: FAILED${NC}"
    fi
    
    # Verificar Frontend
    if curl -s http://localhost:3000 >/dev/null 2>&1; then
        echo -e "${GREEN}✅ Frontend Health: OK${NC}"
    else
        echo -e "${RED}❌ Frontend Health: FAILED${NC}"
    fi
    
    echo ""
    echo "================================"
    echo "Actualización en 30 segundos..."
    
    sleep 30
done

