import pyautogui
import json
import time
import keyboard
from pynput.mouse import Listener, Button
import colorsys

# Lista vacía para almacenar las coordenadas
coordinates = []

def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        print(f'\033[38;2;{get_color()};1m[🔖 ] Recorded click On: {x}, {y}\033[0m')
        coordinates.append((x, y))
    if button == Button.right and pressed:  # Clic derecho para detener el proceso de captura de Clics
        return False

def get_color():
    t = time.time() % 10
    r, g, b = [int(255*x) for x in colorsys.hsv_to_rgb(t / 10, 1.0, 1.0)]
    return f'{r};{g};{b}'

def save_coordinates():
    with open('coordinates.json', 'w') as file:
        json.dump(coordinates, file)
    print('\033[38;2;255;255;255m[💾 ] Create/Saved to Coordinates.json\033[0m')

def load_coordinates():
    with open('coordinates.json', 'r') as file:
        loaded_coordinates = json.load(file)
    return loaded_coordinates

def click_in_loop(minutes, delay):
    # Cargar las coordenadas
    loaded_coordinates = load_coordinates()

    # Calcular el tiempo de finalización
    end_time = time.time() + minutes * 60
    
    # Realizar los clics en un bucle
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        progress = "#" * int((1 - remaining_time / (minutes * 60)) * 20)
        print(f"\033[38;2;{get_color()};1m[⏱  ] Time left: {remaining_time:02d} seconds |{progress:20s}|\033[0m", end='\r')
        for coord in loaded_coordinates:
            pyautogui.click(coord[0], coord[1])
            time.sleep(delay)  # Añadir un tiempo de espera entre cada clic
            if keyboard.is_pressed('esc'):  # Presionar 'esc' para detener el bucle
                return
    print(f"\033[38;2;{get_color()};1m---------------------------------------------------------\033[0m") 


    print(f"\033[38;2;{get_color()};1m[🤖 ] Time's up! Thanks for using the auto-clicker [🤖 ]!\033[0m")
    print(f"\033[38;2;{get_color()};1m---------------------------------------------------------\033[0m") 

def main():
    print(f"\033[38;2;{get_color()};1m#########################################################\033[0m")
    print(f"\033[38;2;{get_color()};1m[ (>‿◠)✌  ] Welcome to the auto-clicker program [🤖]!\033[0m")
    print(f"\033[38;2;{get_color()};1m                 !BY BENOX 2023 \033[0m")
    print(f"\033[38;2;{get_color()};1m#########################################################\033[0m")

    # Grabar los clics
    with Listener(on_click=on_click) as listener:
        listener.join()

    # Guardar las coordenadas
    print(f"\033[38;2;{get_color()};1m---------------------------------------------------------\033[0m") 
    save_coordinates()
    print(f"\033[38;2;{get_color()};1m---------------------------------------------------------\033[0m") 

    # Preguntar al usuario la duración del bucle y el tiempo de espera entre cada clic
    minutes = int(input('[⏱  ] Enter loop duration in minutes: '))
    delay = float(input('[⏱  ] Enter delay between clicks in seconds: '))
    print(f"\033[38;2;{get_color()};1m---------------------------------------------------------\033[0m") 


    # Realizar los clics
    click_in_loop(minutes, delay)

# Ejecutando la función principal
if __name__ == "__main__":
    main()
