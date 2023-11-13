using System;

namespace Aulas {
    class Aula10 {
        static void Main(string[] args) {

            int a = 10;
            bool c1 = a > 5;
            bool c2 = a <= 5;
            bool c3 = a != 5;
            bool c4 = a == 8;

            Console.WriteLine("Valor de A: 10");
            Console.WriteLine();
            Console.WriteLine($"A > 5? (maior): {c1}");
            
            Console.WriteLine($"A <= 5? (menor ou igual): {c2}");
            
            Console.WriteLine($"A != 5? (diferente): {c3}");
            
            Console.WriteLine($"A == 8? (identico): {c4}");
            
        }
    }
}