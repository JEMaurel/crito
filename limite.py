import RPi.GPIO as GPIO
import time

# Configuración inicial
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Configuramos el pin 17 como salida (para el LED)

# Parámetros de control
frecuencia_inicial = 1  # Hz
frecuencia_final = 70  # Hz, suponiendo que el límite de percepción humana está aquí
duracion_total = 6  # segundos para alcanzar el "momento crítico"
momento_critico_mostrado = False

# Cálculo de incremento por cada segundo
incremento_frecuencia = (frecuencia_final - frecuencia_inicial) / duracion_total

try:
    tiempo_inicio = time.time()  # Marca el tiempo de inicio del programa
    frecuencia_actual = frecuencia_inicial

    while True:
        # Calculamos el tiempo desde que comenzó el programa
        tiempo_transcurrido = time.time() - tiempo_inicio
        
        # Aumentar la frecuencia gradualmente
        frecuencia_actual = frecuencia_inicial + incremento_frecuencia * tiempo_transcurrido
        
        # Mostrar la frecuencia actual en consola
        print(f"Frecuencia de parpadeo: {frecuencia_actual:.2f} Hz")
        
        # Verificar si hemos alcanzado el "momento crítico" (aproximadamente 60-70 Hz)
        if frecuencia_actual >= frecuencia_final and not momento_critico_mostrado:
            print("MOMENTO CRÍTICO")
            time.sleep(1)  # Mostrar el cartel del momento crítico durante 1 segundo
            momento_critico_mostrado = True
        
        # Si la frecuencia supera el límite de percepción promedio (por ejemplo, 60 Hz), terminamos
        if frecuencia_actual >= frecuencia_final:
            print(f"Frecuencia máxima alcanzada: {frecuencia_actual:.2f} Hz")
            break
        
        # Control de parpadeo del LED
        periodo = 1 / frecuencia_actual  # Tiempo de un ciclo completo
        GPIO.output(17, GPIO.HIGH)  # Encender el LED
        time.sleep(periodo / 2)  # Mantenerlo encendido por la mitad del periodo
        GPIO.output(17, GPIO.LOW)  # Apagar el LED
        time.sleep(periodo / 2)  # Mantenerlo apagado por la otra mitad del periodo

finally:
    GPIO.cleanup()  # Limpiar la configuración de los pines al finalizar

