class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = self._validar_texto(titulo, "titulo")
        self._autor = self._validar_texto(autor, "autor")
        self._isbn = self._validar_texto(isbn, "isbn")
        self._disponible = True

    @staticmethod
    def _validar_texto(valor, nombre):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El {nombre} no puede estar vacío")
        return valor.strip()

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self._disponible:
            raise ValueError("El libro ya está prestado")
        self._disponible = False

    def devolver(self):
        if self._disponible:
            raise ValueError("El libro no está prestado")
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"
