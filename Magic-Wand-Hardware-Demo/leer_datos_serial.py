import serial
import time
import csv
import keyboard

# Configuración del puerto serial
port = "COM7"  # Verifica que este sea el puerto correcto para tu S3 Mini
baudrate = 115200

def capture_data(figura):
    csv_filename = f'datos_{figura}.csv'
    ser = serial.Serial(port, baudrate)
    time.sleep(2)
    all_data = []
    capturing = False

    while True:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()

            if not capturing and "CAPTURE_START" not in line:
                continue  # Si no estamos capturando, no hacer nada con las líneas recibidas

            print(f"Línea recibida: {line}")

            if "CAPTURE_START" in line:
                capturing = True
                all_data = []
                print("Iniciando captura...")

            elif "CAPTURE_COMPLETE" in line:
                capturing = False
                print(f"Captura completa. {len(all_data)} muestras capturadas.")
                save_capture = None
                print("Presiona ESPACIO para guardar la captura, o SUPR para descartarla.")

                def on_space():
                    nonlocal save_capture
                    save_capture = True
                    keyboard.unhook_all()

                def on_delete():
                    nonlocal save_capture
                    save_capture = False
                    keyboard.unhook_all()

                keyboard.on_press_key("space", lambda _: on_space())
                keyboard.on_press_key("delete", lambda _: on_delete())

                while save_capture is None:
                    time.sleep(0.1)  # Esperar a que el usuario presione una tecla

                if save_capture:
                    with open(csv_filename, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        if file.tell() == 0:
                            writer.writerow(["ax", "ay", "az", "gx", "gy", "gz", "label"])
                        for data in all_data:
                            writer.writerow(data + [figura])
                        writer.writerow([])  # Agregar un salto de línea
                    print("Datos guardados en el archivo CSV.")
                else:
                    print("Captura descartada.")
                all_data = []  # Reiniciar los datos almacenados para la próxima captura
                break  # Salir del bucle de captura después de guardar o descartar

            elif capturing and line.startswith("DATA,"):
                parts = line.split(",")
                if len(parts) == 7:
                    data = [float(value) for value in parts[1:]]
                    all_data.append(data)
                    print(f"Muestra capturada: {data}")
                else:
                    print(f"Línea de datos incompleta: {line}")

        except ValueError as e:
            print(f"Error al convertir los datos: {e}, data: {line}")
        except KeyboardInterrupt:
            break

    ser.close()
    print("Desconectado...")

def main():
    while True:
        print("Presiona 'c' para círculo, 's' para cuadrado, 't' para signo, 'r' para reposo, 'l' para línea, 'w' para hechizo1, 'e' para ele, 'k' para hechizo2 o 'esc' para salir.")
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN and key.name in ['c', 's', 't', 'r', 'l', 'w', 'e', 'k','esc']:
            if key.name == 'c':
                print("Capturando datos para círculo")
                capture_data('circulo')
            elif key.name == 's':
                print("Capturando datos para cuadrado")
                capture_data('cuadrado')
            elif key.name == 't':
                print("Capturando datos para signo")
                capture_data('signo')
            elif key.name == 'r':
                print("Capturando datos para reposo")
                capture_data('reposo')
            elif key.name == 'l':
                print("Capturando datos para línea")
                capture_data('linea')
            elif key.name == 'w':
                print("Capturando datos para hechizo1")
                capture_data('hechizo1')
            elif key.name == 'e':
                print("Capturando datos para letra l")
                capture_data('ele')
            elif key.name == 'k':
                print("Capturando datos para hechizo2")
                capture_data('hechizo2')
            elif key.name == 'esc':
                break
            time.sleep(0.1)
 
if __name__ == "__main__":
    main() 