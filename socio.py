class Socio:
    MAX_LIBROS = 3

    def __init__(self, nombre, dni):
        self._nombre = self._validar_texto(nombre, "nombre")
        self._dni = self._validar_texto(dni, "DNI")
        self._libros = []

    @staticmethod
    def _validar_texto(valor, nombre):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El {nombre} no puede estar vacío")
        return valor.strip()

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def libros(self):
        return self._libros.copy()

    def puede_pedir(self):
        return len(self._libros) < self.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError("El socio ya alcanzó el máximo de libros prestados")
        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError("El socio no tiene ese libro")
        self._libros.remove(libro)

    def __str__(self):
        return (
            f"{self.nombre} (DNI {self.dni}) - "
            f"{len(self._libros)} libro(s) prestado(s)"
        )
