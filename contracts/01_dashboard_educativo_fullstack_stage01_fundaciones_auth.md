# Contrato Stage 1: Fundaciones y Autenticación - Dashboard Educativo

## Información del Proyecto
- **Proyecto**: Dashboard Educativo
- **Fase**: Stage 1 - Fundaciones y Autenticación Completa
- **Autor**: Sistema de Contratos LLM
- **Fecha**: 2025-09-30
- **Propósito**: Establecer la base arquitectónica del sistema con autenticación completa

##############################################
## Objetivos del Stage 1

### Backend Fundacional
- Configurar servidor Python + FastAPI básico
- Implementar estructura de proyecto y configuración
- Crear servicios Mock con dataset inicial
- Establecer API REST básica con envelope estándar
- Implementar autenticación JWT mock
- Configurar testing básico (unitarios e integración)

### Frontend Fundacional
- Configurar Next.js 13.5.6 (LTS) con App Router + TypeScript
- Implementar estructura de componentes base
- Crear sistema de autenticación frontend
- Establecer comunicación con backend (API client)
- Implementar layout responsivo con Tailwind CSS
- Crear páginas principales (login, dashboard básico)
- Implementar sistema de internacionalización (i18n) con inglés como idioma base
- Configurar health checks y auto-cleanup para estabilidad

### Backend - Autenticación Avanzada
- Implementar autenticación OAuth 2.0 con Google en Python usando HTTPS obligatorio
- Configurar manejo de tokens de acceso y refresh tokens con rotación periódica
- Implementar middleware de autenticación OAuth con validación estricta
- Crear endpoints para flujo OAuth completo con PKCE (Proof Key for Code Exchange)
- Configurar seguridad y validación de tokens con restricción de privilegios
- Implementar limitación de permisos (scopes) siguiendo principio de menor privilegio
- Crear mecanismos anti-replay para prevenir reutilización de tokens

### Frontend - Flujo OAuth
- Implementar flujo OAuth en frontend con Next.js y React Query usando Authorization Code Flow
- Crear componentes para autenticación OAuth con generación segura de PKCE
- Manejar estados de autenticación múltiples (JWT y OAuth) con almacenamiento seguro
- Implementar callback de OAuth con validación de estado para prevenir CSRF
- Crear interfaz para gestión de cuentas y sesiones con opciones de revocación
- Implementar manejo de errores OAuth con mensajes amigables y logging seguro

##############################################
## Metodología TDD

Este proyecto sigue la metodología Test-Driven Development (TDD), que consiste en:

1. **Escribir tests primero**: Crear tests que definan el comportamiento esperado antes de implementar el código.
2. **Verificar que los tests fallen**: Ejecutar los tests para confirmar que fallan correctamente.
3. **Implementar código mínimo**: Escribir el código necesario para que los tests pasen.
4. **Verificar que los tests pasen**: Ejecutar los tests para confirmar su éxito.
5. **Refactorizar**: Mejorar el código manteniendo los tests exitosos.

Cada componente y funcionalidad debe seguir este ciclo de desarrollo.

##############################################
## Árbol de Directorios Completo

