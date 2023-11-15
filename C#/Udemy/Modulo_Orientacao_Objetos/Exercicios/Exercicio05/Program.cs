/* Fazer um programa para ler o nome de um aluno e as três notas que ele obteve nos três trimestres do ano 
(primeiro trimestre vale 30 e o segundo e terceiro valem 35 cada). Ao final, mostrar qual a nota final do aluno no 
ano. Dizer também se o aluno está APROVADO ou REPROVADO e, em caso negativo, quantos pontos faltam 
para o aluno obter o mínimo para ser aprovado (que é 60 pontos). Você deve criar uma classe Aluno para resolver 
este problema
*/

using System;
using System.Globalization;

namespace Exercicios {
    class Program {
        static void Main(string[] args) {

            Aluno n;
            n = new Aluno();

            Console.Write("Nome do aluno: ");
            n.Nome = Console.ReadLine();

            Console.WriteLine("Digite as três notas do aluno:");

            Console.Write("Nota1: ");
            n.Nota1 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Nota2: ");
            n.Nota2 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Nota3: ");
            n.Nota3 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.WriteLine($"NOTA FINAL: {n.NotaFinal().ToString("F2", CultureInfo.InvariantCulture)}");
            if (n.Aprovado()) {
                Console.WriteLine("APROVADO");
            }
            else {
                Console.WriteLine("REPROVADO");
                Console.WriteLine($"FALTOU: {n.NotaRestante().ToString("F2", CultureInfo.InvariantCulture)} PONTOS.");
            }
        }
    }
}