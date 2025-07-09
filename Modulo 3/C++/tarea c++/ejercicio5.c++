#include <iostream>

int main() {
    int numeroSecreto = 42;
    int intentoUsuario = 0; 

    std::cout << "¡Adivina el numero secreto (entre 1 y 100)!" << std::endl;

    while (intentoUsuario != numeroSecreto) {
        std::cout << "Introduce tu intento: ";
        std::cin >> intentoUsuario;

        if (intentoUsuario < numeroSecreto) {
            std::cout << "El numero secreto es mas alto." << std::endl;
        } else if (intentoUsuario > numeroSecreto) {
            std::cout << "El numero secreto es mas bajo." << std::endl;
        }
    }

   std::cout << "¡Felicidades! Adivinaste el numero secreto: " << numeroSecreto << std::endl;

    return 0;
}