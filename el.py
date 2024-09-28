import RPi.GPIO as GPIO
import time
import os
import sys

# Configuración inicial
GPIO.setmode(GPIO.BCM)  # Usamos la numeración BCM
GPIO.setup(17, GPIO.OUT)  # Configuramos el pin 17 como salida

def mostrar_opciones():
    print("\nOpciones:")
    print("j - Encender el LED")
    print("k - Apagar el LED")
    print("r - Submenú de opciones adicionales")
    print("Presiona cualquier otra tecla para mostrar las opciones nuevamente.")

def sub_menu_r():
    print("\nSubopciones para 'r':")
    print("t - Dejar el LED encendido y apagar el programa.")
    print("w - Dejar el LED encendido, cuenta regresiva y ejecutar 'apagate.py'.")
    print("Presiona cualquier otra tecla para volver al menú principal.")

# Variable para verificar si se debe limpiar GPIO al finalizar
limpiar_gpio = True

try:
    while True:
        # Mostrar las opciones disponibles
        mostrar_opciones()
        
        # Pregunta al usuario qué desea hacer
        opcion = input("\nElige una opción: ").lower()
        
        if opcion == 'j':
            # Encender el LED
            GPIO.output(17, GPIO.HIGH)
            print("El LED está encendido.")
        elif opcion == 'k':
            # Apagar el LED
            GPIO.output(17, GPIO.LOW)
            print("El LED está apagado.")
        elif opcion == 'r':
            # Mostrar submenú
            sub_menu_r()
            sub_opcion = input("\nElige una subopción: ").lower()
            
            if sub_opcion == 't':
                # Subopción t: Dejar el LED encendido y apagar el programa
                GPIO.output(17, GPIO.HIGH)
                print("El LED permanecerá encendido. Saliendo del programa...")
                limpiar_gpio = False  # No limpiar GPIO
                break  # Termina el programa
            elif sub_opcion == 'w':
                # Subopción w: Dejar el LED encendido, cuenta regresiva y ejecutar apagate.py
                GPIO.output(17, GPIO.HIGH)
                print("El LED permanecerá encendido. Iniciando cuenta regresiva...")
                for i in range(4, 0, -1):
                    print(f"Cerrando en {i}...")
                    time.sleep(1)
                print("Cerrando y ejecutando 'apagate.py'...")
                
                # Ejecutar 'apagate.py' y salir
                os.execvp("python3", ["python3", "apagate.py"])  # Reemplaza el programa actual por apagate.py
            else:
                print("Subopción no válida. Volviendo al menú principal.")
        else:
            print("Opción no válida. Por favor elige 'j', 'k', o 'r'.")
        
        # Pausa para darle tiempo al usuario antes de volver a mostrar las opciones
        time.sleep(1)

finally:
    # Solo limpia los pines si no se eligió la opción de dejar el LED encendido
    if limpiar_gpio:
        GPIO.cleanup()
