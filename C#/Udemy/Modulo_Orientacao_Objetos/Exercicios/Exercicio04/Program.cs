/* Fazer um programa para ler os dados de um funcionário (nome, 
salário bruto e imposto). Em seguida, mostrar os dados do 
funcionário (nome e salário líquido). Em seguida, aumentar o salário 
do funcionário com base em uma porcentagem dada (somente o 
salário bruto é afetado pela porcentagem) e mostrar novamente os 
dados do funcionário. Use a classe projetada abaixo
*/
using Exercicios;
using System;
using System.Globalization;

namespace Exercicios {
    class Program {
        static void Main(string[] args) {
            Funcionario Colaborador;
            Colaborador = new Funcionario();

            Console.Write("Digite o nome do funcionário: ");
            Colaborador.Nome = Console.ReadLine();
            Console.Write("Digite o salário bruto do funcionário: ");
            Colaborador.SalarioBruto = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Digite o valor de imposto a ser pago: ");
            Colaborador.Imposto = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.WriteLine($"Nome: {Colaborador.Nome}");
            Console.WriteLine($"Salário Bruto: {Colaborador.SalarioBruto.ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"Imposto: {Colaborador.Imposto.ToString("F2", CultureInfo.InvariantCulture)}");

            Console.WriteLine("Funcionário: " + Colaborador);

            Console.WriteLine();
            Console.Write("Digite a porcentagem para aumentar o salário: ");
            double aumento = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Colaborador.AumentarSalario(aumento);

            Console.WriteLine("Dados Atualizados: " + Colaborador);
            
        }
    }
}