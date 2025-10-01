# Contrato Stage 2: Integración Google y Dashboards Básicos - Dashboard Educativo

## Información del Proyecto
- **Proyecto**: Dashboard Educativo
- **Fase**: Stage 2 - Integración Google Classroom y Dashboards Básicos
- **Autor**: Sistema de Contratos LLM
- **Fecha**: 2025-09-30
- **Propósito**: Implementar conexión con Google Classroom API y dashboards básicos por rol

##############################################
## Objetivos del Stage 2

### Backend - Integración Google
- Crear GoogleService para interactuar con Classroom API
- Configurar modo dual (Google/Mock) dinámico
- Implementar sincronización básica de cursos
- Configurar rate limiting para API de Google
- Desarrollar endpoints para datos de cursos y estudiantes

### Backend - Métricas Básicas
- Implementar servicios de métricas básicas con Python y FastAPI
- Crear endpoints para datos de dashboard
- Desarrollar agregaciones de datos educativos simples
- Implementar caché básico para consultas frecuentes
- Generar métricas esenciales por rol

### Frontend - Google Classroom
- Crear componentes para selección de modo (Google/Mock) con Tailwind CSS
- Manejar estados de conexión Google
- Crear interfaz para gestión de conexión Google
- Mostrar información de cuenta Google conectada
- Implementar lista de cursos de Google Classroom
- Configurar health checks para conexión Google
- Implementar auto-cleanup de sesiones Google

### Frontend - Dashboards Básicos
- Implementar dashboards básicos por rol (admin, coordinador, docente, estudiante)
- Integrar ApexCharts para visualizaciones básicas con Next.js y Tailwind CSS
- Crear componentes de métricas reutilizables
- Implementar filtros básicos con React Query
- Desarrollar widgets esenciales

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
## Nuevos Componentes del Stage 2

### Backend - Nuevos Archivos
```
backend/app/
├── services/
│   ├── google_service.py          # Nuevo
│   ├── classroom_service.py       # Nuevo
│   └── metrics_service.py         # Nuevo
├── api/endpoints/
│   ├── courses.py                 # Nuevo
│   ├── students.py                # Nuevo
│   └── dashboard.py               # Nuevo
├── middleware/
│   ├── google_auth_middleware.py  # Nuevo
│   └── rate_limit_middleware.py   # Nuevo
├── models/
│   ├── course.py                  # Nuevo
│   ├── student.py                 # Nuevo
│   └── metric.py                  # Nuevo
├── schemas/
│   ├── course_schema.py           # Nuevo
│   ├── student_schema.py          # Nuevo
│   └── metric_schema.py           # Nuevo
├── utils/
│   ├── google_helper.py           # Nuevo
│   ├── cache_helper.py            # Nuevo
│   └── metrics_helper.py          # Nuevo
└── data/
    ├── mock_courses.json          # Nuevo
    └── mock_students.json         # Nuevo
```

### Frontend - Nuevos Archivos
```
frontend/src/
├── app/
│   ├── dashboard/
│   │   ├── admin/
│   │   │   └── page.tsx           # Nuevo - Dashboard admin
│   │   ├── coordinator/
│   │   │   └── page.tsx           # Nuevo - Dashboard coordinador
│   │   ├── teacher/
│   │   │   └── page.tsx           # Nuevo - Dashboard docente
│   │   └── student/
│   │       └── page.tsx           # Nuevo - Dashboard estudiante
│   ├── courses/
│   │   ├── page.tsx               # Nuevo - Lista de cursos
│   │   └── [id]/
│   │       └── page.tsx           # Nuevo - Detalle de curso
│   └── settings/
│       └── google/
│           └── page.tsx           # Nuevo - Configuración Google
├── components/
│   ├── google/
│   │   ├── GoogleConnect.tsx      # Nuevo
│   │   ├── CourseList.tsx         # Nuevo
│   │   └── ModeSelector.tsx       # Nuevo
│   ├── dashboard/
│   │   ├── MetricCard.tsx         # Nuevo
│   │   ├── ChartWidget.tsx        # Nuevo
│   │   ├── CourseMetrics.tsx      # Nuevo
│   │   └── StudentProgress.tsx    # Nuevo
│   └── charts/
│       ├── BarChart.tsx           # Nuevo
│       ├── LineChart.tsx          # Nuevo
│       └── PieChart.tsx           # Nuevo
├── lib/
│   ├── google.ts                  # Nuevo
│   ├── metrics.ts                 # Nuevo
│   └── charts.ts                  # Nuevo
├── hooks/
│   ├── useGoogleClassroom.ts      # Nuevo
│   ├── useMetrics.ts              # Nuevo
│   └── useCharts.ts               # Nuevo
└── types/
    ├── google.types.ts            # Nuevo
    ├── course.types.ts            # Nuevo
    └── metrics.types.ts           # Nuevo
```

