# Patrones de diseño que posiblemente se podrian usar para el desarrollo del video juego Agar.io

# 1. Prototype: Con este patron podremos clonar objetos en tiempo de ejecución, se implemento en la creacion de fichas a "comer" por todos los jugadores, como dichos elementos no cambian en su composicion o estructura, generamos una clonacion del objeto bajo la funcion "getClon" y "putClon" las cuales nos permiten capturar la estructura de una ficha "reina" para luego agregarla al final de la cola para posterior mostrarla en pantalla

# 2. Builder: La implementacion del patron Builder se realizo para realizar la instancia de un nuevo jugador dentro del tablero, dado que todos los jugadores tienen unos parametros iniciales, pero pueden tener existir jugadores con comportamientos distontos lo cual a traves de las funciones "buildCamera", "buildPosition" y "buildRandomMovement" se agregan caracteristicas distintas que serán contenidas por el nuevo jugador o "Player", diferentes a los atributos que se usan para el jugador "Enemy", este tipo de patrón se usa cuando es necesario crear varios objetos y hay restricciones en este caso Jugadores y Enemigos.

# 3. Decorator: Dentro del ejercicio el patron decorator es el encargado de agregar un elemento extra a alguno de los jugadores, como implementacion, clonamos uno de los enemigos y adicionamos la clase "ImpostorDecorator" la cual se encarga de darle cualidades para eliminar enemigos mediante la funcion "killPlayer"  

# 4.Creacionales
Abstract factory, builder, factory method
Este tipo de patrón se utilizó para la versión del juego gon javascript y phaser que encontramos en el directorio agario
Se empleó la Construcción de clases, objetos y otras estructuras de datos.


Permiten crear diferentes instancias de objetos sin tener que preocuparnos de la forma en la que realmente se crean. Se usan cuando es necesario crear varios objetos y hay restricciones.
Ejemplo. Queremos crear player, food y opponents de distintas clases  desde un único punto, y que al crearlos se cree también una física por defecto (tamaño, dimensión, posicionamiento y velocidad) 
•	Abstract Factory. Se crean clases fábrica para cada tipo a crear, ofreciendo un punto desde el que crear lo que necesitemos.
•	Factory Method. Digamos que mete la funcionalidad en un método (redefinido en las subclases). Se utiliza para implementar el abstract factory.
•	Builder. Separa el proceso de cómo se crean las intancias de su representación jerárquica. Digamos que añade control del proceso (orden) a una fabrica abstracta.


# Authors: Julian David Rojas Ordoñez
# 20202099034

# Efren Abdenago Lopez Galvis
# 20202099029

# Edgar Junior Castro Escorcia
# 20202099024

