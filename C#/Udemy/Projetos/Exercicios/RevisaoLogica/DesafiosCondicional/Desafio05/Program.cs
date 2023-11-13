/*
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A 
seguir, calcule e mostre o valor da conta a pagar.

COD     ESPECIFICAÇÃO       PREÇO
1       Cachorro Quente     4.00
2       X-Salada            4.50
3       X-Bacon             5.00
4       Torrada Simples     2.00
5       Refrigerante        1.50

*/
using System;
using System.Globalization;

namespace Desafios {
    class Desafio05 {
        static  void Main(string[] args) {

            double total = 0;
            string produto = "Produto Inválido";

            string produto1 = "Cachorro Quente";
            string produto2 = "X-Salada";
            string produto3 = "X-Bacon";
            string produto4 = "Torrada Simples";
            string produto5 = "Refrigerante";

            Console.WriteLine("Digite o Código do Produto e a Quantidade:");
            string[] valores = Console.ReadLine().Split(' ');
            int codigo = int.Parse(valores[0]);
            int quantidade = int.Parse(valores[1]);

            if (codigo == 1) {
                total = quantidade * 4.0;
                produto = produto1;
            }
            else if (codigo == 2) {
                total = quantidade * 4.5;
                produto = produto2;
            }
            else if (codigo == 3) {
                total = quantidade * 5.0;
                produto = produto3;
            }
            else if (codigo == 4) {
                total = quantidade * 5.0;
                produto = produto4;
            }
            else if (codigo == 5) {
                total = quantidade * 1.5;
                produto = produto5;
            }
            else {
                Console.WriteLine("Código Inválido!");
            }
            Console.WriteLine("-------------------");
            Console.WriteLine("SEU PEDIDO:");
            Console.WriteLine("CÓDIGO:\t | PRODUTO:\t\t\t | QUANTIDADE:\t | TOTAL:"); // esse: \t faz o papel de uma tabulação, um TAB
            Console.WriteLine($"{codigo}\t | {produto}\t\t | {quantidade}\t\t | {total.ToString("F2", CultureInfo.InvariantCulture)} ");

        }
    }
}