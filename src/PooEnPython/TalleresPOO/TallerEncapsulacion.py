class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self._titular = titular
        # Usamos el setter de la propiedad para validar el saldo inicial
        self.saldo = saldo_inicial

    # Propiedad para titular (Solo lectura)
    @property
    def titular(self):
        return self._titular

    # Propiedad para saldo (Lectura y Escritura con validación)
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad: float) -> bool:
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad: float) -> bool:
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

# --- Prueba de la clase ---
if __name__ == "__main__":
    try:
        cuenta = CuentaBancaria("Johan Franco Ramirez", 1000.0)
        
        # Acceso a atributos
        print(f"Titular: {cuenta.titular}")
        print(f"Saldo inicial: {cuenta.saldo}")
        
        # Operaciones
        cuenta.depositar(500.0)
        print(f"Saldo tras depósito: {cuenta.saldo}")
        
        cuenta.retirar(200.0)
        print(f"Saldo tras retiro: {cuenta.saldo}")
        
        # Prueba de restricciones
        print("\nIntentando poner saldo negativo (debe fallar):")
        cuenta.saldo = -50  # Esto lanzará el ValueError
        
    except ValueError as e:
        print(f"Error detectado: {e}")