# ODEs
## Introducción
Para este trabajo resolveremos ecuaciones diferenciales usando rk2, rk4 y euler.
Estas 3 formas de resolver EDOs serán aplicadas a diversas ecuaciones donde hablaremos de en qué caso resulta mejor utilizar un método en concreto y sus diferencias.
 
## Método de Euler
Este método se basa en una expansión de Taylor de una función x(t). De manera que hacemos x(t+h), donde h representa un salto infinitesimal.
 
$$
x(t+h) = x(t) + h\frac{dx}{dt} + \overbrace{ \frac{h^2}{2} \frac{d^2x}{dt^2} } ^{\epsilon} + O(h^3 )
$$
 
Entonces como h es próximo a ser cero nos basta con usar
 
$$
x(t + h) = x(t) + hf(x,t)
$$
 
Para problemas más complejos necesitamos una mejor aproximación, la cual podemos obtener en base a los siguientes parámetros:
 
* 1- Empezamos con $t_{0}=0$ y $x_{0}=0$.
* 2- Discretizamos el tiempo de la forma ti.
* 3- Encontramos un x para cada punto del tiempo, de la forma $x_{i} = x_{i-1} + hf(x_{i-1})$.
 
## Runge-Kutta (RK)
El método de Runge-Kutta es un método numérico el cual se usa para aproximar la solución de una ecuación diferencial. Este es uno de los métodos más útiles para la resolución de ecuaciones diferenciales debido a su estabilidad. Hay varios tipos de Runge-Kutta cuya diferencia radica en su grado. Este es un método que parte del método de Euler, no obstante, este     tiene un mayor rendimiento a nivel computacional. A continuación veremos dos formas de este.
 
## RK2
Lo que buscamos con este método es evaluar el punto medio para evaluar en el método de Euler. O sea, buscamos el punto t+ h/2.

Entonces hagamos la expansión de Taylor alrededor del punto t + h/2.
 
$$
x(t + h) = x\left(t + \frac{h}{2}\right) + \frac{h}{2}\left(\frac{dx}{dt}\right){t+h/2} + \frac{h^2}{8}\left(\frac{d^2x}{dt^2}\right){t+h/2} + O(h^3)
$$
 
Ahora con x(t)
 
$$
x(t) = x\left(t + \frac{h}{2}\right) - \frac{h}{2}\left(\frac{dx}{dt}\right){t+h/2} + \frac{h^2}{8}\left(\frac{d^2x}{dt^2}\right){t+h/2} + O(h^3)
$$
 
Si sustraemos las dos ecuaciones nos queda

$$
x(t + h) = x(t) + h\left(\frac{dx}{dt}\right)_{t+h/2} + O(h^3)
$$

Dándonos
 
$$
x(t + h) = x(t) + hf[x(t + h/2), t + h/2] + O(h^3)
$$
 
Hay un inconveniente, necesitamos el valor del punto medio, no obstante, podemos solucionar este problema aproximando este punto. Esto lo hacemos de una manera muy sencilla. Su aproximación es: (x+h/2) = x(t) + h/2 * f(x,t).

Ahora sí, obtenemos finalmente las ecuaciones de este método
 
* $k_1 = hf(x,t),$
* $k_2 = hf\left(x + \frac{k_1}{2},t + \frac{h}{2}\right)$
 
## RK4

La diferencia con el método anterior es que este usa más puntos entre x(t) y x(t+h) mediante expansiones de Taylor. Para este punto el álgebra se vuelve muy engorroso y llega a tener una complejidad desproporcionada para algunos problemas, por lo cual si hacemos una relación entre su complejidad y su funcionalidad el método de RK4 termina siendo el método          predilecto.
Sus ecuaciones son las siguientes:

* $k_1 = hf(x, t)$,
* $k_2 = hf\left(x + \frac{k_1}{2}, t+\frac{h}{2}\right)$,
* $k_3 = hf\left(x + \frac{k_2}{2}, t+\frac{h}{2}\right)$,
* $k_4 = hf\left(x + k_3, t + h \right)$,
* $x(t+h) = x(t) + \frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4)$.

::: ode

