using System;

namespace Bhaskara {
    class Program {
        static void Main(string[] args) {

            double a = 1.0;
            double b = -3.0;
            double c = -4.0;
            double delta = Math.Pow(b, 2.0) - 4.0 * (a * c); // Math calcula o expoente de B elevado na 2.0
            double x1 = (-b + Math.Sqrt(delta)) / 2.0 * a;

            Console.WriteLine($"Os valores usados foram:");
            Console.WriteLine($"A = {a}, B = {b}, C = {c}");
            Console.WriteLine();
            Console.WriteLine($"O Delta da equação é: {delta} !");
            Console.WriteLine($"O resultado final da fórmula de Bhaskara é: {x1} !");
        }
    }
}