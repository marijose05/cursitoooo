#include <iostream>
#include <vector>   
#include <string>   

int main() {
  
    std::vector<std::string> comidasFavoritas;
    std::string comidaTemporal;

    std::cout << "Por favor, introduce tus 3 comidas favoritas." << std::endl;

    
    for (int i = 0; i < 3; ++i) {
        std::cout << "Comida " << i + 1 << ": ";
        
        
        std::getline(std::cin >> std::ws, comidaTemporal); 
        
      
        comidasFavoritas.push_back(comidaTemporal);
    }

    std::cout << "\n--- Tus comidas favoritas son ---" << std::endl;

   
    for (int i = 0; i < comidasFavoritas.size(); ++i) {
        std::cout << "- " << comidasFavoritas[i] << std::endl;
    }

    return 0;
}
