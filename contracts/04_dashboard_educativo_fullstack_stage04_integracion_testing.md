# Contrato Stage 4: Integración Completa, Testing y Calidad - Dashboard Educativo

## Información del Proyecto
- **Proyecto**: Dashboard Educativo
- **Fase**: Stage 4 - Integración Completa, Testing, Accesibilidad y CI/CD
- **Autor**: Sistema de Contratos LLM
- **Fecha**: 2025-09-30
- **Propósito**: Implementar integración completa con Google, testing exhaustivo, accesibilidad y CI/CD

##############################################
## Objetivos del Stage 4

### Backend - Integración Completa Google
- Implementar sincronización bidireccional con Google Classroom usando Python y HTTPS obligatorio
- Desarrollar gestión completa de estudiantes y tareas con FastAPI y validación estricta
- Crear sistema de sincronización automática y manual con manejo de errores robusto
- Implementar manejo avanzado de permisos Google con principio de menor privilegio
- Desarrollar sistema de backup y recuperación con verificación de integridad
- Crear webhooks para eventos de Google Classroom con validación de firma
- Implementar PKCE para todos los flujos OAuth 2.0
- Configurar rotación automática de refresh tokens

### Frontend - Gestión Avanzada Google
- Implementar interfaz completa de gestión Google Classroom con Next.js
- Crear herramientas de sincronización y monitoreo con React Query
- Desarrollar gestión de conflictos de datos
- Implementar importación/exportación masiva
- Crear panel de administración Google con Tailwind CSS
- Desarrollar herramientas de diagnóstico y troubleshooting

### Testing Completo
- Alcanzar cobertura ≥85% en módulos críticos, ≥70% global
- Implementar testing E2E completo con Playwright
- Crear suite de tests de performance y carga
- Desarrollar tests de accesibilidad automatizados
- Implementar testing de integración con Google API en Python
- Crear tests de regresión visual con Vitest y RTL

### Accesibilidad WCAG 2.2 AA
- Implementar navegación por teclado completa
- Crear sistema de screen reader compatible
- Desarrollar contraste y tipografía accesible
- Implementar ARIA labels y roles apropiados
- Crear modo de alto contraste
- Desarrollar soporte para tecnologías asistivas

### CI/CD Pipeline
- Configurar GitHub Actions para testing automático de Python y Next.js
- Implementar deployment automático por ambientes
- Crear pipeline de quality gates
- Desarrollar monitoreo de performance en producción
- Implementar rollback automático
- Crear sistema de feature flags

##############################################
## Metodología TDD

Este proyecto sigue la metodología Test-Driven Development (TDD), que consiste en:

1. **Escribir tests primero**: Crear tests que definan el comportamiento esperado antes de implementar el código.
2. **Verificar que los tests fallen**: Ejecutar los tests para confirmar que fallan correctamente.
3. **Implementar código mínimo**: Escribir el código necesario para que los tests pasen.
4. **Verificar que los tests pasen**: Ejecutar los tests para confirmar su éxito.
5. **Refactorizar**: Mejorar el código manteniendo los tests exitosos.

Cada componente y funcionalidad debe seguir este ciclo de desarrollo. En este Stage 4, el enfoque TDD es especialmente crítico para garantizar la robustez de la integración completa con Google y el alto nivel de calidad requerido.

##############################################
## Nuevos Componentes del Stage 4

### Backend - Integración Google Completa
```
backend/app/
├── services/
│   ├── google_sync_service.py     # Nuevo
│   ├── google_students_service.py # Nuevo
│   ├── google_assignments_service.py # Nuevo
│   ├── google_grades_service.py   # Nuevo
│   ├── sync_scheduler_service.py  # Nuevo
│   ├── conflict_resolution_service.py # Nuevo
│   └── backup_service.py          # Nuevo
├── api/
│   ├── google_sync.py             # Nuevo
│   ├── google_admin.py            # Nuevo
│   └── webhooks.py                # Nuevo
├── middleware.py                  # Expandido (permisos y sincronización)
├── models/
│   ├── sync_status.py             # Nuevo
│   └── backup.py                  # Nuevo
├── schemas.py                     # Expandido
└── utils.py                       # Expandido
```