##############################################
## Funcionalidades del Stage 2

### Backend - Integración Google Classroom
1. **Google Classroom API**
   - Conexión completa con API de Google usando HTTPS obligatorio
   - Manejo de tokens y permisos con rotación segura y limitación de scopes
   - Sincronización de cursos y estudiantes con validación de datos
   - Manejo de errores estructurado con mensajes amigables y logging seguro
   - Implementación de rate limiting con backoff exponencial
   - Modo dual (Google/Mock) configurable con transición transparente

2. **Gestión de Cursos**
   - Listado de cursos de Google Classroom
   - Detalles de curso con información básica
   - Listado de estudiantes por curso
   - Métricas básicas por curso
   - Sincronización bajo demanda
   - Health checks para integridad de datos
   - Auto-cleanup de datos corruptos

3. **Métricas Básicas**
   - Cálculo de KPIs educativos esenciales
   - Agregaciones por curso, módulo, estudiante
   - Métricas de rendimiento y progreso
   - Comparativas temporales simples
   - Caché básico para consultas frecuentes

### Frontend - Dashboards por Rol
1. **Dashboard Administrador**
   - Vista general del sistema
   - Métricas de todos los cursos
   - Análisis de rendimiento global básico
   - Gestión de usuarios y permisos

2. **Dashboard Coordinador**
   - Métricas de cursos asignados
   - Seguimiento de docentes
   - Análisis de progreso por programa
   - Reportes básicos

3. **Dashboard Docente**
   - Métricas de sus cursos
   - Progreso de estudiantes
   - Estado de tareas y entregas
   - Herramientas de seguimiento básicas

4. **Dashboard Estudiante**
   - Progreso personal
   - Tareas pendientes y completadas
   - Comparativas simples
   - Metas y objetivos

### Frontend - Componentes Google
1. **Selector de Modo**
   - Cambio entre modo Google y Mock
   - Indicador de estado de conexión
   - Configuración de preferencias

2. **Gestión de Conexión Google**
   - Estado de conexión
   - Información de cuenta conectada
   - Opciones de desconexión
   - Permisos otorgados

3. **Visualización de Cursos**
   - Lista de cursos de Google Classroom
   - Detalles básicos de curso
   - Navegación a dashboard de curso
   - Filtros básicos

##############################################
## Endpoints del Stage 2

### Google Classroom API
```
GET /api/v1/google/status                     # Estado de conexión Google
GET /api/v1/google/courses                    # Cursos de Google
GET /api/v1/google/courses/:id                # Detalle de curso
GET /api/v1/google/courses/:id/students       # Estudiantes de curso
POST /api/v1/google/sync/courses              # Sincronizar cursos
```

### Métricas y Dashboards
```
GET /api/v1/metrics/overview                  # Métricas generales
GET /api/v1/metrics/courses/:id               # Métricas de curso
GET /api/v1/metrics/students/:id              # Métricas de estudiante
GET /api/v1/dashboard/admin                   # Dashboard admin
GET /api/v1/dashboard/coordinator             # Dashboard coordinador
GET /api/v1/dashboard/teacher                 # Dashboard docente
GET /api/v1/dashboard/student                 # Dashboard estudiante
```

##############################################
## Estructura de Datos

### Curso de Google Classroom
```json
{
  "id": "123456789",
  "name": "eCommerce Specialist",
  "section": "Section A",
  "description": "Complete eCommerce course",
  "room": "Virtual Room 1",
  "ownerId": "teacher-001",
  "creationTime": "2025-08-15T10:00:00Z",
  "updateTime": "2025-09-20T15:30:00Z",
  "enrollmentCode": "abc123",
  "courseState": "ACTIVE",
  "alternateLink": "https://classroom.google.com/c/123456789",
  "teacherGroupEmail": "teachers-123456789@googlegroups.com",
  "courseGroupEmail": "class-123456789@googlegroups.com",
  "guardiansEnabled": false,
  "calendarId": "calendar-id-123456789"
}
```

