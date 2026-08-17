class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True
    
    def prestar(self) -> str:
        """Cambia el estado de disponibilidad a False si está disponible, o retorna un mensaje si ya está prestado."""
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado exitosamente."
        else:
            return f"Lo siento, el libro '{self.titulo}' no está disponible actualmente."
    
    def devolver(self) -> str:
        """Cambia el estado de disponibilidad a True si estaba prestado, o retorna un mensaje si ya se encontraba disponible."""
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto a la biblioteca."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible en la biblioteca."
    
    def informacion(self) -> str:
        """Devuelve una cadena con toda la información del libro, incluyendo su estado de disponibilidad."""
        estado = "Disponible" if self.disponible else "No disponible (Prestado)"
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}\n"
            f"Estado: {estado}"
        )

# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())

if __name__ == "__main__":
    main()