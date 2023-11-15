/* Fazer um programa para ler nome e salário de dois funcionários. Depois, mostrar o salário 
médio dos funcionários
*/

using System;
using System.Globalization;

namespace Exercicio02 {
    class Program {
        static void Main(string[] args) {
            Dados x, y;
            x = new Dados();
            y = new Dados();

            Console.WriteLine("Vamos analisar o salário médio:");
            Console.Write("Insira o nome do funcionário 1: ");
            x.nome = Console.ReadLine();
            Console.Write("Insira o Salário do funcionário 1: ");
            x.salario = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.Clear();
            Console.WriteLine("Vamos analisar o salário médio:");
            Console.Write("Insira o nome do funcionário 2: ");
            y.nome = Console.ReadLine();
            Console.Write("Insira o Salário do funcionário 2: ");
            y.salario = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            double media  = (x.salario + y.salario) / 2;

            Console.Clear();
            Console.WriteLine($"FUNCIONÁRIO:\t SALÁRIO:");
            Console.WriteLine($"{x.nome}\t {x.salario.ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"{y.nome}\t {y.salario.ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"MÉDIA: {media.ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