### Métricas de Curso
```json
{
  "courseId": "123456789",
  "courseName": "eCommerce Specialist",
  "metrics": {
    "totalStudents": 150,
    "activeStudents": 142,
    "completionRate": 78.5,
    "averageGrade": 8.2,
    "assignmentsTotal": 45,
    "assignmentsCompleted": 38,
    "engagementScore": 85.3
  },
  "trends": {
    "weekly": {
      "submissions": [45, 50, 48, 52, 55],
      "grades": [7.8, 8.0, 8.1, 8.2, 8.3]
    }
  }
}
```

### Métricas de Estudiante
```json
{
  "studentId": "student-001",
  "studentName": "Ana Martinez",
  "metrics": {
    "coursesEnrolled": 2,
    "coursesCompleted": 1,
    "overallProgress": 67.5,
    "averageGrade": 8.7,
    "assignmentsCompleted": 28,
    "assignmentsPending": 12,
    "streakDays": 15
  },
  "courseProgress": [
    {
      "courseId": "123456789",
      "courseName": "eCommerce Specialist",
      "progress": 85.0,
      "grade": 8.9,
      "status": "active"
    }
  ]
}
```

##############################################
## Testing del Stage 2 con TDD

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
   - `google_service.test.py`: Tests para conexión con Google Classroom API antes de implementación
   - `classroom_service.test.py`: Tests para gestión de cursos y estudiantes antes de implementación
   - `metrics_service.test.py`: Tests para cálculo de métricas antes de implementación

2. **Tests de Integración Iniciales**
   - `google_integration.test.py`: Tests para endpoints de Google antes de implementación
   - `dashboard_integration.test.py`: Tests para endpoints de dashboard antes de implementación
   - `metrics_integration.test.py`: Tests para endpoints de métricas antes de implementación

3. **Tests de Mock**
   - `google_mock.test.py`: Tests para modo Mock de Google Classroom antes de implementación
   - `metrics_mock.test.py`: Tests para métricas con datos mock antes de implementación

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
   - `GoogleConnect.test.tsx`: Tests para componente de conexión Google antes de implementación
   - `ModeSelector.test.tsx`: Tests para selector de modo antes de implementación
   - `MetricCard.test.tsx`: Tests para tarjetas de métricas antes de implementación
   - `ChartWidget.test.tsx`: Tests para widgets de gráficos antes de implementación

2. **Tests de Hooks Iniciales**
   - `useGoogleClassroom.test.ts`: Tests para hook de Google Classroom antes de implementación
   - `useMetrics.test.ts`: Tests para hook de métricas antes de implementación

##############################################
## Criterios de Aceptación (DoD) - Stage 2

### Backend Google
- [ ] Conexión con Google Classroom API funcionando
- [ ] Sincronización de cursos implementada
- [ ] Modo dual (Google/Mock) funcionando
- [ ] Rate limiting configurado
- [ ] Manejo de errores de API implementado con sanitización y categorización
- [ ] Tests de integración con Google pasando
- [ ] Health checks para conexión Google implementados
- [ ] Auto-cleanup de sesiones Google funcionando
- [ ] Recuperación rápida ante fallos de API

### Backend Métricas
- [ ] Servicio de métricas calculando KPIs correctamente
- [ ] Endpoints de dashboard respondiendo por rol
- [ ] Agregaciones de datos funcionando
- [ ] Caché básico implementado
- [ ] Tests de métricas con cobertura ≥70%

### Frontend Google
- [ ] Selector de modo (Google/Mock) funcionando
- [ ] Interfaz de conexión Google implementada
- [ ] Lista de cursos de Google mostrándose correctamente
- [ ] Navegación entre cursos funcionando
- [ ] Manejo de errores de conexión implementado con mensajes amigables y reintentos
- [ ] Health checks visuales para estado de conexión Google
- [ ] Auto-cleanup de datos corruptos en interfaz
- [ ] Recuperación rápida ante fallos de conexión

### Frontend Dashboards
- [ ] Dashboard admin con métricas globales
- [ ] Dashboard coordinador con métricas de programa
- [ ] Dashboard docente con métricas de curso
- [ ] Dashboard estudiante con progreso personal
- [ ] ApexCharts integrado y funcionando
- [ ] Componentes de métricas reutilizables
- [ ] Filtros básicos funcionando
- [ ] Responsive design en todos los dashboards

### Criterios TDD
- [ ] Tests unitarios escritos antes de la implementación de cada componente
- [ ] Tests de integración escritos antes de conectar componentes
- [ ] Tests de infraestructura implementados
- [ ] Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- [ ] Documentación de decisiones de diseño basadas en tests
- [ ] Cobertura de tests cumple con el mínimo requerido (≥75%)
- [ ] Tests de health checks implementados
- [ ] Tests de auto-cleanup implementados

