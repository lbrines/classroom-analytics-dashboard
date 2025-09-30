#!/bin/bash
# dev.sh
# Inicio automático del Dashboard Educativo

set -e

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuración de puertos
FRONTEND_PORT=${FRONTEND_PORT:-3000}
BACKEND_PORT=${BACKEND_PORT:-8000}

echo "🚀 Iniciando Dashboard Educativo..."
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ Error: Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

# Verificar puertos
echo "📡 Verificando disponibilidad de puertos..."
if lsof -Pi :$BACKEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Puerto $BACKEND_PORT (Backend) en uso, liberando...${NC}"
    lsof -ti:$BACKEND_PORT | xargs kill -9 2>/dev/null || true
    sleep 2
fi

if lsof -Pi :$FRONTEND_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Puerto $FRONTEND_PORT (Frontend) en uso, liberando...${NC}"
    lsof -ti:$FRONTEND_PORT | xargs kill -9 2>/dev/null || true
    sleep 2
fi

# Verificar archivos .env
if [ ! -f "backend/.env" ]; then
    echo "📝 Creando backend/.env desde env.example..."
    cp backend/env.example backend/.env
fi

if [ ! -f "frontend/.env.local" ]; then
    echo "📝 Creando frontend/.env.local desde env.local.example..."
    cp frontend/env.local.example frontend/.env.local
fi

echo ""
echo -e "${GREEN}🎯 URLs del proyecto:${NC}"
echo "   Frontend: http://localhost:$FRONTEND_PORT"
echo "   Backend:  http://localhost:$BACKEND_PORT"
echo "   API Docs: http://localhost:$BACKEND_PORT/docs"
echo ""

# Iniciar Backend
echo "🐍 Iniciando Backend (puerto $BACKEND_PORT)..."
cd backend
python3 -m uvicorn app.main:app --reload --port $BACKEND_PORT > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
cd ..

# Esperar a que el backend esté listo
sleep 3

# Iniciar Frontend
echo "⚛️  Iniciando Frontend (puerto $FRONTEND_PORT)..."
cd frontend
npm run dev -- --port $FRONTEND_PORT > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

# Guardar PIDs
mkdir -p logs
echo $BACKEND_PID > logs/backend.pid
echo $FRONTEND_PID > logs/frontend.pid

echo ""
echo -e "${GREEN}✅ Servicios iniciados correctamente${NC}"
echo ""
echo "📋 PIDs:"
echo "   Backend:  $BACKEND_PID"
echo "   Frontend: $FRONTEND_PID"
echo ""
echo "📝 Logs:"
echo "   Backend:  tail -f logs/backend.log"
echo "   Frontend: tail -f logs/frontend.log"
echo ""
echo "🛑 Para detener los servicios:"
echo "   ./scripts/stop.sh"

