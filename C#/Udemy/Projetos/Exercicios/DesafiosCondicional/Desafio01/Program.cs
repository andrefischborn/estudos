/*Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não.
Exemplos:
Entrada: Saída:
-10 NEGATIVO
Entrada: Saída:
8 NAO NEGATIVO
Entrada: Saída:
0 NAO NEGATIVO
*/
using System;

namespace Desafios {
    class Desafio01 {
        static void Main(string[] args) {

            Console.WriteLine("Entre um Número Inteiro:");
            int n1 = int.Parse(Console.ReadLine());

            if (n1 < 0) {
                Console.WriteLine("NEGATIVO");
            }
            else {
                Console.WriteLine("NAO NEGATIVO");
            }

        }
    }
}