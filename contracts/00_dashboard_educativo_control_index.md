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
- **Frontend**: Next.js 15 + TypeScript + Tailwind CSS
- **Integración**: Google Classroom API + OAuth 2.0
- **Testing**: pytest + Vitest + Playwright
- **CI/CD**: GitHub Actions + Docker

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

# Frontend
npm run dev
npm run build
npm run test
```

### URLs Importantes
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/v1/health

### Configuraciones Clave
- **Modo**: MOCK (desarrollo) / GOOGLE (producción)
- **Base de datos**: MongoDB local
- **Autenticación**: JWT tokens
- **CORS**: Configurado para frontend

## 📋 Criterios de Aceptación Globales

### Funcionalidad
- [ ] Sistema funciona en modo MOCK y GOOGLE
- [ ] Autenticación JWT implementada
- [ ] Roles de usuario funcionando
- [ ] Dashboards por rol implementados

### Calidad
- [ ] Cobertura de tests ≥70% (incluidos tests específicos para escenarios de error)
- [ ] Linting y formateo automático
- [ ] Documentación actualizada (incluyendo estrategias de manejo de errores)
- [ ] Performance optimizada
- [ ] Catálogo de mensajes de error amigables
- [ ] Estrategias de recuperación ante fallos

### Accesibilidad
- [ ] WCAG 2.1 AA compliance
- [ ] Navegación por teclado
- [ ] Screen reader compatible
- [ ] Contraste adecuado

## 🔄 Flujo de Implementación con TDD

1. **Escribir tests Stage 1** → Tests para fundaciones y autenticación
2. **Implementar Stage 1** → Código para pasar tests de fundaciones y autenticación
3. **Escribir tests Stage 2** → Tests para Google y dashboards básicos
4. **Implementar Stage 2** → Código para pasar tests de integración y visualización
5. **Escribir tests Stage 3** → Tests para visualización avanzada y notificaciones
6. **Implementar Stage 3** → Código para pasar tests de experiencia de usuario
7. **Escribir tests Stage 4** → Tests para integración completa y calidad
8. **Implementar Stage 4** → Código para pasar tests finales

## 📝 Notas para Desarrolladores

- **Commits atómicos**: Un commit por funcionalidad
- **Mensajes descriptivos**: Usar formato convencional
- **TDD Estricto**: Seguir ciclo red-green-refactor (tests fallando → tests pasando → refactorización)
- **Commits TDD**: Separar commits de tests, implementación y refactorización
- **Documentación**: Mantener actualizada y usar tests como documentación viva
- **Performance**: Optimizar desde el inicio con tests de performance
- **Seguridad OAuth**: Implementar PKCE, rotación de tokens, validación de estado y limitación de permisos
- **Manejo de Errores**: Sistema completo con mensajes amigables, tipado de errores y estrategias de recuperación

---

**Este archivo sirve como punto de entrada para comprender el proyecto completo con estructura consolidada. Leer los contratos individuales para detalles específicos de implementación.**