```
/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py
│   │   │   │   ├── oauth.py
│   │   │   │   └── health.py
│   │   │   └── router.py
│   │   ├── services/
│   │   │   ├── mock_service.py
│   │   │   ├── auth_service.py
│   │   │   └── oauth_service.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── exceptions.py
│   │   ├── middleware/
│   │   │   ├── auth_middleware.py
│   │   │   ├── oauth_middleware.py
│   │   │   └── validation_middleware.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── oauth_token.py
│   │   │   └── response.py
│   │   ├── schemas/
│   │   │   ├── user_schema.py
│   │   │   ├── oauth_schema.py
│   │   │   └── response_schema.py
│   │   ├── utils/
│   │   │   ├── logger.py
│   │   │   ├── response_helper.py
│   │   │   └── validation_helper.py
│   │   ├── data/
│   │   │   └── mock_users.json
│   │   └── main.py
│   ├── tests/
│   │   ├── unit/
│   │   │   ├── services/
│   │   │   └── endpoints/
│   │   └── integration/
│   │       └── test_auth.py
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── .env.example
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── oauth/
│   │   │   │       ├── callback/
│   │   │   │       │   └── page.tsx
│   │   │   │       └── page.tsx
│   │   │   ├── dashboard/
│   │   │   │   └── page.tsx
│   │   │   ├── globals.css
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Card.tsx
│   │   │   │   ├── Input.tsx
│   │   │   │   └── Layout.tsx
│   │   │   ├── auth/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   ├── OAuthButton.tsx
│   │   │   │   └── AuthGuard.tsx
│   │   │   └── dashboard/
│   │   │       ├── DashboardHeader.tsx
│   │   │       └── StatsCard.tsx
│   │   ├── i18n/
│   │   │   ├── config.ts
│   │   │   ├── locales/
│   │   │   │   └── en.json
│   │   │   └── types.ts
│   │   ├── lib/
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   ├── oauth.ts
│   │   │   └── utils.ts
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   ├── useOAuth.ts
│   │   │   ├── useApi.ts
│   │   │   └── useTranslation.ts
│   │   ├── types/
│   │   │   ├── auth.types.ts
│   │   │   ├── oauth.types.ts
│   │   │   └── api.types.ts
│   │   └── constants/
│   │       ├── api.constants.ts
│   │       └── oauth.constants.ts
│   ├── public/
│   │   ├── images/
│   │   └── icons/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   └── .env.local.example
```

##############################################
## Funcionalidades del Stage 1

### Backend - Funcionalidades Core
1. **Servidor Base**
   - FastAPI con Python
   - Middleware de CORS, logging y manejo de errores
   - Configuración de entorno con dotenv
   - Health check endpoint

2. **Autenticación Completa**
   - JWT tokens para sesiones
   - OAuth 2.0 con Google
   - Middleware de autenticación
   - Roles básicos: admin, coordinador, docente, estudiante
   - Endpoints: login, refresh, logout, oauth

3. **API REST Fundacional**
   - Envelope estándar `{data, meta, error?}` con estructura de errores tipados
   - Códigos HTTP apropiados y consistentes
   - Validación de entrada con feedback detallado
   - Manejo centralizado de errores con sanitización de información sensible
   - Catálogo de mensajes de error amigables para usuarios

4. **Dataset Mock Inicial**
   - Usuarios de prueba (admin, docentes, estudiantes)
   - Estructura base para cursos y tareas
   - Datos realistas para testing

### Frontend - Funcionalidades Core
1. **Configuración Base**
   - Next.js 13.5.6 (LTS) con App Router
   - TypeScript estricto
   - Tailwind CSS integrado
   - Configuración de ESLint y Prettier
   - Health checks automáticos del sistema
   - Auto-cleanup de procesos y archivos temporales

2. **Sistema de Autenticación Completo**
   - Formulario de login responsivo
   - Integración OAuth con Google
   - Manejo de tokens JWT
   - Protección de rutas
   - Persistencia de sesión
   - Selector de método de autenticación

3. **Layout y Navegación**
   - Layout principal responsivo
   - Navegación adaptativa (móvil/desktop)
   - Header con información de usuario
   - Sidebar colapsible

4. **Dashboard Básico**
   - Página principal post-login
   - Cards de estadísticas básicas
   - Navegación entre secciones
   - Indicadores de estado

5. **Sistema de Internacionalización (i18n)**
   - Arquitectura base para soporte multi-idioma
   - Inglés como idioma predeterminado
   - Componentes para traducción de textos
   - Hooks personalizados para acceso a traducciones
   - Estructura escalable para futuros idiomas

##############################################
## Endpoints del Stage 1

### Backend Endpoints
```
# Salud del sistema
GET /api/v1/health

# Autenticación JWT
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
GET /api/v1/auth/me

# Autenticación OAuth
GET /api/v1/oauth/google/url
GET /api/v1/oauth/google/callback
POST /api/v1/oauth/google/revoke
GET /api/v1/oauth/status

# Usuario actual
GET /api/v1/user/profile
```