### Frontend - Gestión Google Avanzada
```
frontend/src/
├── app/
│   ├── admin/
│   │   ├── google/
│   │   │   ├── page.tsx           # Nuevo - Panel de administración Google
│   │   │   ├── sync/
│   │   │   │   └── page.tsx       # Nuevo - Configuración de sincronización
│   │   │   ├── students/
│   │   │   │   └── page.tsx       # Nuevo - Gestión de estudiantes
│   │   │   └── assignments/
│   │   │       └── page.tsx       # Nuevo - Gestión de tareas
│   │   └── backup/
│   │       └── page.tsx           # Nuevo - Backup y recuperación
│   └── diagnostics/
│       └── page.tsx               # Nuevo - Herramientas de diagnóstico
├── components/
│   ├── google/
│   │   ├── SyncPanel.tsx          # Nuevo
│   │   ├── ConflictResolver.tsx   # Nuevo
│   │   ├── ImportExport.tsx       # Nuevo
│   │   └── PermissionsManager.tsx # Nuevo
│   └── admin/
│       ├── BackupControls.tsx     # Nuevo
│       └── DiagnosticsTools.tsx   # Nuevo
```

### Testing Infrastructure
```
/
├── tests/
│   ├── e2e/
│   │   ├── playwright.config.ts
│   │   ├── auth/
│   │   │   ├── login.spec.ts
│   │   │   ├── oauth.spec.ts
│   │   │   └── permissions.spec.ts
│   │   ├── dashboard/
│   │   │   ├── admin.spec.ts
│   │   │   ├── teacher.spec.ts
│   │   │   └── student.spec.ts
│   │   ├── google/
│   │   │   ├── sync.spec.ts
│   │   │   └── integration.spec.ts
│   │   └── accessibility/
│   │       ├── keyboard.spec.ts
│   │       └── screenreader.spec.ts
│   ├── performance/
│   │   ├── load.test.js
│   │   ├── stress.test.js
│   │   └── metrics.test.js
│   └── visual/
│       ├── snapshots/
│       └── regression.test.js
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── build.yml
│       ├── deploy.yml
│       └── accessibility.yml
└── scripts/
    ├── test-coverage.sh
    ├── lighthouse.js
    └── deploy.sh
```

### Accessibility Components
```
frontend/src/
├── components/
│   └── a11y/
│       ├── SkipLink.tsx           # Nuevo
│       ├── FocusTrap.tsx          # Nuevo
│       ├── ScreenReaderText.tsx   # Nuevo
│       └── ContrastToggle.tsx     # Nuevo
├── styles/
│   └── a11y.css                   # Nuevo
└── hooks/
    └── useA11y.ts                 # Nuevo
```

##############################################
## Funcionalidades del Stage 4

### Backend - Integración Google Completa
1. **Sincronización Bidireccional**
   - Sincronización completa de cursos, estudiantes y tareas
   - Resolución automática de conflictos
   - Detección de cambios incrementales
   - Sincronización programada y bajo demanda
   - Registro detallado de cambios

2. **Gestión Avanzada de Estudiantes**
   - Importación masiva desde Google Classroom
   - Sincronización de perfiles y fotos
   - Gestión de inscripciones y desinscripciones
   - Manejo de estudiantes inactivos

3. **Gestión Avanzada de Tareas**
   - Creación y edición de tareas en Google Classroom
   - Sincronización de fechas y plazos
   - Gestión de materiales y recursos
   - Calificación sincronizada

4. **Sistema de Backup y Recuperación**
   - Backups automáticos programados
   - Recuperación selectiva de datos
   - Exportación completa del sistema
   - Puntos de restauración

5. **Webhooks y Eventos**
   - Suscripción a eventos de Google Classroom
   - Procesamiento asíncrono de cambios
   - Notificaciones basadas en eventos
   - Auditoría de cambios

