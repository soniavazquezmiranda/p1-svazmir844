from libro import Libro


def main():
    libros = [
        Libro("La colmena", "Camilo José Cela", 1951),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("La casa de Bernarda Alba", "Federico García Lorca", 1936),
        Libro("Nada", "Carmen Laforet", 1945),
        Libro("La familia de Pascual Duarte", "Camilo José Cela", 1942)
    ]

    libro = libros[1]

    try:
        print(libro)
        libro.prestar()
        libro.prestar()
    except ValueError as error:
        print(error)

    try:
        print(libro)
        libro.devolver()
        libro.devolver()
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