### Respuestas Estándar
```json
// Éxito
{
  "data": { /* contenido */ },
  "meta": {
    "timestamp": "2025-09-25T13:15:00Z",
    "version": "1.0.0",
    "requestId": "uuid"
  }
}

// Error
{
  "error": {
    "code": "AUTH_INVALID_CREDENTIALS",
    "message": "Invalid credentials",
    "userMessage": "The username or password you entered is incorrect",
    "details": {
      "username": "The username you entered is incorrect",
      "password": "The password you entered is incorrect"
}
```

##############################################
## Dataset Mock del Stage 1

### Usuarios de Prueba
```json
{
  "users": [
    {
      "id": "admin-001",
      "email": "admin@educational.dashboard",
      "password": "admin123",
      "role": "admin",
      "name": "System Administrator",
      "active": true
    },
    {
      "id": "coord-001",
      "email": "coordinator@educational.dashboard",
      "password": "coord123",
      "role": "coordinator",
      "name": "Maria Gonzalez",
      "active": true
    },
    {
      "id": "teacher-001",
      "email": "teacher1@educational.dashboard",
      "password": "teacher123",
      "role": "teacher",
      "name": "Carlos Rodriguez",
      "active": true
    },
    {
      "id": "student-001",
      "email": "student1@educational.dashboard",
      "password": "student123",
      "role": "student",
      "name": "Ana Martinez",
      "active": true
    }
  ]
}
```

### OAuth Tokens Mock
```json
{
  "oauth_tokens": [
    {
      "user_id": "teacher-001",
      "provider": "google",
      "access_token": "ya29.mock-token-teacher",
      "refresh_token": "1//mock-refresh-token-teacher",
      "expires_at": "2025-10-30T14:30:00Z",
      "scope": "https://www.googleapis.com/auth/classroom.courses.readonly"
    }
  ]
}
```

##############################################
## Testing del Stage 1 con TDD

### Enfoque TDD para Backend
1. **Tests Unitarios Iniciales**
   - Escribir tests para cada servicio antes de su implementación
   - Definir comportamientos esperados mediante assertions claras
   - Crear mocks para dependencias externas

2. **Tests de Integración Iniciales**
   - Escribir tests para endpoints antes de implementarlos
   - Definir contratos de API mediante tests
   - Establecer casos de éxito y error esperados

### Backend Tests
1. **Tests Unitarios Iniciales**
   - `auth_service.test.py`: Tests para validación JWT antes de implementación
   - `oauth_service.test.py`: Tests para flujo OAuth antes de implementación
   - `mock_service.test.py`: Tests para validación de datos mock antes de creación
   - `response_helper.test.py`: Tests para envelope de respuestas antes de implementación

2. **Tests de Integración Iniciales**
   - `auth.integration.test.py`: Tests para endpoints de autenticación JWT
   - `oauth.integration.test.py`: Tests para endpoints de OAuth
   - `health.integration.test.py`: Tests para health check
   - `middleware.integration.test.py`: Tests para middleware de auth

### Enfoque TDD para Frontend
1. **Tests de Componentes Iniciales**
   - Escribir tests para cada componente UI antes de implementarlo
   - Definir props, eventos y comportamiento esperado
   - Crear mocks para servicios y contextos

2. **Tests de Hooks Iniciales**
   - Escribir tests para hooks personalizados antes de implementarlos
   - Definir comportamiento esperado para diferentes estados
   - Simular eventos y cambios de estado

### Frontend Tests
1. **Tests de Componentes Iniciales**
   - `LoginForm.test.tsx`: Tests para formulario de login antes de implementación
   - `OAuthButton.test.tsx`: Tests para botón de OAuth antes de implementación
   - `AuthGuard.test.tsx`: Tests para protección de rutas antes de implementación
   - `Layout.test.tsx`: Tests para layout principal antes de implementación
   - `TranslatedText.test.tsx`: Tests para componente de texto traducido antes de implementación

