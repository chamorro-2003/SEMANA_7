# Sistema de Gestión - restaurante_app

**Estudiante:** Nayely Soledad Chamorro Vicente

**Asignatura:** Programación Orientada a Objetos

# Descripción del Sistema
Este proyecto consiste en una aplicación de consola desarrollada en Python con el propósito de simular la gestión interna de un restaurante mediante una estructura organizada y modular, en el cual através de un menú dinámico e interactivo, el usuario puede administrar información relacionada con dos entidades fundamentales del sistema como los productos y los clientes. Además, la aplicación permite registrar, consultar y gestionar datos de manera ordenada, facilitando el control de la información dentro de un entorno controlado en memoria.

---
## Estructura del Proyecto
Su estructura esta diseñada en base a principios de la arquitectura modular, ya que cada componente cumple una función específica dentro del sistema, ya que por un lado, la carpeta **modelos** almacena las entidades principales y sus características, permitiendo representar organizadamente la información de los productos y clientes, por otro lado, la carpeta **servicios** es la encargada de administrar las colecciones de objectos, realizar las busquedas y operaciones necesarias para el funcionamiento, por último, el archivo **main** funciona como un punto de conección entre el sistema y la acciones del usuario.

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
---
## Componentes Técnicos Aplicados
Constructor tradicional, @property y @setter
La clase Producto utiliza el constructor tradicional init para inicializar sus atributos al momento de crear cada objeto. Además, se emplean propiedades (@property) y métodos modificadores (@setter) para controlar el acceso y la modificación de los datos, garantizando que la información sea válida desde el inicio. Gracias a estas validaciones, los campos nombre y categoría no pueden estar vacíos, mientras que el precio debe ser un valor numérico mayor que cero. De esta manera, se evita la creación de registros inconsistentes y se protege la integridad de la información dentro del sistema.
## Uso de @dataclass
Para la entidad Cliente se implementó el decorador @dataclass, el cual simplifica la creación de clases destinadas al almacenamiento de datos. Esta herramienta genera automáticamente métodos como el constructor (init), la representación del objeto (repr) y las comparaciones básicas, reduciendo la cantidad de código repetitivo. Como resultado, el proyecto gana en legibilidad, organización y facilidad de mantenimiento.
Servicio de Administración
La clase Restaurante actúa como el centro de administración del sistema, ya que gestiona las colecciones de productos y clientes mediante listas privadas. Para ello, ofrece métodos que permiten registrar, listar y buscar información, manteniendo separada la lógica de negocio de la interfaz de usuario. Esta organización facilita el control de los datos y permite ampliar el sistema de manera más sencilla en el futuro.
Reflexión sobre la Creación Dinámica de Objetos
El paso de utilizar datos definidos directamente en el código a crear objetos mediante información ingresada por el usuario representa un aspecto fundamental en el desarrollo de aplicaciones reales. Este proceso permite transformar datos de entrada en objetos validados y estructurados, asegurando que la información cumpla con las reglas del sistema. Además, fortalece la integridad de los datos y favorece la escalabilidad, ya que la misma lógica puede adaptarse posteriormente para trabajar con bases de datos o servicios externos sin modificar los modelos principales.
