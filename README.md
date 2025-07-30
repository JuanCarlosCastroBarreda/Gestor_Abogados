# Gestor de Abogados

Sistema de gestión de expedientes legales desarrollado en Python con Flask y SQLAlchemy, siguiendo principios SOLID y buenas prácticas de ingeniería de software.

## 🏗️ Arquitectura

El proyecto está organizado en capas:
- **Presentación:** Controladores REST y vistas HTML, formateo de respuestas con Presenters, rutas con Blueprints.
- **Aplicación:** Servicios que implementan la lógica de negocio y orquestan operaciones.
- **Dominio:** Entidades principales, reglas de negocio, interfaces de repositorios.
- **Infraestructura:** Implementaciones concretas de repositorios y acceso a base de datos.

## 💎 Principios SOLID

## 💎 Principios SOLID en la Codebase

**SRP (Single Responsibility Principle):**
Cada clase y módulo tiene una única responsabilidad. Por ejemplo, `ExpedientePresenter` solo formatea respuestas HTTP, y `IExpedienteRepositorio` define únicamente la interfaz de acceso a datos de expedientes.

**OCP (Open/Closed Principle):**
El sistema está abierto a extensión pero cerrado a modificación. Puedes agregar nuevos métodos o entidades (por ejemplo, nuevos tipos de repositorios o presentadores) sin modificar las clases existentes. Los Blueprints permiten añadir nuevas rutas sin alterar el núcleo de la aplicación.

**LSP (Liskov Substitution Principle):**
Las implementaciones pueden sustituir a sus interfaces sin alterar el funcionamiento. Por ejemplo, `RepositorioExpedienteSQL` implementa `IExpedienteRepositorio` y puede ser intercambiado por otro repositorio sin romper la lógica de negocio.

**ISP (Interface Segregation Principle):**
Las interfaces son específicas y no obligan a implementar métodos innecesarios. `IExpedienteRepositorio` solo expone los métodos relevantes para expedientes, evitando dependencias innecesarias.

**DIP (Dependency Inversion Principle):**
Las capas superiores dependen de abstracciones y no de implementaciones concretas. Los servicios reciben instancias de interfaces (como `IExpedienteRepositorio`) y no de clases concretas, facilitando el testing y la extensibilidad.

## 🛠️ Patrones de Diseño
- **Repository Pattern:** Abstracción del acceso a datos.
- **Service Layer Pattern:** Encapsula lógica de negocio.
- **Presenter Pattern:** Formatea datos para la presentación.

## 📊 Estructura
```
Gestor_Abogados/
├── app/
│   ├── presentacion/
│   ├── aplicacion/
│   ├── dominio/
│   ├── infraestructura/
│   └── templates/
├── requirements.txt
└── run.py
```

## 🚀 Funcionalidades
- Gestión completa de expedientes (CRUD)
- API REST y vistas HTML
- Manejo de roles de usuario
- Gestión de documentos
- Calendario de eventos

## ⚙️ Tecnologías
- Flask
- SQLAlchemy
- Jinja2

## 🔄 Buenas Prácticas
- Separación de responsabilidades
- Inyección de dependencias
- Manejo de errores y validaciones
- Código limpio y comentado

## 🧪 Testing
- Estructura preparada para tests unitarios e integración

## 📝 Conclusión
Este proyecto aplica principios SOLID y patrones de diseño para lograr un sistema mantenible, extensible y profesional.