2. **Tests de Hooks Iniciales**
   - `useAuth.test.ts`: Tests para hook de autenticación JWT antes de implementación
   - `useOAuth.test.ts`: Tests para hook de autenticación OAuth antes de implementación
   - `useTranslation.test.ts`: Tests para hook de traducciones antes de implementación

##############################################
## Criterios de Aceptación (DoD) - Stage 1

### Backend
- [ ] Servidor FastAPI funcionando en puerto 8000 (desarrollo)
- [ ] Health check respondiendo correctamente
- [ ] Autenticación JWT implementada y funcionando
- [ ] Autenticación OAuth con Google implementada
- [ ] Middleware de auth protegiendo rutas
- [ ] Dataset mock cargado y accesible
- [ ] Envelope de respuesta estándar implementado
- [ ] Tests unitarios ≥70% cobertura
- [ ] Tests de integración para auth funcionando
- [ ] Logging estructurado configurado
- [ ] Variables de entorno configuradas por ambiente
- [ ] Documentación Swagger/OpenAPI generada automáticamente
- [ ] Scripts de gestión de puertos funcionando

### Frontend
- [ ] Next.js 13.5.6 (LTS) configurado y funcionando en puerto 3000 (desarrollo)
- [ ] Página de login responsiva y funcional
- [ ] Flujo OAuth con Google implementado
- [ ] Dashboard básico accesible post-login
- [ ] Autenticación frontend integrada con backend
- [ ] Layout responsivo (móvil, tablet, desktop)
- [ ] Tailwind CSS integrado correctamente
- [ ] Protección de rutas implementada
- [ ] Sistema i18n implementado con inglés como idioma base
- [ ] Componentes utilizando sistema de traducciones
- [ ] Manejo de estados de carga y error con React Query
- [ ] Tests de componentes básicos funcionando con Vitest y RTL
- [ ] TypeScript sin errores
- [ ] Variables de entorno configuradas por ambiente
- [ ] Health checks del sistema funcionando
- [ ] Auto-cleanup de procesos implementado
- [ ] Recuperación rápida (<30 min) ante errores críticos

### Integración
- [ ] Frontend y backend comunicándose correctamente
- [ ] CORS configurado apropiadamente para cada ambiente
- [ ] Tokens JWT funcionando end-to-end
- [ ] Flujo OAuth completo funcionando
- [ ] Manejo de errores consistente
- [ ] Sesiones persistiendo correctamente
- [ ] Scripts de verificación de puertos funcionando
- [ ] Configuración de Docker Compose operativa

### Criterios TDD
- [ ] Tests unitarios escritos antes de la implementación de cada componente
- [ ] Tests de integración escritos antes de conectar componentes
- [ ] Tests de infraestructura implementados
- [ ] Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- [ ] Documentación de decisiones de diseño basadas en tests
- [ ] Cobertura de tests cumple con el mínimo requerido (≥75%)
- [ ] Verificación de integridad de dependencias
- [ ] Procedimientos de rollback documentados

##############################################
## Configuración de Desarrollo

### Gestión de Puertos y Recursos

#### Asignación de Puertos por Ambiente
| Servicio | Desarrollo | Producción | Descripción |
|----------|------------|------------|-------------|
| Frontend | 3000 | 80/443 | Next.js Development |
| Backend | 8000 | 443 | FastAPI Development |
| Database | 5432 | 5432 | PostgreSQL |
| Redis | 6379 | 6379 | Cache (Opcional) |

#### Variables de Entorno por Ambiente

**Desarrollo (.env.development)**
```env
# Ambiente
ENVIRONMENT=development

# Puertos
FRONTEND_PORT=3000
BACKEND_PORT=8000
DATABASE_PORT=5432

# Backend
PORT=8000
JWT_SECRET=dev-secret-key-change-in-production
JWT_EXPIRES_IN=24h
CORS_ORIGIN=http://localhost:3000
LOG_LEVEL=debug

# OAuth
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:3000/oauth/callback
GOOGLE_SCOPES=profile,email,openid
OAUTH_PKCE_ENABLED=true
OAUTH_STATE_SECRET=your-random-state-secret
OAUTH_REFRESH_TOKEN_ROTATION_ENABLED=true
OAUTH_REFRESH_TOKEN_EXPIRY_DAYS=30
OAUTH_ACCESS_TOKEN_EXPIRY_MINUTES=15
OAUTH_ENFORCE_HTTPS=true
```

