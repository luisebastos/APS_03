import numpy as np
import cv2 as cv

def matriz_rotacao(theta):
    rad = np.radians(theta)  
    return np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])

def matriz_cisalhamento(shear_factor):
    return np.array([
        [1, shear_factor, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

def matriz_translacao(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def transformar_imagem(image, theta, shear_factor):
    h, w = image.shape[:2]  

    destino = np.zeros_like(image)

    R = matriz_rotacao(theta)
    S = matriz_cisalhamento(shear_factor)

    T1 = matriz_translacao(-w // 2, -h // 2)

    T2 = R @ S

    T3 = matriz_translacao(w // 2, h // 2)

    T_final = T3 @ T2 @ T1
    T_inv = np.linalg.inv(T_final)

    for i in range(h):
        for j in range(w):
            destino_coords = np.array([j, i, 1])

            origem_coords = T_inv @ destino_coords
            x_orig, y_orig = origem_coords[0], origem_coords[1]

            if 0 <= x_orig < w and 0 <= y_orig < h:
                destino[i, j] = image[int(y_orig), int(x_orig)]

    return destino

def run():
    cap = cv.VideoCapture(0)
    
    width = 320
    height = 240
    angle = 0
    rotation_speed = 1
    shear_factor = 0.0
    shear_direction = 1  

    if not cap.isOpened():
        print("Não consegui abrir a câmera!")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não consegui capturar frame!")
            break

        frame = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        image = np.array(frame).astype(float) / 255

        transformed_image = transformar_imagem(image, angle, shear_factor)

        cv.imshow('Minha Imagem!', transformed_image)

        angle += rotation_speed
        if angle >= 360:
            angle = 0

        shear_factor += 0.01 * shear_direction
        if abs(shear_factor) >= 0.3: 
            shear_direction *= -1  

        key = cv.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('+'):
            rotation_speed += 1
        elif key == ord('-'):
            rotation_speed = max(1, rotation_speed - 1)

    cap.release()
    cv.destroyAllWindows()

run()