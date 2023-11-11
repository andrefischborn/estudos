using System;   // Biblioteca básica

namespace aula02    // Namespace é uma forma de organizar os objetos. É um local.
{
    class Program 
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            Console.WriteLine(args.GetValue(0)); // devemos colocar um parametro na hora de rodar o programa no terminal ou vai dar erro. Ex: program teste
            Console.WriteLine("teste");
        }
    }
}