##############################################
## Configuración de Desarrollo

### Backend (.env)
```env
ENVIRONMENT=development
PORT=8000
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_API_SCOPES=https://www.googleapis.com/auth/classroom.courses,https://www.googleapis.com/auth/classroom.rosters,https://www.googleapis.com/auth/classroom.coursework.students
GOOGLE_API_RATE_LIMIT=100
OAUTH_PKCE_ENABLED=true
OAUTH_STATE_SECRET=your-random-state-secret
OAUTH_REFRESH_TOKEN_ROTATION_ENABLED=true
OAUTH_REFRESH_TOKEN_EXPIRY_DAYS=30
OAUTH_ACCESS_TOKEN_EXPIRY_MINUTES=15
OAUTH_ENFORCE_HTTPS=true

# Error Handling
ERROR_SANITIZE_SENSITIVE_DATA=true
ERROR_FRIENDLY_MESSAGES=true
ERROR_RETRY_ATTEMPTS=3
ERROR_RETRY_BACKOFF_MS=1000
CACHE_TTL=300
DEFAULT_MODE=MOCK
TEST_WATCH_MODE=true
TEST_COVERAGE_THRESHOLD=70
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
NEXT_PUBLIC_DEFAULT_MODE=MOCK
```

##############################################
## Flujo de Trabajo del Stage 2

### Orden de Implementación con TDD
1. **Backend Google** (4-5 días)
   - Día 1: Escribir tests para conexión con Google Classroom API
   - Día 2: Implementar conexión con Google API para pasar tests
   - Día 3: Escribir tests para endpoints de cursos y estudiantes
   - Día 4: Implementar endpoints y modo dual para pasar tests
   - Día 5: Refactorizar y optimizar

2. **Backend Métricas** (4-5 días)
   - Día 1: Escribir tests para servicio de métricas básicas
   - Día 2: Implementar servicio de métricas para pasar tests
   - Día 3: Escribir tests para endpoints de dashboard por rol
   - Día 4: Implementar endpoints y caché básico
   - Día 5: Refactorizar y optimizar

3. **Frontend Google** (3-4 días)
   - Día 1: Escribir tests para selector de modo y componentes de conexión
   - Día 2: Implementar selector de modo y componentes para pasar tests
   - Día 3: Escribir tests para lista de cursos
   - Día 4: Implementar lista de cursos y refactorizar

4. **Frontend Dashboards** (5-6 días)
   - Día 1: Escribir tests para componentes de métricas y gráficos
   - Día 2: Implementar componentes base para pasar tests
   - Día 3: Escribir tests para dashboards por rol
   - Día 4-5: Implementar dashboards por rol para pasar tests
   - Día 6: Refactorizar e integrar ApexCharts

5. **Integración y Testing Final** (3-4 días)
   - Día 1: Escribir tests end-to-end para flujos completos
   - Día 2: Conectar frontend con backend para pasar tests
   - Día 3-4: Refinamiento de UX y optimización

### Criterios de Finalización
- Todos los DoD completados
- Tests pasando con cobertura ≥70%
- Aplicación funcionando en ambos modos (Google/Mock)
- Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- Commit con mensaje: `[feature/contracts] Stage 2 google and dashboards completed with TDD`
- Registro en `workspace/status.md`

##############################################
## Notas de Implementación

1. **Modo Dual**: Asegurar que el sistema funcione tanto con Google Classroom como con datos mock
2. **Manejo de Errores**: Implementar manejo robusto de errores de API de Google con tipado, mensajes amigables, protección de información sensible y estrategias de recuperación
3. **Performance**: Optimizar consultas a Google Classroom API
4. **Caché Inteligente**: Implementar caché para reducir llamadas a API
5. **Responsive Design**: Asegurar que todos los dashboards funcionen en móviles
6. **Componentes Reutilizables**: Diseñar componentes de métricas y gráficos reutilizables
7. **Testing Completo**: Cubrir tanto modo Google como modo Mock en tests
8. **Enfoque TDD**: Seguir estrictamente el ciclo de desarrollo TDD para todos los componentes
9. **Documentación de Tests**: Documentar las decisiones de diseño basadas en los tests
10. **Health Checks**: Verificación continua de salud de conexiones Google
11. **Auto-cleanup**: Limpieza automática de sesiones y datos corruptos
12. **Recuperación Rápida**: Procedimientos para resolver fallos de API en <30 minutos

Este stage establece la conexión con Google Classroom y los dashboards básicos por rol, sentando las bases para visualizaciones más avanzadas en etapas posteriores.
