/*
Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e 
mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B.
Entrada: 
3.0 4.0 5.2 
Saída:
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
*/
using System;
using System.Globalization;

namespace Exercicios {
    class Exe06 {
        static void Main(string[] args) {

            Console.WriteLine("Digite Três valores para: A B C (na mesma linha):");
            string[] entrada = Console.ReadLine().Split(' ');
            double a = double.Parse(entrada[0], CultureInfo.InvariantCulture);
            double b = double.Parse(entrada[1], CultureInfo.InvariantCulture);
            double c = double.Parse(entrada[2], CultureInfo.InvariantCulture);

            double pi = 3.14159;

            double triangulo = a * c / 2.0;
            double circulo = pi * (c * c);
            double trapezio = (a + b) / (2.0 * c);
            double quadrado = b * b;
            double retangulo = a * b;

            Console.WriteLine($"TRIÂNGULO: {triangulo.ToString("F3", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"CIRCULO: {circulo.ToString("F3", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"TRAPÉZIO: {trapezio.ToString("F3", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"QUADRADO: {quadrado.ToString("F3", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"RETÂNGULO: {retangulo.ToString("F3", CultureInfo.InvariantCulture)}");
        }
    }
}
