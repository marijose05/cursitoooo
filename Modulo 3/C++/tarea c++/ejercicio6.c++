#include <iostream>

int main() {
    int opcion;

    
    do {
    
        std::cout << "\n--- MENU ---" << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Elige una opcion: ";
        std::cin >> opcion;

    
        switch (opcion) {
            case 1:
                std::cout << "¡Hola! Que tengas un buen dia." << std::endl;
                break; 
            case 2:
                std::cout << "¡Adios! Vuelve pronto." << std::endl;
                break;
            case 3:
                std::cout << "Saliendo del programa..." << std::endl;
                break;
            default: 
                std::cout << "Opcion no valida. Por favor, intenta de nuevo." << std::endl;
                break;
        }

    } while (opcion != 3); 

    return 0;
}