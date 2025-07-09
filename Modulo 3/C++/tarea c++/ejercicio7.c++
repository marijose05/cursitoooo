#include <iostream>

float calcularAreaRectangulo(float base, float altura);

int main() {
    float baseUsuario, alturaUsuario;

    
    std::cout << "Introduce la base del rectangulo: ";
    std::cin >> baseUsuario;
    std::cout << "Introduce la altura del rectangulo: ";
    std::cin >> alturaUsuario;

   
    float area = calcularAreaRectangulo(baseUsuario, alturaUsuario);

    
    std::cout << "El area del rectangulo es: " << area << std::endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    
    return base * altura;
}
