from biblioteca import Biblioteca
from libro import Libro
from socio import Socio


def probar(condicion, mensaje):
    assert condicion, mensaje


def debe_fallar(funcion, mensaje):
    try:
        funcion()
    except ValueError:
        return
    probar(False, mensaje)


def mostrar_ejemplo():
    biblioteca = Biblioteca("Biblioteca POO")
    libro_rayuela = Libro("Rayuela", "Cortázar", "978-1")
    biblioteca.agregar_libro(libro_rayuela)
    biblioteca.agregar_libro(Libro("Ficciones", "Borges", "978-2"))
    biblioteca.registrar_socio(Socio("Ana", "30111222"))

    print("Ejemplo de préstamo y devolución:")
    biblioteca.prestar("978-1", "30111222")
    print("Prestado:", libro_rayuela)
    print("Disponibles:", ", ".join(str(libro) for libro in biblioteca.libros_disponibles()))
    biblioteca.devolver("978-1", "30111222")
    print("Devuelto:", libro_rayuela)


def ejecutar_pruebas():
    # Libro
    libro = Libro("T", "A", "I1")
    probar(libro.disponible, "Un libro nuevo debe estar disponible")
    libro.prestar()
    probar(not libro.disponible, "prestar() no marca el libro como prestado")
    debe_fallar(libro.prestar, "No se puede prestar un libro ya prestado")
    libro.devolver()
    probar(libro.disponible, "devolver() no marca el libro como disponible")
    debe_fallar(libro.devolver, "No se puede devolver un libro que no está prestado")
    probar("I1" in str(libro) and "T" in str(libro), "__str__ debe mostrar ISBN y título")
    try:
        libro.disponible = False
        probar(False, "disponible debe ser una propiedad de solo lectura")
    except AttributeError:
        pass

    # Socio
    socio = Socio("Test", "D1")
    probar(
        len(socio.libros) == 0 and socio.puede_pedir(),
        "Un socio nuevo no tiene libros y puede pedir",
    )
    for i in range(3):
        socio.agregar_libro(Libro("T", "A", f"X{i}"))
    probar(not socio.puede_pedir(), "Con 3 libros el socio no puede pedir más")
    debe_fallar(
        lambda: socio.agregar_libro(Libro("T", "A", "X9")),
        "No se puede superar el máximo de 3 libros",
    )
    debe_fallar(
        lambda: socio.quitar_libro(Libro("T", "A", "NO")),
        "No se puede quitar un libro que el socio no tiene",
    )

    # Biblioteca
    biblioteca = Biblioteca("Test")
    for i in range(5):
        biblioteca.agregar_libro(Libro("T", "A", f"B{i}"))
    biblioteca.registrar_socio(Socio("S", "D1"))
    biblioteca.registrar_socio(Socio("R", "D2"))
    debe_fallar(
        lambda: biblioteca.agregar_libro(Libro("T", "A", "B0")),
        "No se permiten ISBN repetidos",
    )
    debe_fallar(
        lambda: biblioteca.registrar_socio(Socio("X", "D1")),
        "No se permiten DNI repetidos",
    )
    debe_fallar(
        lambda: biblioteca.prestar("NOEXISTE", "D1"),
        "prestar debe fallar si el libro no existe",
    )
    debe_fallar(
        lambda: biblioteca.prestar("B0", "NOEXISTE"),
        "prestar debe fallar si el socio no existe",
    )

    biblioteca.prestar("B0", "D1")
    probar(
        len(biblioteca.libros_disponibles()) == 4,
        "prestar no saca el libro de los disponibles",
    )
    debe_fallar(
        lambda: biblioteca.prestar("B0", "D2"),
        "No se puede prestar un libro ya prestado",
    )
    debe_fallar(
        lambda: biblioteca.devolver("B0", "D2"),
        "Un socio no puede devolver un libro que no tiene",
    )

    biblioteca.prestar("B1", "D1")
    biblioteca.prestar("B2", "D1")
    debe_fallar(
        lambda: biblioteca.prestar("B3", "D1"),
        "Un socio con 3 libros no puede pedir otro",
    )
    probar(
        len(biblioteca.libros_disponibles()) == 2,
        "Si el préstamo falla, el libro debe seguir disponible",
    )

    biblioteca.devolver("B0", "D1")
    probar(
        len(biblioteca.libros_disponibles()) == 3,
        "devolver no vuelve a poner el libro como disponible",
    )
    biblioteca.prestar("B3", "D1")


def main():
    mostrar_ejemplo()
    ejecutar_pruebas()
    print("¡Todas las pruebas pasaron!")


if __name__ == "__main__":
    main()