**Producción (.env.production)**
```env
# Ambiente
ENVIRONMENT=production

# Puertos
FRONTEND_PORT=80
BACKEND_PORT=443
DATABASE_PORT=5432

# Backend
PORT=443
JWT_SECRET=production-secret-key-change-this
JWT_EXPIRES_IN=1h
CORS_ORIGIN=https://your-domain.com
LOG_LEVEL=warning

# OAuth
GOOGLE_CLIENT_ID=your-production-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-production-google-client-secret
GOOGLE_REDIRECT_URI=https://your-domain.com/oauth/callback
GOOGLE_SCOPES=profile,email,openid
OAUTH_PKCE_ENABLED=true
OAUTH_STATE_SECRET=your-production-random-state-secret
OAUTH_REFRESH_TOKEN_ROTATION_ENABLED=true
OAUTH_REFRESH_TOKEN_EXPIRY_DAYS=15
OAUTH_ACCESS_TOKEN_EXPIRY_MINUTES=10
OAUTH_ENFORCE_HTTPS=true
```

#### Frontend (.env.local)
```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_NAME=Educational Dashboard
NEXT_PUBLIC_VERSION=1.0.0
NEXT_PUBLIC_DEFAULT_LOCALE=en

# OAuth
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
NEXT_PUBLIC_OAUTH_PKCE_ENABLED=true
NEXT_PUBLIC_OAUTH_ERROR_MESSAGES_ENABLED=true
NEXT_PUBLIC_OAUTH_SCOPES=profile,email,openid
NEXT_PUBLIC_ERROR_REPORTING_LEVEL=user-friendly
```

### Scripts de Gestión de Puertos

#### Verificación de Puertos (scripts/check-ports.sh)
```bash
#!/bin/bash
# Verificar disponibilidad de puertos

check_port() {
    local port=$1
    local service=$2
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "❌ Puerto $port ($service) está en uso"
        return 1
    else
        echo "✅ Puerto $port ($service) está disponible"
        return 0
    fi
}

echo "🔍 Verificando puertos del Dashboard Educativo..."
check_port 3000 "Frontend"
check_port 8000 "Backend"
check_port 5432 "Database"
check_port 6379 "Redis (Opcional)"

echo "✅ Verificación completada"
```

#### Inicio Automático (scripts/dev.sh)
```bash
#!/bin/bash
# Inicio automático con detección de puertos

source .env.development 2>/dev/null || {
    echo "⚠️  Archivo .env.development no encontrado, usando valores por defecto"
    FRONTEND_PORT=3000
    BACKEND_PORT=8000
}

echo "🚀 Iniciando Dashboard Educativo..."
echo "Frontend: http://localhost:$FRONTEND_PORT"
echo "Backend: http://localhost:$BACKEND_PORT"

# Verificar puertos
./scripts/check-ports.sh

# Iniciar servicios
cd frontend && npm run dev -- --port $FRONTEND_PORT &
cd backend && python -m uvicorn app.main:app --reload --port $BACKEND_PORT &

echo "✅ Servicios iniciados"
```

#### Monitoreo de Puertos (scripts/monitor-ports.sh)
```bash
#!/bin/bash
# Monitoreo continuo de puertos

while true; do
    echo "=== Estado de Puertos $(date) ==="
    
    for port in 3000 8000 5432; do
        if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
            echo "✅ Puerto $port: ACTIVO"
        else
            echo "❌ Puerto $port: INACTIVO"
        fi
    done
    
    echo "================================"
    sleep 30
done
```

