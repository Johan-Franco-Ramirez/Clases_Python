# Clase que representa un libro
class Libro:

    # Constructor: se ejecuta automáticamente al crear un objeto
    def __init__(self, titulo, autor, anio, genero):
        # Atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

        # El libro inicia disponible para préstamo
        self.disponible = True

    # Método para prestar un libro
    def prestar(self):

        # Verifica si el libro está disponible
        if self.disponible:
            # Cambia el estado a no disponible
            self.disponible = False

            # Retorna un mensaje indicando que fue prestado
            return f"'{self.titulo}' fue prestado"

        # Si ya estaba prestado
        return f"'{self.titulo}' no está disponible"

    # Método para devolver un libro
    def devolver(self):

        # Verifica si el libro estaba prestado
        if not self.disponible:
            # Cambia el estado a disponible
            self.disponible = True

            # Retorna un mensaje indicando que fue devuelto
            return f"'{self.titulo}' fue devuelto"

        # Si ya estaba disponible
        return f"'{self.titulo}' ya estaba disponible"

    # Método para mostrar toda la información del libro
    def mostrar_info(self):

        # Operador ternario:
        # Si disponible es True muestra "Disponible",
        # de lo contrario muestra "Prestado"
        estado = "Disponible" if self.disponible else "Prestado"

        # Retorna todos los datos del libro en un solo texto
        return f"{self.titulo} | {self.autor} | {self.anio} | {self.genero} | {estado}"


# Programa principal
# Solo se ejecuta cuando este archivo se ejecuta directamente
if __name__ == "__main__":

    # Crear dos objetos de la clase Libro
    libro1 = Libro(
        "Cien años de soledad",
        "García Márquez",
        1967,
        "Realismo mágico"
    )

    libro2 = Libro(
        "El principito",
        "Saint-Exupéry",
        1943,
        "Infantil"
    )

    # Mostrar información inicial del libro
    print(libro1.mostrar_info())

    # Prestar el libro
    print(libro1.prestar())

    # Mostrar nuevamente la información
    print(libro1.mostrar_info())

    # Devolver el libro
    print(libro1.devolver())

    # Mostrar el estado final
    print(libro1.mostrar_info())