### Frontend - Gestión Google Avanzada
1. **Panel de Administración Google**
   - Dashboard de estado de sincronización
   - Configuración de parámetros de integración
   - Monitoreo de uso de API y cuotas
   - Logs de sincronización y errores

2. **Herramientas de Sincronización**
   - Control manual de sincronización
   - Programación de sincronizaciones
   - Visualización de progreso en tiempo real
   - Resolución manual de conflictos

3. **Importación/Exportación Masiva**
   - Importación masiva de estudiantes
   - Exportación de datos a Google Sheets
   - Importación de calificaciones
   - Migración entre cursos

4. **Diagnóstico y Troubleshooting**
   - Herramientas de diagnóstico de conexión
   - Validación de permisos
   - Logs detallados de errores
   - Sugerencias de resolución

### Testing Completo
1. **Testing E2E**
   - Flujos completos de usuario por rol
   - Escenarios críticos automatizados
   - Testing cross-browser
   - Simulación de condiciones adversas

2. **Testing de Performance**
   - Tests de carga con múltiples usuarios
   - Medición de tiempos de respuesta
   - Análisis de uso de recursos
   - Identificación de cuellos de botella

3. **Testing de Integración**
   - Pruebas de integración con Google API
   - Simulación de fallos de API
   - Validación de sincronización bidireccional
   - Testing de webhooks

4. **Testing Visual y de Regresión**
   - Snapshots de componentes clave
   - Comparación automática de cambios visuales
   - Testing de responsive design
   - Validación de temas y estilos

### Accesibilidad WCAG 2.2 AA
1. **Navegación por Teclado**
   - Focus visible y mejorado
   - Orden de tabulación lógico
   - Atajos de teclado
   - Trampas de foco para modales

2. **Compatibilidad con Screen Readers**
   - Textos alternativos para imágenes
   - ARIA labels y roles
   - Anuncios de cambios dinámicos
   - Landmarks semánticos

3. **Diseño Accesible**
   - Contraste de color AA/AAA
   - Tipografía escalable
   - Espaciado adecuado
   - Modo de alto contraste

4. **Soporte para Tecnologías Asistivas**
   - Compatibilidad con lectores de pantalla
   - Soporte para zoom y magnificación
   - Compatibilidad con software de dictado
   - Alternativas para interacciones complejas

### CI/CD Pipeline
1. **GitHub Actions Workflow**
   - Testing automático en cada PR
   - Build y validación de código
   - Despliegue por ambiente
   - Notificaciones de estado

2. **Quality Gates**
   - Cobertura de tests mínima
   - Validación de accesibilidad
   - Análisis estático de código
   - Performance benchmarks

3. **Deployment Automatizado**
   - Despliegue por ambiente (dev, staging, prod)
   - Estrategia de blue-green deployment
   - Rollback automático
   - Monitoreo post-despliegue

4. **Feature Flags**
   - Sistema de feature toggles
   - Despliegue gradual de características
   - A/B testing
   - Kill switches de emergencia

##############################################
## Endpoints del Stage 4

### Google Classroom Avanzado
```
GET /api/v1/google/status                    # Estado de conexión Google
GET /api/v1/google/students                    # Estudiantes de Google
POST /api/v1/google/students/import            # Importar estudiantes
PUT /api/v1/google/students/:id/sync           # Sincronizar estudiante
DELETE /api/v1/google/students/:id             # Eliminar estudiante
GET /api/v1/google/assignments                 # Tareas de Google
POST /api/v1/google/assignments/create         # Crear tarea
PUT /api/v1/google/assignments/:id             # Actualizar tarea
DELETE /api/v1/google/assignments/:id          # Eliminar tarea
```

### Sincronización y Backup
```
GET /api/v1/sync/status                      # Estado de sincronización
POST /api/v1/sync/start                      # Iniciar sincronización
POST /api/v1/sync/stop                       # Detener sincronización
GET /api/v1/sync/logs                        # Logs de sincronización
GET /api/v1/sync/conflicts                   # Listar conflictos
POST /api/v1/sync/conflicts/:id/resolve      # Resolver conflicto
GET /api/v1/backup                           # Listar backups
POST /api/v1/backup/create                   # Crear backup
POST /api/v1/backup/:id/restore              # Restaurar backup
```

