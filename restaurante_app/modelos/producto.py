class Producto:
    def __init__(
        self, nombre: str, categoria: str, precio: float, disponible: bool = True
    ):
        # Inicialización de atributos con validación
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # --- Propiedades y métodos para valores ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    # --- Propiedades y métodos de categoria ---
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede quedar vacía.")
        self._categoria = valor.strip()

    # --- Propiedades y métodos de precio ---
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = valor

    # --- Propiedades y métodos de disponibilidad ---
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}"
