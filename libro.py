class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")

        self.disponible = False

    def devolver(self):
        if self.disponible:
            raise ValueError("El libro ya está disponible")

        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"
    
    def __eq__(self, otro):
        if not isinstance(otro, Libro):
            return False
        return (
            self.titulo == otro.titulo
            and self.autor == otro.autor
            and self.anio == otro.anio
        )
