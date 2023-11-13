using System;

namespace Entradas {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Digite uma Frase para armazenar na variável 'Frase':");
            string frase = Console.ReadLine();
            

            Console.WriteLine("Digite uma Cor:");
            string x = Console.ReadLine();
            Console.WriteLine("Digite outra Cor:");
            string y = Console.ReadLine();
            Console.WriteLine("Digite outra Cor:");
            string z = Console.ReadLine();

            Console.WriteLine("Agora digite 3 cores na mesma linha:");

            string[] cores = Console.ReadLine().Split(' ');
            string a = cores[0];
            string b = cores[1];
            string c = cores[2];

            Console.WriteLine($"A frase que você sugeriu foi: {frase}");
            Console.WriteLine($"Suas três primeiras cores escolhidas foram:");
            Console.WriteLine(x);
            Console.WriteLine(y);
            Console.WriteLine(z);
            Console.WriteLine($"As outras cores escolhidas foram: {a}, {b} e {c}");
        }
    }
}