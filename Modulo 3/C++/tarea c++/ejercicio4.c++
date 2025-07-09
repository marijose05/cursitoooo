#include <iostream>
#define LIMITE 10

int main() {
    int numero;

    std::cout << "Introduce un numero para ver su tabla de multiplicar: ";
    std::cin >> numero;
    std::cout << "----------------------------------------------------" << std::endl;

    std::cout << "Tabla de multiplicar del " << numero << ":" << std::endl;

   
    for (int i = 1; i <= LIMITE; ++i) {
        std::cout << numero << " x " << i << " = " << (numero * i) << std::endl;
    }

    return 0;
}
