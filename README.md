# Patrones de diseño que posiblemente se podrian usar para el desarrollo del video juego Agar.io

# 1. Prototype: Con este patron podremos clonar objetos en tiempo de ejecución, se implemento en la creacion de fichas a "comer" por todos los jugadores, como dichos elementos no cambian en su composicion o estructura, generamos una clonacion del objeto bajo la funcion "getClon" y "putClon" las cuales nos permiten capturar la estructura de una ficha "reina" para luego agregarla al final de la cola para posterior mostrarla en pantalla

# 2. Builder: La implementacion del patron Builder se realizo para realizar la instancia de un nuevo jugador dentro del tablero, dado que todos los jugadores tienen unos parametros iniciales, pero pueden tener existir jugadores con comportamientos distontos lo cual a traves de las funciones "buildCamera", "buildPosition" y "buildRandomMovement" extendimos nuevos atributos que contendra el nuevo jugador o "Player", diferentes a los atributos que se usan para el jugador "Enemy", este tipo de patrón se usa cuando es necesario crear varios objetos y hay restricciones en este caso Jugadores y Enemigos.

# 3. Decorator: Dentro del ejercicio el patron decorator es el encargado de agregar un elemento extra a alguno de los jugadores, como implementacion, clonamos uno de los enemigos y adicionamos la clase "ImpostorDecorator" la cual se encarga de darle cualidades para eliminar enemigos mediante la funcion "killPlayer"  


