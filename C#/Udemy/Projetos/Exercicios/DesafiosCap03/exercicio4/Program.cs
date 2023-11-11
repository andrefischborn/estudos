/* Fazer um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por 
hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas 
decimais
*/
using System;
using System.Globalization;

namespace Exercicios {
    class Exe04 {
        static void Main(string[] args) {
            Console.WriteLine("Digite o Número do funcionário:");
            double number = double.Parse(Console.ReadLine());

            Console.WriteLine("Digite quantas horas o funcionário trabalhou:");
            double ht = double.Parse(Console.ReadLine());

            Console.WriteLine("Digite o valor de hora dele:");
            double valorHora = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            double salario = (ht * valorHora);

            Console.WriteLine($"O Funcionário número: {number} recebe um salário de: {salario.ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}