### Webhooks
```
POST /api/v1/webhooks/google/course          # Webhook de curso
POST /api/v1/webhooks/google/student         # Webhook de estudiante
POST /api/v1/webhooks/google/assignment      # Webhook de tarea
GET /api/v1/webhooks/status                  # Estado de webhooks
```

### Diagnóstico y Monitoreo
```
GET /api/v1/diagnostics/google               # Diagnóstico de conexión Google
GET /api/v1/diagnostics/permissions          # Diagnóstico de permisos
GET /api/v1/monitoring/api-usage             # Uso de API
GET /api/v1/monitoring/performance           # Métricas de performance
```

##############################################
## Estructura de Datos

### Estado de Sincronización
```json
{
  "status": "in_progress",
  "lastSync": "2025-09-29T15:30:00Z",
  "nextScheduledSync": "2025-09-30T03:00:00Z",
  "progress": {
    "total": 150,
    "processed": 75,
    "succeeded": 70,
    "failed": 5,
    "percentComplete": 50
  },
  "entities": {
    "courses": {
      "total": 10,
      "synced": 10,
      "failed": 0
    },
    "students": {
      "total": 120,
      "synced": 60,
      "failed": 3
    },
    "assignments": {
      "total": 20,
      "synced": 5,
      "failed": 2
    }
  },
  "errors": [
    {
      "entity": "student",
      "id": "student-045",
      "error": "API_RATE_LIMIT_EXCEEDED",
      "timestamp": "2025-09-29T15:32:10Z"
    }
  ]
}
```

### Conflicto de Sincronización
```json
{
  "id": "conflict-001",
  "entity": "assignment",
  "entityId": "assignment-123",
  "timestamp": "2025-09-29T14:25:00Z",
  "source": {
    "system": "google_classroom",
    "data": {
      "title": "Final Project Submission",
      "dueDate": "2025-10-15T23:59:59Z",
      "maxPoints": 100
    }
  },
  "target": {
    "system": "dashboard",
    "data": {
      "title": "Final Project Submission",
      "dueDate": "2025-10-20T23:59:59Z",
      "maxPoints": 100
    }
  },
  "differences": [
    {
      "field": "dueDate",
      "sourceValue": "2025-10-15T23:59:59Z",
      "targetValue": "2025-10-20T23:59:59Z"
    }
  ],
  "resolutionOptions": [
    "use_source",
    "use_target",
    "manual"
  ],
  "status": "pending"
}
```

### Backup
```json
{
  "id": "backup-2025-09-29-15-00",
  "timestamp": "2025-09-29T15:00:00Z",
  "size": 15728640,
  "type": "full",
  "status": "completed",
  "contents": {
    "courses": 10,
    "students": 150,
    "assignments": 45,
    "submissions": 1200
  },
  "location": "s3://dashboard-backups/2025-09-29/full.zip",
  "createdBy": "system",
  "expiresAt": "2025-10-29T15:00:00Z"
}
```

##############################################
## Testing del Stage 4 con TDD

### Enfoque TDD para Backend
1. **Tests Unitarios Iniciales**
   - Escribir tests para cada servicio antes de su implementación
   - Definir comportamientos esperados mediante assertions claras
   - Crear mocks para dependencias externas
   - Enfoque especial en mocks para APIs de Google

2. **Tests de Integración Iniciales**
   - Escribir tests para flujos completos antes de implementarlos
   - Definir contratos de API mediante tests
   - Establecer casos de éxito y error esperados
   - Simular respuestas de Google API

### Backend Tests
1. **Tests Unitarios Iniciales**
   - `google_sync_service.test.py`: Tests para sincronización bidireccional antes de implementación
   - `conflict_resolution.test.py`: Tests para resolución de conflictos antes de implementación
   - `backup_service.test.py`: Tests para backup y recuperación antes de implementación
   - `webhooks.test.py`: Tests para procesamiento de webhooks antes de implementación

