#include <iostream>
#include <fstream> 
#include <string>

int main(void){

    std::string crop;
    std::string rainfall;
    float pH;
    int month;

    std::ofstream outputFile("input.txt", std::ios::app);

     if (!outputFile.is_open()) {
        std::cerr << "Error: Could not open the file for writing." << std::endl;
        return 1; // Indicate an error
    }

    while(true){
        std::cout<<"Farmer input interface:"<<std::endl;
        // [Crop] [Rainfall] [Soil pH] [Planting month] 
        std::cout<<"Enter data(space separated) or 'exit' to quit."<<std::endl;
        std::cin>> crop;
        if(crop == "exit"){
            break;
        }
        std::cin>> rainfall;
        std::cin>> pH;
        while(pH<4 || pH >8){
            std::cout<<"Value out of bounds. Enter correct pH."<<std::endl;
            std::cin>> pH;  
        }
        std::cin>> month;
        while(month<1 || month >12){
            std::cout<<"Value out of bounds. Enter correct month."<<std::endl;
            std::cin>> month;  
        }

        std::string input = crop+","+rainfall+","+std::to_string(pH)+","+std::to_string(month);
        outputFile << input<< std::endl;
    }

    system("python predict.py");

    std::ifstream inputFile("results.txt");

    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open the file." << std::endl;
        return 1;
    }

     std::string line;
    while (std::getline(inputFile, line)) {
        std::cout << line << std::endl;
    }

    inputFile.close();
    outputFile.close();

    return 0;
}