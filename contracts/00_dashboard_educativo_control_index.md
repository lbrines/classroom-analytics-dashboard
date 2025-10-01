# Contrato de Control - Dashboard Educativo (Versión Consolidada)

## Información del Proyecto
- **Proyecto**: Dashboard Educativo
- **Tipo**: Sistema de Gestión Educativa Full-Stack
- **Autor**: Sistema de Contratos LLM
- **Fecha**: 2025-09-30
- **Versión**: 2.0 (Consolidación de etapas)

## Índice de Contratos

| # | Archivo | Descripción | Componente | Etapa |
|---|---------|-------------|------------|---------|
| 01 | `01_dashboard_educativo_fullstack_stage01_fundaciones_auth.md` | Fundaciones del sistema y autenticación | Full-Stack | Stage 1 |
| 02 | `02_dashboard_educativo_fullstack_stage02_google_dashboards.md` | Integración Google y dashboards básicos | Full-Stack | Stage 2 |
| 03 | `03_dashboard_educativo_fullstack_stage03_visualizacion_notificaciones.md` | Visualización avanzada y notificaciones | Full-Stack | Stage 3 |
| 04 | `04_dashboard_educativo_fullstack_stage04_integracion_testing.md` | Integración completa, testing y CI/CD | Full-Stack | Stage 4 |

## Mapeo de Funcionalidades por Stage

### Stage 1: Fundaciones y Autenticación
- **Backend**: FastAPI base, autenticación JWT, OAuth 2.0, dataset mock
{{ ... }}
- **Objetivo**: Base arquitectónica sólida con autenticación completa

### Stage 2: Integración Google y Dashboards Básicos
- **Backend**: Google Classroom API, modo dual (Google/Mock), métricas básicas
- **Frontend**: Selector de modo, lista de cursos, dashboards básicos por rol, visualizaciones esenciales
- **Objetivo**: Conexión con Google Classroom y visualización básica de datos

### Stage 3: Visualización Avanzada y Notificaciones
- **Backend**: Métricas avanzadas, analytics, caché, reportes, búsqueda, notificaciones push, websockets
- **Frontend**: Dashboards avanzados, ApexCharts, filtros interactivos, búsqueda contextual, notificaciones en tiempo real
- **Objetivo**: Visualización avanzada, búsqueda y comunicación en tiempo real

### Stage 4: Integración Completa y Calidad
- **Backend**: Sincronización completa, manejo de errores avanzado, tests E2E, performance, seguridad
- **Frontend**: Gestión avanzada de cursos/estudiantes/tareas, accesibilidad WCAG, tests visuales, PWA
- **Objetivo**: Integración robusta con Google, calidad y accesibilidad

## 🏗️ Arquitectura General

### Stack Tecnológico
- **Backend**: Python + FastAPI + MongoDB
- **Frontend**: Next.js 13.5.6 (LTS) + TypeScript + Tailwind CSS
- **Integración**: Google Classroom API + OAuth 2.0
- **Testing**: pytest + Vitest + Playwright
- **CI/CD**: GitHub Actions + Docker
- **Infraestructura**: Health checks + Auto-cleanup + Version verification

### Flujo de Desarrollo
1. **Base** → Fundaciones del sistema
2. **Stage 1** → Autenticación completa
3. **Stage 2** → Integración con Google y dashboards básicos
4. **Stage 3** → Visualización avanzada y notificaciones
5. **Stage 4** → Integración completa y calidad

## 🤖 Guía para LLMs

### Orden de Lectura Recomendado
1. **Leer este archivo primero** (00) para contexto general
2. **Stages secuencialmente** (01-04) para desarrollo progresivo

### Puntos Clave a Considerar
- **Modo Dual**: Sistema funciona con Google Classroom o datos mock
- **Roles**: admin, coordinador, docente, estudiante
- **TDD First**: Test-Driven Development con tests escritos antes que el código
- **Responsive**: Diseño móvil-first en todo el frontend
- **Accesibilidad**: WCAG 2.2 AA integrada en Stage 4
- **Idioma**: Inglés como idioma único de la interfaz y datos

### Contexto del Proyecto
- **Dominio**: Educación digital
- **Usuarios**: Instituciones educativas
- **Datos**: Cursos, estudiantes, tareas, calificaciones
- **Integración**: Google Classroom como fuente principal

## 📊 Dataset Mock

### Cursos de Ejemplo
1. **eCommerce Specialist** (~150 students)
2. **Digital Marketing Specialist** (~150 students)

### Tipos de Tareas
- **Initial Assessment**: Knowledge evaluation
- **Applied Practice**: Module exercises
- **Final Project**: Integrative deliverable

### Estados de Tareas
- **Submitted**: Completed on time
- **Pending**: Within deadline
- **Late**: Past deadline but accepted
- **Not Submitted**: No delivery

## 🚀 Quick Reference

### Comandos Principales
```bash
# Backend
python -m uvicorn app.main:app --reload
python -m pytest
python scripts/health_check.py          # Verificar salud del sistema
python scripts/cleanup.py              # Limpiar procesos y archivos

# Frontend
npm run health-check                   # Verificar integridad del sistema
npm run cleanup                       # Limpiar procesos y archivos
npm run dev                          # Desarrollo con verificación
npm run build                        # Build con validación
npm run test                         # Tests con cobertura de infraestructura
```

