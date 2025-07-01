// Incluimos la librería iostream para poder usar cout y cin
#include <iostream>

int main() {
    // Usamos 'cout' para mostrar un mensaje en la pantalla.
    // '<<' es el operador de inserción, envía el texto a cout.
    std::cout << "¡Hola, mundo!" << std::endl;

    int edad; // Declaramos una variable para guardar la edad.
    std::cout << "Introduce tu edad: ";
    // Usamos 'cin' para leer un número del teclado y guardarlo en 'edad'.
    // '>>' es el operador de extracción, toma el valor de cin y lo guarda en la variable.
    std::cin >> edad;

    std::cout << "Tienes " << edad << " años." << std::endl;
    return 0;
}