2. **Tests de Integración Iniciales**
   - `google_api.integration.test.py`: Tests para integración con Google API antes de implementación
   - `sync_flow.integration.test.py`: Tests para flujo completo de sincronización antes de implementación
   - `backup_restore.integration.test.py`: Tests para backup y restauración antes de implementación

3. **Tests de Performance Iniciales**
   - `sync_performance.test.py`: Tests para rendimiento de sincronización
   - `api_load.test.py`: Tests para carga de API
   - `database_performance.test.py`: Tests para rendimiento de base de datos

### Enfoque TDD para Frontend
1. **Tests de Componentes Iniciales**
   - Escribir tests para cada componente UI antes de implementarlo
   - Definir props, eventos y comportamiento esperado
   - Crear mocks para servicios y contextos
   - Enfoque en accesibilidad desde el diseño

2. **Tests E2E Iniciales**
   - Escribir tests E2E para flujos críticos antes de implementarlos
   - Definir escenarios completos de usuario
   - Establecer criterios de éxito medibles

### Frontend Tests
1. **Tests E2E Iniciales**
   - `admin_google.spec.ts`: Tests para panel de administración Google antes de implementación
   - `sync_process.spec.ts`: Tests para proceso de sincronización antes de implementación
   - `conflict_resolution.spec.ts`: Tests para resolución de conflictos antes de implementación
   - `accessibility.spec.ts`: Tests para navegación por teclado y screen reader antes de implementación

2. **Tests de Componentes Iniciales**
   - `SyncPanel.test.tsx`: Tests para panel de sincronización antes de implementación
   - `ConflictResolver.test.tsx`: Tests para resolución de conflictos antes de implementación
   - `AccessibilityComponents.test.tsx`: Tests para componentes de accesibilidad antes de implementación

3. **Tests Visuales Iniciales**
   - `dashboard_snapshots.test.tsx`: Tests para snapshots de dashboards antes de implementación
   - `high_contrast.test.tsx`: Tests para modo de alto contraste antes de implementación
   - `responsive_design.test.tsx`: Tests para diseño responsive antes de implementación

### Accessibility Tests
1. **Tests Automatizados Iniciales**
   - `keyboard_navigation.test.ts`: Tests para navegación por teclado antes de implementación
   - `screen_reader.test.ts`: Tests para compatibilidad con lectores de pantalla antes de implementación
   - `color_contrast.test.ts`: Tests para contraste de color antes de implementación
   - `aria_roles.test.ts`: Tests para roles ARIA correctos antes de implementación

2. **Tests Manuales**
   - Definir protocolos de verificación con NVDA y JAWS
   - Establecer criterios para navegación exclusiva por teclado
   - Diseñar pruebas con usuarios con discapacidades
   - Crear checklist de validación WCAG 2.2 AA

##############################################
## Criterios de Aceptación (DoD) - Stage 4

### Google Classroom Completo
- [ ] Sincronización bidireccional funcionando correctamente (extiende la integración básica del Stage 2)
- [ ] Gestión completa de estudiantes implementada (basado en la estructura de Stage 1 y 2)
- [ ] Gestión completa de tareas implementada (complementa las métricas del Stage 2 y 3)
- [ ] Sistema de backup y recuperación funcionando (asegura persistencia de datos de stages anteriores)
- [ ] Webhooks configurados y procesando eventos (integra con notificaciones del Stage 3)
- [ ] Resolución de conflictos implementada (mejora el modo dual del Stage 2)

### Testing Completo
- [ ] Cobertura de tests ≥85% en módulos críticos (mejora el 70% requerido en stages anteriores)
- [ ] Cobertura global ≥70% (consolida tests de todos los stages previos)
- [ ] Tests E2E cubriendo flujos críticos (complementa los tests unitarios del Stage 1)
- [ ] Tests de performance estableciendo líneas base (verifica optimizaciones del Stage 3)
- [ ] Tests de integración con Google API (valida la integración completa del Stage 2)
- [ ] Tests visuales y de regresión implementados (asegura consistencia visual del Stage 3)

