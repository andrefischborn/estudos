/*
Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar.
Exemplos:
Entrada: Saída:
12 PAR
Entrada: Saída:
-27 IMPAR
Entrada: Saída:
0 PAR
*/
using System;
namespace Desafios {
    class Desafio02 {
        static void Main(string[] args) {
            Console.WriteLine("Entre um número Inteiro:");
            int n1 = int.Parse(Console.ReadLine());
            if (n1 % 2 == 0) {  // O resto da divisão de um número par sempre da 0.
                Console.WriteLine("Número Par");
            }
            else {  // Resto da divisão se der diferente de 0 é porque é impar.
                Console.WriteLine("Número Impar");
            }
        }
    }
}