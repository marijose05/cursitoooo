#include <iostream>


void modificarPorValor(int val) {
    std::cout << "  (Dentro de 'modificarPorValor') El valor recibido es: " << val << std::endl;
    val += 10;
    std::cout << "  (Dentro de 'modificarPorValor') El valor ahora es: " << val << std::endl;
}


void modificarPorReferencia(int &ref) {
    std::cout << "  (Dentro de 'modificarPorReferencia') El valor recibido es: " << ref << std::endl;
    ref += 10;
    std::cout << "  (Dentro de 'modificarPorReferencia') El valor ahora es: " << ref << std::endl;
}

int main() {
    int numero = 20;

    std::cout << "--- Demostracion de Paso por Valor ---" << std::endl;
    std::cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << std::endl;
    modificarPorValor(numero);
    std::cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (SIN CAMBIOS)" << std::endl;
    
    std::cout << "\n--- Demostracion de Paso por Referencia ---" << std::endl;
    std::cout << "Valor de 'numero' ANTES de llamar a la funcion: " << numero << std::endl;
    modificarPorReferencia(numero);
    std::cout << "Valor de 'numero' DESPUES de llamar a la funcion: " << numero << " (¡CAMBIO!)" << std::endl;

    return 0;
}
