// Trabalhando com escopo de variáveis
using System;

namespace aula04 {
    class aula04 {
        int num1=10;
        static void Main() {
            int num2=20;
            Console.WriteLine(num2);
        }
        void Teste(){
            int num3=4;
            Console.WriteLine(num1);
        }
    }
}