### Accesibilidad WCAG 2.2 AA
- [ ] Navegación completa por teclado (aplica a todas las interfaces de stages anteriores)
- [ ] Compatibilidad con screen readers (mejora la experiencia de usuario del Stage 3)
- [ ] Contraste de color cumpliendo AA/AAA (refina el diseño visual del Stage 1)
- [ ] ARIA implementado correctamente (complementa los componentes del Stage 2 y 3)
- [ ] Modo de alto contraste funcionando (extiende la visualización del Stage 3)
- [ ] Validación automática de accesibilidad pasando (integra con CI/CD)

### CI/CD Pipeline
- [ ] GitHub Actions configurado y funcionando (automatiza los procesos de testing de todos los stages)
- [ ] Quality gates implementados (garantiza los criterios de calidad de stages anteriores)
- [ ] Deployment automático configurado (optimiza el proceso de despliegue del Stage 1)
- [ ] Monitoreo post-despliegue implementado (supervisa el rendimiento de features del Stage 2 y 3)
- [ ] Sistema de feature flags funcionando (permite control gradual de nuevas funcionalidades)
- [ ] Rollback automático configurado (proporciona seguridad para todas las implementaciones)

### Criterios TDD
- [ ] Tests unitarios escritos antes de la implementación de cada componente
- [ ] Tests de integración escritos antes de conectar componentes
- [ ] Tests E2E escritos antes de implementar flujos completos
- [ ] Tests de accesibilidad escritos antes de implementar componentes visuales
- [ ] Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- [ ] Documentación de decisiones de diseño basadas en tests
- [ ] Cobertura de tests cumple con el mínimo requerido (≥85% en módulos críticos, ≥70% global)

##############################################
## Configuración de Desarrollo

### Backend (.env)
```env
ENVIRONMENT=development
PORT=8000
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_API_SCOPES=https://www.googleapis.com/auth/classroom.courses,https://www.googleapis.com/auth/classroom.rosters,https://www.googleapis.com/auth/classroom.coursework.students
SYNC_SCHEDULE="0 3 * * *"
BACKUP_SCHEDULE="0 1 * * *"
BACKUP_RETENTION_DAYS=30
WEBHOOK_SECRET=your-webhook-secret
TEST_WATCH_MODE=true
TEST_COVERAGE_THRESHOLD_CRITICAL=85
TEST_COVERAGE_THRESHOLD_GLOBAL=70
TDD_CYCLE_VALIDATION=true

# OAuth Security
OAUTH_PKCE_ENABLED=true
OAUTH_STATE_SECRET=your-random-state-secret
OAUTH_REFRESH_TOKEN_ROTATION_ENABLED=true
OAUTH_REFRESH_TOKEN_EXPIRY_DAYS=15
OAUTH_ACCESS_TOKEN_EXPIRY_MINUTES=10
OAUTH_ENFORCE_HTTPS=true
OAUTH_TOKEN_BINDING=true

# Error Handling
ERROR_SANITIZE_SENSITIVE_DATA=true
ERROR_FRIENDLY_MESSAGES=true
ERROR_CATALOG_PATH=/app/config/error_messages.json
ERROR_RETRY_ATTEMPTS=3
ERROR_RETRY_BACKOFF_MS=1000
ERROR_BOUNDARY_FALLBACK_UI=true
ERROR_REPORTING_ENABLED=true
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_FEATURE_FLAGS_ENDPOINT=/api/v1/features
NEXT_PUBLIC_ENABLE_HIGH_CONTRAST=true
NEXT_PUBLIC_ACCESSIBILITY_FEATURES=true
```

### CI/CD (.github/workflows/deploy.yml)
```yaml
name: Deploy
on:
  push:
    branches: [main, staging]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: npm test
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: npm run build
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy
        run: ./scripts/deploy.sh
```

##############################################
## Flujo de Trabajo del Stage 4 con TDD

