# Contrato Stage 3: Visualización Avanzada y Notificaciones - Dashboard Educativo

## Información del Proyecto
- **Proyecto**: Dashboard Educativo
- **Fase**: Stage 3 - Visualización Avanzada, Búsqueda y Notificaciones
- **Autor**: Sistema de Contratos LLM
- **Fecha**: 2025-09-30
- **Propósito**: Implementar visualizaciones avanzadas, búsqueda de estudiantes y sistema de notificaciones

##############################################
## Objetivos del Stage 3

### Backend - Métricas y Analytics Avanzados
- Implementar servicios avanzados de métricas y estadísticas
- Desarrollar agregaciones complejas de datos educativos con pandas y NumPy
- Implementar caché avanzado para consultas pesadas
- Crear sistema de filtros y segmentación sofisticado
- Generar reportes detallados en tiempo real

### Backend - Sistema de Búsqueda
- Implementar búsqueda avanzada de estudiantes
- Crear índices optimizados para búsqueda
- Desarrollar filtros contextuales por rol
- Implementar búsqueda por múltiples criterios
- Optimizar rendimiento de consultas de búsqueda

### Backend - Sistema de Notificaciones
- Implementar sistema de notificaciones en tiempo real con FastAPI y WebSockets seguros (wss://)
- Crear servicio de alertas inteligentes en Python con manejo de errores tipado
- Integrar notificaciones Telegram (mock) con reintentos y manejo de fallos
- Desarrollar sistema de eventos y triggers con validación de datos
- Implementar notificaciones por email (mock) con plantillas seguras
- Crear sistema de preferencias de notificación con validación estricta
- Implementar mecanismos de recuperación ante fallos de conexión

### Frontend - Visualización Avanzada
- Implementar gráficos interactivos avanzados con React y Tailwind CSS
- Crear sistema de notificaciones en tiempo real con React Query
- Desarrollar widgets personalizables
- Implementar drill-down y navegación contextual
- Crear dashboards avanzados por rol
- Desarrollar sistema de alertas visuales

### Frontend - Búsqueda de Estudiantes
- Implementar interfaz de búsqueda avanzada
- Crear componentes de resultados de búsqueda
- Desarrollar filtros dinámicos para búsqueda
- Implementar vista detallada de estudiante
- Crear experiencia de búsqueda contextual por rol

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
## Nuevos Componentes del Stage 3

### Backend - Nuevos Archivos
```
backend/app/
├── services/
│   ├── insights.py                # Expandido (métricas avanzadas)
│   ├── search_service.py          # Nuevo
│   ├── notification_service.py    # Nuevo
│   ├── websocket_service.py       # Nuevo
│   ├── alert_service.py           # Nuevo
│   └── event_service.py           # Nuevo
├── api/
│   ├── insights.py                # Expandido
│   ├── search.py                  # Nuevo
│   ├── notifications.py           # Nuevo
│   └── websocket.py               # Nuevo
├── middleware.py                  # Expandido (websocket y notificaciones)
├── models/
│   ├── insights.py                # Expandido
│   ├── search.py                  # Nuevo
│   └── notification.py            # Nuevo
├── schemas.py                     # Expandido
└── utils.py                       # Expandido
```

### Frontend - Nuevos Archivos
```
frontend/src/
├── app/
│   ├── dashboard/
│   │   ├── [role]/                # Expandido - Dashboards avanzados
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   ├── search/
│   │   ├── page.tsx               # Nuevo - Búsqueda principal
│   │   └── [id]/
│   │       └── page.tsx           # Nuevo - Detalle de estudiante
│   ├── notifications/
│   │   └── page.tsx               # Nuevo - Centro de notificaciones
│   └── preferences/
│       └── notifications/
│           └── page.tsx           # Nuevo - Preferencias de notificaciones
├── components/
│   ├── widgets.tsx                # Expandido - Widgets avanzados
│   ├── charts.tsx                 # Expandido - Gráficos avanzados
│   ├── search/
│   │   ├── SearchBar.tsx          # Nuevo
│   │   ├── SearchResults.tsx      # Nuevo
│   │   └── StudentDetail.tsx      # Nuevo
│   ├── notifications/
│   │   ├── NotificationCenter.tsx # Nuevo
│   │   ├── NotificationBadge.tsx  # Nuevo
│   │   └── AlertBanner.tsx        # Nuevo
│   └── filters/
│       └── AdvancedFilters.tsx    # Nuevo
├── lib/
│   ├── utils.ts                   # Expandido
│   ├── search.ts                  # Nuevo
│   └── notifications.ts           # Nuevo
├── hooks.ts                       # Expandido (useSearch, useNotifications)
└── types.ts                       # Expandido
```

##############################################
## Funcionalidades del Stage 3

### Backend - Métricas y Analytics Avanzados
1. **Servicio de Insights Avanzados**
   - Análisis predictivo básico
   - Detección de patrones de rendimiento
   - Correlaciones entre variables educativas
   - Segmentación avanzada de estudiantes
   - Métricas comparativas entre períodos

2. **Sistema de Reportes Avanzados**
   - Reportes personalizables
   - Exportación en múltiples formatos
   - Programación de reportes periódicos
   - Reportes contextuales por rol
   - Visualizaciones embebidas en reportes

3. **Caché Optimizado**
   - Estrategias de caché avanzadas
   - Invalidación selectiva
   - Precarga de datos frecuentes
   - Caché por usuario y rol
   - Optimización de memoria

### Backend - Sistema de Búsqueda
1. **Búsqueda de Estudiantes**
   - Búsqueda por nombre, ID y curso
   - Filtros por estado y rendimiento
   - Resultados optimizados con indexación
   - Acceso contextual según rol
   - Búsqueda de texto completo

2. **Filtros Avanzados**
   - Filtrado por múltiples criterios
   - Filtros anidados y combinados
   - Guardado de filtros favoritos
   - Filtros contextuales por rol
   - Historial de búsquedas recientes

### Backend - Sistema de Notificaciones
1. **Notificaciones en Tiempo Real**
   - WebSockets para actualizaciones instantáneas
   - Cola de notificaciones
   - Priorización de notificaciones
   - Entrega garantizada
   - Estado de lectura y confirmación

2. **Alertas Inteligentes**
   - Detección de estudiantes en riesgo
   - Alertas de plazos próximos
   - Notificaciones de cambios importantes
   - Alertas de rendimiento anómalo
   - Recordatorios personalizados

3. **Canales de Notificación**
   - Notificaciones en aplicación
   - Notificaciones por email (mock)
   - Notificaciones Telegram (mock)
   - Preferencias por usuario
   - Horarios configurables

### Frontend - Visualización Avanzada
1. **Gráficos Interactivos**
   - Drill-down en gráficos
   - Tooltips enriquecidos
   - Animaciones y transiciones
   - Comparativas y superposiciones
   - Exportación de visualizaciones

2. **Dashboards Avanzados por Rol**
   - **Dashboard Administrador**
     - Vista general del sistema con KPIs avanzados
     - Análisis de tendencias institucionales
     - Comparativas entre programas
     - Métricas de uso del sistema
     - Búsqueda global de estudiantes

   - **Dashboard Coordinador**
     - Análisis de rendimiento por programa
     - Métricas comparativas entre docentes
     - Seguimiento de cohortes
     - Predicción de resultados
     - Búsqueda de estudiantes por programa

   - **Dashboard Docente**
     - Análisis detallado de rendimiento de curso
     - Identificación de estudiantes en riesgo
     - Patrones de entrega y participación
     - Recomendaciones de intervención
     - Búsqueda de estudiantes por curso

   - **Dashboard Estudiante**
     - Análisis personalizado de progreso
     - Recomendaciones de estudio
     - Comparativas anónimas con compañeros
     - Proyección de resultados
     - Calendario de entregas

3. **Widgets Personalizables**
   - Arrastrar y soltar widgets
   - Configuración de parámetros
   - Guardado de configuraciones
   - Compartir dashboards
   - Temas visuales

### Frontend - Búsqueda y Notificaciones
1. **Interfaz de Búsqueda**
   - Barra de búsqueda omnipresente
   - Resultados instantáneos
   - Filtros contextuales
   - Vista detallada de estudiante
   - Acciones rápidas desde resultados

2. **Centro de Notificaciones**
   - Bandeja de notificaciones
   - Filtros por tipo y prioridad
   - Marcado como leído/no leído
   - Acciones desde notificaciones
   - Historial completo

3. **Alertas Visuales**
   - Indicadores de estado
   - Banners de alertas importantes
   - Notificaciones toast
   - Badges de contador
   - Alertas contextuales

##############################################
## Endpoints del Stage 3

### Insights y Métricas Avanzadas
```
GET /api/v1/insights/metrics                    # Métricas generales
GET /api/v1/insights/entity/:type/:id           # Métricas por entidad
GET /api/v1/insights/trends                     # Tendencias y análisis
GET /api/v1/insights/engagement                 # Métricas de engagement
GET /api/v1/insights/predictions                # Predicciones básicas
```

### Búsqueda
```
GET /api/v1/search/:entity                      # Búsqueda genérica por entidad
GET /api/v1/entity/:type/:id                    # Detalles de entidad
GET /api/v1/search/filters                      # Obtener filtros disponibles
POST /api/v1/search/save                        # Guardar búsqueda
```

### Notificaciones
```
GET /api/v1/notifications                       # Obtener notificaciones
PUT /api/v1/notifications/:id/read              # Marcar como leída
GET /api/v1/notifications/preferences           # Obtener preferencias
PUT /api/v1/notifications/preferences           # Actualizar preferencias
WS /api/v1/ws/notifications                     # WebSocket de notificaciones
```

### Reportes
```
GET /api/v1/reports/generate                    # Generar reporte
GET /api/v1/reports/export/:id                  # Exportar reporte
POST /api/v1/reports/schedule                   # Programar reporte
```

##############################################
## Estructura de Datos

### Notificación
```json
{
  "id": "notif-001",
  "userId": "teacher-001",
  "type": "alert",
  "priority": "high",
  "title": "Student at Risk",
  "message": "John Smith has missed 3 consecutive assignments",
  "data": {
    "studentId": "student-045",
    "courseId": "course-001",
    "assignmentsMissed": 3
  },
  "read": false,
  "createdAt": "2025-09-28T14:30:00Z",
  "expiresAt": "2025-10-05T14:30:00Z",
  "actions": [
    {
      "label": "View Student",
      "url": "/students/student-045"
    },
    {
      "label": "Send Message",
      "action": "sendMessage"
    }
  ]
}
```

### Resultado de Búsqueda
```json
{
  "query": "Smith",
  "entityType": "student",
  "totalResults": 15,
  "page": 1,
  "pageSize": 10,
  "results": [
    {
      "id": "student-045",
      "name": "John Smith",
      "email": "john.smith@example.com",
      "courseId": "course-001",
      "courseName": "eCommerce Specialist",
      "status": "at_risk",
      "progress": 45.5,
      "lastActive": "2025-09-25T10:15:00Z",
      "highlights": {
        "name": ["John <em>Smith</em>"]
      }
    },
    // More results...
  ],
  "filters": {
    "applied": {
      "courseId": "course-001",
      "status": "at_risk"
    },
    "available": {
      "status": ["active", "at_risk", "inactive"],
      "courseId": ["course-001", "course-002"]
    }
  }
}
```

### Preferencias de Notificaciones
```json
{
  "userId": "teacher-001",
  "channels": {
    "inApp": true,
    "email": true,
    "telegram": false
  },
  "types": {
    "assignment": true,
    "studentRisk": true,
    "announcement": true,
    "grade": false
  },
  "schedule": {
    "quietHours": {
      "enabled": true,
      "start": "22:00",
      "end": "08:00"
    },
    "digest": {
      "enabled": true,
      "frequency": "daily",
      "time": "18:00"
    }
  }
}
```

##############################################
## Testing del Stage 3 con TDD

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
   - `insights.test.ts`: Tests para métricas y analytics avanzados antes de implementación
   - `search.test.ts`: Tests para sistema de búsqueda antes de implementación
   - `notifications.test.ts`: Tests para sistema de notificaciones antes de implementación
   - `websocket.test.ts`: Tests para comunicación WebSocket antes de implementación

2. **Tests de Integración Iniciales**
   - `insights.integration.test.ts`: Tests para endpoints de insights antes de implementación
   - `search.integration.test.ts`: Tests para búsqueda y filtros antes de implementación
   - `notifications.integration.test.ts`: Tests para sistema completo de notificaciones antes de implementación

3. **Tests de Performance Iniciales**
   - `search.performance.test.ts`: Tests para rendimiento de búsquedas
   - `websocket.performance.test.ts`: Tests para rendimiento de WebSockets
   - `cache.performance.test.ts`: Tests para efectividad del caché avanzado

### Enfoque TDD para Frontend
1. **Tests de Componentes Iniciales**
   - Escribir tests para cada componente UI antes de implementarlo
   - Definir props, eventos y comportamiento esperado
   - Crear mocks para servicios y contextos

2. **Tests de Integración Iniciales**
   - Escribir tests para flujos completos antes de implementarlos
   - Definir comportamiento esperado para interacciones complejas
   - Simular eventos y cambios de estado en flujos completos

### Frontend Tests
1. **Tests de Componentes Iniciales**
   - `SearchBar.test.tsx`: Tests para barra de búsqueda antes de implementación
   - `NotificationCenter.test.tsx`: Tests para centro de notificaciones antes de implementación
   - `AdvancedCharts.test.tsx`: Tests para gráficos avanzados antes de implementación
   - `StudentDetail.test.tsx`: Tests para vista detallada de estudiante antes de implementación

2. **Tests de Integración Iniciales**
   - `SearchFlow.test.tsx`: Tests para flujo completo de búsqueda antes de implementación
   - `NotificationFlow.test.tsx`: Tests para flujo de notificaciones antes de implementación
   - `DashboardInteraction.test.tsx`: Tests para interacciones en dashboards antes de implementación

##############################################
## Criterios de Aceptación (DoD) - Stage 3

### Backend Avanzado
- [ ] Servicios de insights avanzados funcionando correctamente
- [ ] Sistema de búsqueda optimizado implementado
- [ ] Sistema de notificaciones en tiempo real funcionando
- [ ] WebSockets configurados y funcionando
- [ ] Caché avanzado optimizando consultas
- [ ] Endpoints respondiendo correctamente
- [ ] Tests con cobertura ≥75%
- [ ] Performance optimizada para grandes volúmenes de datos

### Frontend Avanzado
- [ ] Visualizaciones interactivas avanzadas implementadas
- [ ] Sistema de búsqueda integrado en dashboards
- [ ] Centro de notificaciones funcionando
- [ ] Alertas visuales implementadas
- [ ] Dashboards avanzados por rol
- [ ] Widgets personalizables funcionando
- [ ] Drill-down y navegación contextual
- [ ] Responsive design en todas las nuevas funcionalidades

### Experiencia de Usuario
- [ ] Notificaciones entregadas en tiempo real
- [ ] Búsquedas respondiendo en <500ms
- [ ] Interactividad fluida en gráficos
- [ ] Transiciones y animaciones optimizadas
- [ ] Feedback visual para todas las acciones
- [ ] Experiencia consistente en todos los roles

### Criterios TDD
- [ ] Tests unitarios escritos antes de la implementación de cada componente
- [ ] Tests de integración escritos antes de conectar componentes
- [ ] Tests de performance definidos antes de optimizaciones
- [ ] Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- [ ] Documentación de decisiones de diseño basadas en tests
- [ ] Cobertura de tests cumple con el mínimo requerido (≥75%)

##############################################
## Configuración de Desarrollo

### Backend (.env)
```env
ENVIRONMENT=development
PORT=8000
WEBSOCKET_PORT=8001
CACHE_STRATEGY=advanced
CACHE_TTL=600
SEARCH_INDEX_UPDATE_INTERVAL=60
NOTIFICATION_RETENTION_DAYS=30
EMAIL_MOCK=true
TELEGRAM_MOCK=true
TEST_WATCH_MODE=true
TEST_COVERAGE_THRESHOLD=75
TDD_CYCLE_VALIDATION=true

# OAuth y Seguridad
OAUTH_PKCE_ENABLED=true
OAUTH_STATE_SECRET=your-random-state-secret
OAUTH_REFRESH_TOKEN_ROTATION_ENABLED=true
OAUTH_REFRESH_TOKEN_EXPIRY_DAYS=30
OAUTH_ACCESS_TOKEN_EXPIRY_MINUTES=15
OAUTH_ENFORCE_HTTPS=true
WEBSOCKET_SECURE=true

# Error Handling
ERROR_SANITIZE_SENSITIVE_DATA=true
ERROR_FRIENDLY_MESSAGES=true
ERROR_RETRY_ATTEMPTS=3
ERROR_RETRY_BACKOFF_MS=1000
ERROR_BOUNDARY_FALLBACK_UI=true
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_WS_URL=ws://localhost:8001/api/v1/ws
NEXT_PUBLIC_SEARCH_DEBOUNCE_MS=300
NEXT_PUBLIC_NOTIFICATION_POLL_INTERVAL=30000
```

##############################################
## Flujo de Trabajo del Stage 3

### Orden de Implementación con TDD
1. **Backend Insights Avanzados** (4-5 días)
   - Día 1: Escribir tests para servicios de métricas avanzadas
   - Día 2: Implementar servicios básicos para pasar tests
   - Día 3: Escribir tests para análisis avanzados y caché
   - Día 4: Implementar análisis y caché para pasar tests
   - Día 5: Refactorizar y optimizar rendimiento

2. **Backend Búsqueda** (3-4 días)
   - Día 1: Escribir tests para sistema de búsqueda e índices
   - Día 2: Implementar sistema básico para pasar tests
   - Día 3: Escribir tests para filtros avanzados
   - Día 4: Implementar filtros y optimizaciones para pasar tests

3. **Backend Notificaciones** (4-5 días)
   - Día 1: Escribir tests para WebSockets y sistema de notificaciones
   - Día 2: Implementar WebSockets básicos para pasar tests
   - Día 3: Escribir tests para alertas inteligentes y canales
   - Día 4: Implementar alertas y canales para pasar tests
   - Día 5: Refactorizar y optimizar

4. **Frontend Visualizaciones** (5-6 días)
   - Día 1: Escribir tests para componentes de gráficos avanzados
   - Día 2: Implementar componentes básicos para pasar tests
   - Día 3: Escribir tests para drill-down y navegación
   - Día 4: Implementar drill-down para pasar tests
   - Día 5-6: Escribir tests e implementar widgets personalizables

5. **Frontend Búsqueda** (3-4 días)
   - Día 1: Escribir tests para interfaz de búsqueda
   - Día 2: Implementar interfaz para pasar tests
   - Día 3: Escribir tests para vista detallada y filtros dinámicos
   - Día 4: Implementar vista detallada y filtros para pasar tests

6. **Frontend Notificaciones** (3-4 días)
   - Día 1: Escribir tests para centro de notificaciones
   - Día 2: Implementar centro de notificaciones para pasar tests
   - Día 3: Escribir tests para alertas visuales y preferencias
   - Día 4: Implementar alertas y preferencias para pasar tests

7. **Integración y Testing Final** (3-4 días)
   - Día 1: Escribir tests end-to-end para flujos completos
   - Día 2: Integrar componentes para pasar tests E2E
   - Día 3-4: Optimizar rendimiento y refactorizar

### Criterios de Finalización
- Todos los DoD completados
- Tests pasando con cobertura ≥75%
- Aplicación funcionando con todas las nuevas características
- Historial de commits muestra ciclo TDD (tests → implementación → refactor)
- Commit con mensaje: `[feature/contracts] Stage 3 visualization and notifications completed with TDD`
- Registro en `workspace/status.md`

##############################################
## Notas de Implementación

1. **Performance Primero**: Optimizar consultas desde el inicio
2. **Caché Inteligente**: Implementar caché granular y eficiente
3. **Responsive Charts**: Asegurar gráficos adaptables
4. **Real-time Updates**: Configurar WebSockets correctamente
5. **Accessibility**: Gráficos accesibles con alt text y navegación por teclado
6. **Export Ready**: Preparar exportación de datos y visualizaciones
7. **Modular Design**: Componentes reutilizables y configurables
8. **Error Boundaries**: Manejo robusto de errores en visualizaciones con mensajes amigables y estrategias de recuperación
9. **TDD Estricto**: Seguir el ciclo TDD para todas las funcionalidades
10. **Tests como Documentación**: Usar tests para documentar comportamiento esperado
11. **Refactorización Segura**: Refactorizar con confianza gracias a los tests

Este stage transforma datos en insights accionables para todos los roles del sistema educativo, mejorando la experiencia con búsqueda avanzada y notificaciones en tiempo real.
