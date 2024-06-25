import numpy as np

def func(x, t):
    """ Función de ejemplo para resolver mediante los métodos para ODEs

    Args:
        x (float): Valores de la variable dependiente a evaluar.
        t (float): Valores de la variable independiente a evaluar.

    Returns:
        float: Un número que es el resultado de evaluar los variables x y t en la función.

    """
    return -(x*x*x) + np.sin(t)

def euler(f,x0,t0,tf,N):
    """ Método de Euler para resolver ODE

    Examples:
        >>> x_vals20, t_vals20 = euler(func, 0.0, 0.0, 10.0, 20)

        >>> x_vals1000, t_vals1000 = euler(func, 0.0, 0.0, 10.0, 1000)

    Args:
        f (float): Valor devuelto al evaluar las variables en la función.
        x0 (float): Valor inicial de la variable dependiente x(t).
        t0 (float): Valor inicial de la variable independiente t.
        tf (float): Valor final elegido para la variable dependiente t.
        N (int): Pasos temporales para llegar al punto final (tf).

    Returns:
        array: Un arreglo con los valores x_vals y t_vals para cada iteración del for loop (solución numérica de la ecuación).

    """
    t_vals = np.linspace(t0,tf,N)
    h = t_vals[1] - t_vals[0]
    x_vals = np.zeros(t_vals.size)
    x_vals[0] = x0
    for i in range(t_vals.size - 1):
        x_vals[i+1] = x_vals[i] + (h * f(x_vals[i], t_vals[i]))

    return x_vals, t_vals

def rk2(f,x0,t0,tf,N):
    """ Método de RK2 para resolver ODE

    Examples:
        >>> x_vals20, t_vals20 = rk2(func, 0.0, 0.0, 10.0, 20)

        >>> x_vals1000, t_vals1000 = rk2(func, 0.0, 0.0, 10.0, 1000)

    Args:
        f (float): Valor devuelto al evaluar las variables en la función.
        x0 (float): Valor inicial de la variable dependiente x(t).
        t0 (float): Valor inicial de la variable independiente t.
        tf (float): Valor final elegido para la variable dependiente t.
        N (int): Pasos temporales para llegar al punto final (tf).

    Returns:
        array: Un arreglo con los valores x_vals y t_vals para cada iteración del for loop (solución numérica de la ecuación).

    """
    t_vals = np.linspace(t0,tf,N)
    h = t_vals[1] - t_vals[0]
    x_vals = np.zeros(t_vals.size)
    x_vals[0] = x0
    for i in range(t_vals.size - 1):
        k1 = h * f(x_vals[i], t_vals[i])
        k2 = h * f(x_vals[i] + (k1/2), t_vals[i] + (h/2))
        x_vals[i+1] = x_vals[i] + k2

    return x_vals, t_vals

def rk4(f,x0,t0,tf,N):
    """ Método de RK4 para resolver ODE

    Examples:
        >>> x_vals20, t_vals20 = rk4(func, 0.0, 0.0, 10.0, 20)

        >>> x_vals1000, t_vals1000 = rk4(func, 0.0, 0.0, 10.0, 1000)

    Args:
        f (float): Valor devuelto al evaluar las variables en la función.
        x0 (float): Valor inicial de la variable dependiente x(t).
        t0 (float): Valor inicial de la variable independiente t.
        tf (float): Valor final elegido para la variable dependiente t.
        N (int): Pasos temporales para llegar al punto final (tf).

    Returns:
        array: Un arreglo con los valores x_vals y t_vals para cada iteración del for loop (solución numérica de la ecuación).

    """
    t_vals = np.linspace(t0,tf,N)
    h = t_vals[1] - t_vals[0]
    x_vals = np.zeros(t_vals.size)
    x_vals[0] = x0
    for i in range(t_vals.size - 1):
        k1 = h * f(x_vals[i], t_vals[i])
        k2 = h * f(x_vals[i] + (k1/2), t_vals[i] + (h/2))
        k3 = h * f(x_vals[i] + (k2/2), t_vals[i] + (h/2))
        k4 = h * f(x_vals[i] + k3, t_vals[i] + h)
        x_vals[i+1] = x_vals[i] + (k1 + 2*k2 + 2*k3 + k4)/6

    return x_vals, t_vals