### Orden de Implementación con TDD
1. **Backend Google Completo** (7-8 días)
   - Día 1-2: Escribir tests para sincronización bidireccional
   - Día 3: Implementar sincronización para pasar tests
   - Día 4: Escribir tests para gestión avanzada de estudiantes y tareas
   - Día 5: Implementar gestión avanzada para pasar tests
   - Día 6: Escribir tests para sistema de backup y webhooks
   - Día 7-8: Implementar backup y webhooks para pasar tests y refactorizar

2. **Frontend Google Avanzado** (6-7 días)
   - Día 1: Escribir tests para panel de administración
   - Día 2: Implementar panel para pasar tests
   - Día 3: Escribir tests para herramientas de sincronización
   - Día 4: Implementar herramientas para pasar tests
   - Día 5: Escribir tests para gestión de conflictos y diagnóstico
   - Día 6-7: Implementar gestión de conflictos y diagnóstico para pasar tests

3. **Testing Infrastructure** (4-5 días)
   - Día 1: Configurar Playwright y definir escenarios E2E
   - Día 2: Escribir tests E2E para flujos críticos
   - Día 3: Escribir tests de performance y visuales
   - Día 4-5: Implementar tests de integración y refinar tests existentes

4. **Accesibilidad** (5-6 días)
   - Día 1: Escribir tests para navegación por teclado
   - Día 2: Implementar navegación por teclado para pasar tests
   - Día 3: Escribir tests para componentes accesibles y ARIA
   - Día 4: Implementar componentes accesibles para pasar tests
   - Día 5-6: Escribir tests e implementar modo de alto contraste

5. **CI/CD Pipeline** (4-5 días)
   - Día 1: Escribir tests para quality gates
   - Día 2: Configurar GitHub Actions con validación de tests
   - Día 3: Escribir tests para deployment y rollback
   - Día 4-5: Implementar scripts de deployment y feature flags

6. **Integración y Testing Final** (4-5 días)
   - Día 1: Ejecutar y refinar tests E2E completos
   - Día 2: Validar accesibilidad con herramientas automatizadas
   - Día 3: Verificar pipeline CI/CD con tests completos
   - Día 4-5: Realizar pruebas de carga y optimizar puntos críticos

### Criterios de Finalización
- Todos los DoD completados
- Tests pasando con cobertura requerida
- Aplicación accesible según WCAG 2.2 AA
- CI/CD pipeline funcionando correctamente
- Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- Commit con mensaje: `[feature/contracts] Stage 4 integration and quality completed with TDD`
- Registro en `workspace/status.md`

##############################################
## Notas de Implementación

1. **Robustez Ante Fallos**: Implementar manejo avanzado de errores y recuperación con estrategias de fallback
2. **Optimización de API**: Minimizar llamadas a Google API y respetar límites de rate con backoff exponencial
3. **Accesibilidad desde el Inicio**: Integrar accesibilidad en todos los componentes nuevos con pruebas automatizadas
4. **Testing Automatizado**: Priorizar la automatización de tests críticos con cobertura completa de casos de error
5. **Monitoreo Proactivo**: Implementar alertas para detectar problemas temprano con dashboards de error
6. **Documentación Completa**: Documentar todas las integraciones y procesos incluyendo estrategias de manejo de errores
7. **Seguridad OAuth**: Implementar PKCE, rotación de tokens, validación de estado y limitación de permisos
8. **Mensajes de Error**: Crear catálogo de mensajes de error amigables con recomendaciones de solución
9. **Protección de Datos**: Sanitizar información sensible en logs y mensajes de error
10. **TDD para Errores**: Escribir tests específicos para escenarios de error antes de implementar código
11. **Error Boundaries**: Implementar componentes de recuperación para fallos en UI con experiencia degradada
12. **Cobertura de Código**: Mantener alta cobertura de tests en módulos críticos

Este stage completa la integración con Google Classroom y eleva la calidad del sistema con testing exhaustivo, accesibilidad y CI/CD robusto. La implementación de TDD garantiza un código más mantenible, mejor documentado y con menos errores, especialmente importante en esta fase final donde se integran todos los componentes del sistema.
