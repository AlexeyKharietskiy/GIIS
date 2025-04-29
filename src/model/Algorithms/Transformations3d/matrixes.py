import numpy as np

def load_object(filename):
    return np.loadtxt(filename)

def translation_matrix(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    
def move_matrix(dx, dy, dz):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [dx, dy, dz, 1]
    ])

def rotation_matrix_x(theta):
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), np.sin(theta), 0],
        [0, -np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])
    
def rotation_matrix_y(theta):
    return np.array([
        [np.cos(theta), 0, -np.sin(theta), 0],
        [0, 1, 0, 0],
        [np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    
def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    
def apply_transformation(points, refactor_matrix):
    homogeneous_points = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed = np.dot(homogeneous_points, refactor_matrix.T)
    return transformed[:, :3]


if __name__ == "__main__":
    # Загрузка объекта из файла
    points = load_object(r'D:\Project\sem6\GIIS\src\model\Algorithms\Transformations3d\object.txt')
    print("Исходные координаты:\n", points)

    # Определяем последовательность преобразований
    # 1. Перемещение на (2, 3, 1)
    T = translation_matrix(2, 3, 1)
    points = apply_transformation(points, T)
    print("\nПосле перемещения на (2, 3, 1):\n", points)

    # 2. Поворот вокруг оси Z на 45 градусов
    R = rotation_matrix_z(np.deg2rad(45))
    points = apply_transformation(points, R)
    print("\nПосле поворота на 45 градусов вокруг оси Z:\n", points)

    # 3. Масштабирование (сжатие/растяжение): уменьшение в 0.5 раз по всем осям
    S = scaling_matrix(0.5, 0.5, 0.5)
    points = apply_transformation(points, S)
    print("\nПосле масштабирования (уменьшение в 0.5 раз):\n", points)