/* UTILIZANDO ORIENTAÇÃO A OBJETOS
Fazer um programa para ler os dados de duas pessoas, depois mostrar o nome da pessoa mais 
velha.*/

using Exercicio01;
using System;

namespace Desafios {
    class Program {
        static void Main() {

            Dados x, y;

            x = new Dados();
            y = new Dados();

            Console.WriteLine("Insira os dados:");
            Console.Write("Nome da pessoa 1: "); 
            x.nome = Console.ReadLine();
            Console.Write("Idade da pessoa 1: ");
            x.idade = int.Parse(Console.ReadLine());
            Console.Clear();
            Console.WriteLine("Insira os dados:");
            Console.Write("Nome da pessoa 2: ");
            y.nome = Console.ReadLine();
            Console.Write("Idade da pessoa 2: ");
            y.idade = int.Parse(Console.ReadLine());
            Console.Clear();
            Console.WriteLine($"Foi cadastrado {x.nome} com {x.idade} anos, e {y.nome} com {y.idade} anos.");

            if (x.idade > y.idade) {
                Console.WriteLine($"{x.nome} é a pessoa mais velha.");
            }
            else
            {
                Console.WriteLine($"{y.nome} é a pessoa mais velha.");
            }
        }
    }
}