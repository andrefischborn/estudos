/*
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos 
seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em 
nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”
*/
using System;
namespace Desafios {
    class Desafio06 {
        double intervalo = 0;
        static void Main(string[] args) {
            
            Console.WriteLine("Digite um número: ");
            double intervalo = double.Parse(Console.ReadLine());

           if (intervalo >= 0 && intervalo <= 25  ) {
                Console.WriteLine("O número encontra-se no intervalo: [0,25]");
            }
           else if (intervalo > 25 && intervalo <= 50) {
                Console.WriteLine("O número encontra-se no intervalo: [25,50]");
            }
            else if (intervalo > 50 && intervalo <= 75) {
                Console.WriteLine("O número encontra-se no intervalo: [50,75]");
            }
            else if (intervalo > 75 && intervalo <= 100) {
                Console.WriteLine("O número encontra-se no intervalo: [75,100]");
            }
            else {
                Console.WriteLine("O número encontra-se Fora de Intervalo");
            }

        }
    }
}