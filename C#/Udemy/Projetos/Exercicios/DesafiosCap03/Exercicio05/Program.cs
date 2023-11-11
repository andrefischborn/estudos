/* Fazer um programa para ler
o código de uma peça: 1, 
o número de peças 1, 
valor unitário de cada peça 1, 
o código de uma peça 2, 
o número de peças 2 
o valor unitário de cada peça 2. 
Calcule e mostre o valor a ser pago
*/

using System;
using System.Globalization;

namespace Exercicios {
    class Exe05 {
        static void Main(string[] args) {

            Console.WriteLine($"Digite o Código, Quantidade e Valor do primeiro produto:");
            string[] entrada1 = Console.ReadLine().Split(' ');

            double codigoPeca1 = double.Parse(entrada1[0]);
            double numeroDePecas1 = double.Parse(entrada1[1]);
            double valorPeca1 = double.Parse(entrada1[2],CultureInfo.InvariantCulture);

            Console.WriteLine($"Digite o Código, Quantidade e Valor do segundo produto:");
            string[] entrada2 = Console.ReadLine().Split(' ');

            double codigoPeca2 = double.Parse(entrada2[0]);
            double numeroDePecas2 = double.Parse(entrada2[1]);
            double valorPeca2 = double.Parse(entrada2[2],CultureInfo.InvariantCulture);

            double valorPagar = (numeroDePecas1 * valorPeca1) + (numeroDePecas2 * valorPeca2);

            Console.WriteLine();
            Console.WriteLine("PEDIDO:");
            Console.WriteLine($"COD:{codigoPeca1} QTD:{numeroDePecas1} VALOR: {valorPeca1:F2}");
            Console.WriteLine($"COD:{codigoPeca2} QTD:{numeroDePecas2} VALOR: {valorPeca2:F2}");
            Console.WriteLine($"VALOR A PAGAR: {valorPagar:F2}");


        }
    }
}