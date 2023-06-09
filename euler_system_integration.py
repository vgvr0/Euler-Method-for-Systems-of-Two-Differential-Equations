def euler_system_integration(f1, f2, t0, x0, y0, h, n):
    """
    Función para realizar la integración numérica utilizando el método de Euler para sistemas de dos ecuaciones diferenciales.

    Parámetros:
    - f1: La función que describe la primera ecuación diferencial dx/dt = f1(t, x, y).
    - f2: La función que describe la segunda ecuación diferencial dy/dt = f2(t, x, y).
    - t0: El valor inicial de t.
    - x0: El valor inicial de x.
    - y0: El valor inicial de y.
    - h: El tamaño del paso.
    - n: El número de iteraciones.

    Retorna:
    - Tres listas: una con los valores de t, otra con los valores de x, y otra con los valores de y.
    """
    t_values = [t0]
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        t = t_values[-1]
        x = x_values[-1]
        y = y_values[-1]

        x_new = x + h * f1(t, x, y)
        y_new = y + h * f2(t, x, y)
        t_new = t + h

        t_values.append(t_new)
        x_values.append(x_new)
        y_values.append(y_new)

    return t_values, x_values, y_values


def equation1(t, x, y):
    """
    La función que describe la primera ecuación diferencial dx/dt = t^2 + y.
    """
    return t ** 2 + y


def equation2(t, x, y):
    """
    La función que describe la segunda ecuación diferencial dy/dt = x - t.
    """
    return x - t


# Parámetros de integración
t0 = 0  # Valor inicial de t
x0 = 0  # Valor inicial de x
y0 = 0  # Valor inicial de y
h = 0.1  # Tamaño del paso
n = 10  # Número de iteraciones

# Realizar la integración
t_values, x_values, y_values = euler_system_integration(equation1, equation2, t0, x0, y0, h, n)

# Imprimir los resultados
for t, x, y in zip(t_values, x_values, y_values):
    print(f"t = {t}, x = {x}, y = {y}")
