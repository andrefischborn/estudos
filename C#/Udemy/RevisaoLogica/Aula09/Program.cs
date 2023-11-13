using System;
using System.Globalization;

namespace Entradas2 {
    class Program {
        static void Main(string[] args) {


            int n1 = int.Parse(Console.ReadLine());
            char ch = char.Parse(Console.ReadLine());
            double n2 = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.WriteLine($"Você digitou: {n1} {ch} {n2.ToString("F2", CultureInfo.InvariantCulture)}");
            
            string[] vet = Console.ReadLine().Split(' ');
            string nome = vet[0];
            char sexo = char.Parse(vet[1]);
            int idade = int.Parse(vet[2]);
            double altura = double.Parse(vet[3], CultureInfo.InvariantCulture);
            
            Console.WriteLine($"{nome} tem {idade} anos, é do gênero {sexo}, e mede {altura.ToString(CultureInfo.InvariantCulture)} de altura.");
        }
    }
}
