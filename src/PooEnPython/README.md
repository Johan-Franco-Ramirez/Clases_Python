# Fundamentos de Python: Clases, Objetos y Encapsulación

Repositorio desarrollado para las actividades de formación en Programación Orientada a Objetos (POO) en Python, abarcando talleres prácticos y un reto integrador de gestión.

---

## 📂 Estructura del Repositorio

```text
PooEnPython/
│
├── EjemplosPOO/         # Material didáctico base
├── TalleresPOO/
│   ├── TallerLibros.py      # Gestión de libros (Clases y Objetos)
│   └── TallerEncapsulacion.py # Cuenta Bancaria (Encapsulación)
└── RetoPOO/
    └── RetoSistemaPrestamos.py # Sistema de Préstamos de Equipos

```

---

## 🛠️ Descripción de Módulos

### Talleres de Práctica (TalleresPOO/)
TallerLibros.py: Implementación de la clase Libro con atributos básicos (titulo, autor, paginas, disponible) y métodos de control como prestar(), devolver() y informacion(), garantizando validaciones de estado en consola.

TallerEncapsulacion.py: Creación de la clase CuentaBancaria aplicando atributos privados (_titular, _saldo), uso de decoradores @property para control de lectura exclusiva en el titular, y validaciones estrictas mediante @setter para impedir saldos negativos, junto con métodos de depósito y retiro seguros.

### Reto Integrador (RetoPOO/)
RetoSistemaPrestamos.py: Aplicación modular orientada a la gestión del inventario y préstamos de equipos institucionales. Utiliza colecciones anidadas (diccionarios y listas) y tuplas inmutables (usuario, fecha) para mantener la trazabilidad e integridad del historial de cada equipo.
---

## 💡 Reflexión

Este espacio consolidó los pilares de la POO, permitiendo estructurar código modular, seguro y escalable mediante la protección de datos y el modelado de entidades del mundo real.

## Johan Franco R. ADSO