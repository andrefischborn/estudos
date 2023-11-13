/* Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o 
X, se for o caso
*/

using System;
namespace Desafios {
    class Program {
        static void Main(string[] args) {

            Console.WriteLine("Digite um valor inteiro: ");
            int X = int.Parse(Console.ReadLine());

            for (int i = 1; i <= X; i++) {  // Inicio: i=1 ; Condição: i<=x ; i = i+1
                if (i % 2 != 0) {   //  Se o resto da divisão de i dividido por 2 der diferente de 0, então ele é impar.
                    Console.WriteLine(i);
                }
            }
        }
    }
}