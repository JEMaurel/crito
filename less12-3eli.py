import threading

# Contador global
contador = 0
lock = threading.Lock()  # Crea un objeto Lock

def incrementar():
    global contador
    for _ in range(100000):
        with lock:  # Adquiere el Lock
            contador += 1  # Incrementa el contador
            # Se liberará el Lock automáticamente al salir del bloque 'with'

# Crear dos hilos que ejecutarán la función incrementar
hilos = [threading.Thread(target=incrementar) for _ in range(2)]

# Iniciar los hilos
for hilo in hilos:
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Imprimir el resultado final
print("Contador final:", contador)