#### Scripts de Soporte TDD (scripts/tdd-support.sh)
```bash
#!/bin/bash
# Scripts para facilitar el desarrollo TDD

# Ejecutar tests en modo watch
tdd_watch() {
  cd backend && python -m pytest --watch
}

# Verificar que los tests fallen antes de implementación
tdd_verify_fail() {
  cd backend && python -m pytest --new-only
}

# Verificar cobertura de tests
tdd_coverage() {
  cd backend && python -m pytest --cov=app
}

# Ejecutar ciclo TDD completo
tdd_cycle() {
  tdd_verify_fail && echo "✅ Tests fallan correctamente" || exit 1
  # Implementar código...
  tdd_watch && echo "✅ Tests pasan después de implementación" || exit 1
  tdd_coverage && echo "✅ Cobertura verificada" || exit 1
}
```

### Comandos de Desarrollo

#### Comandos por Ambiente

**Desarrollo**
```bash
# Verificar puertos disponibles
./scripts/check-ports.sh

# Iniciar con detección automática
./scripts/dev.sh

# Monitoreo continuo
./scripts/monitor-ports.sh

# Backend manual
cd backend
python -m uvicorn app.main:app --reload --port 8000
python -m pytest                        # Ejecutar tests
python -m pytest --watch                # Tests en modo watch

# Frontend manual
cd frontend
npm run dev -- --port 3000  # Next.js en modo desarrollo
npm run test         # Ejecutar tests con Vitest

# Docker Compose desarrollo
docker-compose -f docker-compose.dev.yml up
```

**Producción**
```bash
# Build de producción
cd frontend
npm run build

# Backend producción
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Docker Compose producción
docker-compose -f docker-compose.prod.yml up -d
```

#### Docker Compose (docker-compose.yml)
```yaml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports:
      - "${FRONTEND_PORT:-3000}:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:${BACKEND_PORT:-8000}/api/v1
    depends_on:
      - backend
  
  backend:
    build: ./backend
    ports:
      - "${BACKEND_PORT:-8000}:8000"
    environment:
      - PORT=8000
      - CORS_ORIGIN=http://localhost:${FRONTEND_PORT:-3000}
    depends_on:
      - database
  
  database:
    image: mongo:6.0
    ports:
      - "${DATABASE_PORT:-27017}:27017"
    environment:
      - MONGO_INITDB_DATABASE=educational_dashboard
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
```

#### Docker Compose por Ambiente

**Desarrollo (docker-compose.dev.yml)**
```yaml
version: '3.8'
services:
  frontend:
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
  
  backend:
    ports:
      - "8000:8000"
    environment:
      - PORT=8000
      - CORS_ORIGIN=http://localhost:3000
      - LOG_LEVEL=debug
```

**Producción (docker-compose.prod.yml)**
```yaml
version: '3.8'
services:
  frontend:
    ports:
      - "80:3000"
      - "443:3000"
    environment:
      - NEXT_PUBLIC_API_URL=https://your-domain.com/api/v1
  
  backend:
    ports:
      - "443:8000"
    environment:
      - PORT=8000
      - CORS_ORIGIN=https://your-domain.com
      - LOG_LEVEL=warning
```

##############################################
## Flujo de Trabajo del Stage 1

### Orden de Implementación con TDD
1. **Backend Base** (3-4 días)
   - Día 1: Escribir tests para servidor FastAPI y autenticación JWT
   - Día 2: Implementar servidor y autenticación para pasar tests
   - Día 3: Escribir tests para dataset mock
   - Día 4: Implementar dataset mock y refactorizar

2. **Backend OAuth** (3-4 días)
   - Día 1: Escribir tests para flujo OAuth con Google
   - Día 2: Implementar endpoints OAuth para pasar tests básicos
   - Día 3: Escribir tests para manejo de tokens
   - Día 4: Completar implementación OAuth y refactorizar

3. **Frontend Base** (3-4 días)
   - Día 1: Escribir tests para componentes de login y layout
   - Día 2: Implementar componentes para pasar tests
   - Día 3: Escribir tests para integración con backend
   - Día 4: Implementar integración y refactorizar

4. **Frontend OAuth** (3-4 días)
   - Día 1: Escribir tests para componentes OAuth
   - Día 2: Implementar componentes OAuth para pasar tests
   - Día 3: Escribir tests para flujo completo
   - Día 4: Implementar flujo completo y refactorizar

