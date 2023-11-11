/*
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao 
Multiplos", indicando se os valores lidos são múltiplos entre si. Atenção: os números devem poder ser digitados em 
ordem crescente ou decrescente.
Exemplos:
Entrada: Saída:
6 24 Sao Multiplos
Entrada: Saída:
6 25 Nao sao Multiplos
Entrada: Saída:
24 6 Sao Multiplo
*/

using System;
namespace Desafios {
    class Desafio03 {
        static void Main(string[] args) {
            Console.WriteLine("Digite um valor para A:");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite um valor para B:");
            int b = int.Parse(Console.ReadLine());
            
            if (a % b == 0 || b% a == 0) {
                Console.WriteLine("São Multiplos");

            }
            else {
                Console.WriteLine("Não são multiplos");
            }
        }
    }
}