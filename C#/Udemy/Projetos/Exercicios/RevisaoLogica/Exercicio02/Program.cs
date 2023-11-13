using System;
using System.Globalization;

namespace Exercicio02 {
    class Program {
        static void Main(string[] args) {

            Console.WriteLine($"Entre com seu nome completo:");
            string nome = Console.ReadLine();

            Console.WriteLine($"Quantos quartos tem na sua casa?");
            int quartos = int.Parse(Console.ReadLine());

            Console.WriteLine("Entre com o preço de um produto:");
            double preco = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            Console.WriteLine("Entre seu último nome, idade e altura (na mesma linha):");
            string[] vet = Console.ReadLine().Split(' ');

            string ultimonome = vet[0];
            int idade = int.Parse(vet[1]);
            double altura = double.Parse(vet[2], CultureInfo.InvariantCulture);

            Console.WriteLine($"Seu nome completo é: {nome}");
            Console.WriteLine($"Sua casa tem {quartos} quartos.");
            Console.WriteLine($"O preço do seu produto é: {preco.ToString("f2", CultureInfo.InvariantCulture)}");

            Console.WriteLine($"Seu último nome é: {ultimonome}, você tem: {idade} e mede {altura.ToString("F2", CultureInfo.InvariantCulture)} de altura.");
        }
    }
}