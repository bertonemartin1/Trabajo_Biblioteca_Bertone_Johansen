from libro import Libro
from socio import Socio


class Biblioteca:
    def __init__(self, nombre):
        self._nombre = self._validar_texto(nombre, "nombre")
        self._libros = {}
        self._socios = {}

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El {campo} no puede estar vacío")
        return valor.strip()

    @property
    def nombre(self):
        return self._nombre

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("Solo se pueden agregar libros")
        if libro.isbn in self._libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if not isinstance(socio, Socio):
            raise ValueError("Solo se pueden registrar socios")
        if socio.dni in self._socios:
            raise ValueError(f"Ya existe un socio con DNI {socio.dni}")
        self._socios[socio.dni] = socio

    def prestar(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        if dni not in self._socios:
            raise ValueError(f"No existe un socio con DNI {dni}")

        libro = self._libros[isbn]
        socio = self._socios[dni]
        if not libro.disponible:
            raise ValueError("El libro no está disponible")
        if not socio.puede_pedir():
            raise ValueError("El socio alcanzó el máximo de libros prestados")

        libro.prestar()
        socio.agregar_libro(libro)

    def devolver(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        if dni not in self._socios:
            raise ValueError(f"No existe un socio con DNI {dni}")

        libro = self._libros[isbn]
        socio = self._socios[dni]
        if libro not in socio.libros:
            raise ValueError("El socio no tiene ese libro")

        libro.devolver()
        socio.quitar_libro(libro)

    def libros_disponibles(self):
        return [libro for libro in self._libros.values() if libro.disponible]
