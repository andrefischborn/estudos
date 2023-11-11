/* Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro 
casas decimais conforme exemplos.
Fórmula da área: area = π.raio2
Considere o valor de π = 3.14159 */
using System;
using System.Globalization;

namespace Exercicios {
    class Exe02 {
        static void Main(string[] args) {

            Console.WriteLine("Digite um valor de área para calcular o raio.");
            double raio = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            double pi = 3.14159;
            double resultado = (double)pi * Math.Pow(raio, 2);

            Console.WriteLine($"O valor do raio da área: {raio.ToString("F2", CultureInfo.InvariantCulture)} é de: {resultado.ToString("f4", CultureInfo.InvariantCulture)}");
        }
    }
}