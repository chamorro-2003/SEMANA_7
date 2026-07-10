from dataclasses import dataclass

# Clase Cliente
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self) -> str:
        return f"Cliente ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"