5. **Integración y Testing Final** (2-3 días)
   - Día 1: Escribir tests end-to-end para flujos completos
   - Día 2-3: Ajustar implementación para pasar tests E2E y documentar

### Criterios de Finalización
- Todos los DoD completados
- Tests pasando con cobertura ≥70%
- Aplicación funcionando localmente
- Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- Commit con mensaje: `[feature/contracts] Stage 1 foundations and auth completed with TDD`
- Registro en `workspace/status.md`

##############################################
## Mejores Prácticas de Gestión de Puertos

### Principios de Asignación de Puertos

#### 1. **Puertos Estándar por Servicio**
- **Frontend**: 3000 (desarrollo), 80/443 (producción)
- **Backend**: 8000 (desarrollo), 443 (producción)
- **Database**: 5432 (ambos ambientes)
- **Cache**: 6379 (ambos ambientes)

#### 2. **Configuración por Ambiente**
```bash
# Desarrollo: Puertos estándar
FRONTEND_PORT=3000
BACKEND_PORT=8000

# Producción: Puertos estándar web
FRONTEND_PORT=80/443
BACKEND_PORT=443
```

#### 3. **Verificación Automática**
- Scripts que verifican disponibilidad antes del inicio
- Detección automática de conflictos
- Sugerencias de puertos alternativos
- Monitoreo continuo del estado

#### 4. **Documentación Centralizada**
- Registro de todos los puertos asignados
- Documentación de cambios y migraciones
- Guías de troubleshooting
- Comandos de verificación

### Beneficios de esta Implementación

| Beneficio | Descripción |
|-----------|-------------|
| **Simplicidad** | Solo dos ambientes (dev/prod) para mantener |
| **Consistencia** | Mismos puertos en todo el equipo |
| **Flexibilidad** | Fácil cambio entre desarrollo y producción |
| **Detección Temprana** | Conflictos identificados antes del desarrollo |
| **Mantenibilidad** | Configuración centralizada y documentada |
| **Claridad** | Menos confusión entre ambientes intermedios |

### Troubleshooting Común

#### Puerto en Uso
```bash
# Identificar proceso usando puerto
lsof -i :8000

# Terminar proceso
kill -9 <PID>

# Verificar disponibilidad
./scripts/check-ports.sh
```

#### Cambio de Puerto
```bash
# Actualizar variables de entorno
export BACKEND_PORT=8001

# Reiniciar servicios
./scripts/dev.sh
```

#### Verificación de Conectividad
```bash
# Verificar backend
curl http://localhost:8000/api/v1/health

# Verificar frontend
curl http://localhost:3000
```

##############################################
## Notas de Implementación

1. **Prioridad en Simplicidad**: Mantener el código simple y bien estructurado
2. **Testing Desde el Inicio**: Implementar tests junto con funcionalidades
3. **Responsive Design**: Asegurar funcionamiento en móviles desde el inicio
4. **Seguridad Básica**: JWT, OAuth, validación de entrada, CORS apropiado
5. **Logging**: Implementar logging estructurado para debugging
6. **Error Handling**: Manejo consistente de errores en frontend y backend con mensajes amigables, logging estructurado y protección de información sensible
7. **Internacionalización**: Separar textos del código usando sistema i18n
8. **Idioma Único**: Inglés como idioma base con estructura para expansión futura
9. **Autenticación Dual**: Soportar tanto JWT como OAuth de manera coherente
10. **Gestión de Puertos**: Implementar mejores prácticas de asignación y verificación
11. **Simplicidad de Ambientes**: Mantener solo desarrollo y producción para reducir complejidad
12. **Health Checks**: Verificación continua de salud del sistema
13. **Auto-cleanup**: Limpieza automática de procesos y archivos temporales
14. **Recuperación Rápida**: Procedimientos documentados para resolver errores en <30 minutos
15. **Verificación de Versiones**: Validar versiones estables antes de desarrollo

Este stage establece las fundaciones sólidas, el sistema de autenticación completo y las mejores prácticas de gestión de recursos con una configuración simplificada de dos ambientes para el resto del proyecto.