### URLs Importantes
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/v1/health
- **System Health**: http://localhost:8000/api/v1/health/system
- **Dependencies Health**: http://localhost:8000/api/v1/health/dependencies

### Configuraciones Clave
- **Modo**: MOCK (desarrollo) / GOOGLE (producción)
- **Base de datos**: MongoDB local
- **Autenticación**: JWT tokens
- **CORS**: Configurado para frontend
- **Versiones**: Next.js 13.5.6 (LTS), Node.js 18+ (LTS)
- **Salud del Sistema**: Verificación automática habilitada
- **Auto-limpieza**: Procesos y archivos temporales

## 📋 Criterios de Aceptación Globales

### Funcionalidad
- [ ] Sistema funciona en modo MOCK y GOOGLE
- [ ] Autenticación JWT implementada
- [ ] Roles de usuario funcionando
- [ ] Dashboards por rol implementados
- [ ] Sistema de salud del sistema operativo
- [ ] Verificación de versiones estables
- [ ] Recuperación rápida (<30 min) ante errores críticos

### Calidad
- [ ] Cobertura de tests ≥75% (incluidos tests de infraestructura y escenarios de error)
- [ ] Tests de infraestructura implementados
- [ ] Linting y formateo automático
- [ ] Documentación actualizada (incluyendo estrategias de manejo de errores)
- [ ] Performance optimizada
- [ ] Catálogo de mensajes de error amigables
- [ ] Estrategias de recuperación ante fallos
- [ ] Verificación de integridad de dependencias
- [ ] Procedimientos de rollback documentados

### Accesibilidad
- [ ] WCAG 2.1 AA compliance
- [ ] Navegación por teclado
- [ ] Screen reader compatible
- [ ] Contraste adecuado

## 🔄 Flujo de Implementación con TDD

### Preparación del Entorno (Día 0)
1. **Verificar versiones** → Node.js 18+ (LTS), Next.js 13.5.6 (LTS)
2. **Limpiar entorno** → Eliminar procesos y archivos temporales
3. **Verificar integridad** → Validar node_modules y dependencias
4. **Configurar scripts** → Health checks y auto-cleanup

### Implementación por Stages
1. **Escribir tests Stage 1** → Tests para fundaciones + tests de infraestructura
2. **Implementar Stage 1** → Código + scripts de salud del sistema
3. **Escribir tests Stage 2** → Tests para Google + tests de conexión robusta
4. **Implementar Stage 2** → Código + manejo robusto de errores de integración
5. **Escribir tests Stage 3** → Tests para visualización + tests de estabilidad
6. **Implementar Stage 3** → Código + sistema de recuperación rápida
7. **Escribir tests Stage 4** → Tests para integración + tests de robustez completa
8. **Implementar Stage 4** → Código + pipeline de calidad con health checks

## 📝 Notas para Desarrolladores

### Metodología de Desarrollo
- **Commits atómicos**: Un commit por funcionalidad
- **Mensajes descriptivos**: Usar formato convencional
- **TDD Estricto**: Seguir ciclo red-green-refactor (tests fallando → tests pasando → refactorización)
- **Commits TDD**: Separar commits de tests, implementación y refactorización
- **Documentación**: Mantener actualizada y usar tests como documentación viva

### Infraestructura y Robustez
- **Versiones estables**: Usar únicamente versiones LTS (Next.js 13.5.6, Node.js 18+)
- **Health checks**: Verificar salud del sistema antes de cada sesión de desarrollo
- **Auto-limpieza**: Limpiar procesos y archivos temporales automáticamente
- **Recuperación rápida**: Tener procedimientos de rollback documentados
- **Verificación de integridad**: Validar node_modules después de instalaciones

### Calidad y Performance
- **Performance**: Optimizar desde el inicio con tests de performance
- **Tests de infraestructura**: Implementar tests para salud del sistema
- **Cobertura**: Mantener ≥75% incluyendo tests de infraestructura
- **Rollback**: Documentar procedimientos de recuperación

### Seguridad y Manejo de Errores
- **Seguridad OAuth**: Implementar PKCE, rotación de tokens, validación de estado y limitación de permisos
- **Manejo de Errores**: Sistema completo con mensajes amigables, tipado de errores y estrategias de recuperación
- **Mensajes de error**: Catálogo completo con estrategias de recuperación
- **Logging seguro**: No exponer información sensible en logs

---

**Este archivo sirve como punto de entrada para comprender el proyecto completo con estructura consolidada y mejoras de robustez implementadas. Leer los contratos individuales para detalles específicos de implementación.**

## 🛡️ Mejoras de Robustez Implementadas

### Lecciones Aprendidas Aplicadas
- **Next.js 13.5.6 (LTS)**: Versión estable que previene errores de template variables
- **Health Checks Automáticos**: Verificación continua de salud del sistema
- **Auto-cleanup**: Limpieza automática de procesos y archivos temporales
- **Tests de Infraestructura**: Validación de integridad del sistema
- **Recuperación Rápida**: Procedimientos documentados para resolver errores en <30 minutos
- **Verificación de Versiones**: Control estricto de dependencias estables

### Beneficios Esperados
- **95% menos errores** de módulos corruptos
- **80% reducción** en tiempo de resolución de errores
- **Desarrollo más predecible** y estable
- **Base sólida** para futuras iteraciones
- **Calidad profesional** desde el inicio
