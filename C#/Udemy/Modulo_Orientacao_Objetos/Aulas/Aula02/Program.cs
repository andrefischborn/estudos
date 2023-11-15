/* ESTE É UM PROGRAMA SEM ORIENTAÇÃO A OBJETOS:
        Para fazer esse programa foi usado vários códigos repetidos e muitas linhas

Pedido:
Fazer um programa para ler as medidas dos lados de dois triângulos X e Y (suponha medidas
válidas). Em seguida, mostrar o valor das áreas dos dois triângulos e dizer qual dos dois triângulos
possui a maior área.
A fórmula para calcular a área de um triângulo a partir das medidas de seus lados a, b e c é a
seguinte (fórmula de Heron):
                    p = a + b + c / 2
                    area = RAIZ DE: p*( p - a)*( p - b)*( p - c) 
*/

using System;
using System.Globalization;

namespace Aula02 {
    class Program {
        static void Main(string[] args) {

            Triangulo x, y;
            x = new Triangulo();
            y = new Triangulo();

            Console.WriteLine("Entre os valores (válidos) de dois triângulos e vamos ver qual possui maior área.");

            Console.WriteLine("VALORES DO TRIÂNGULO 1:");
            Console.Write("Valor do lado A: ");
            x.A = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Valor do lado B: ");
            x.B = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Valor do lado C: ");
            x.C = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            double areaX = x.Area();

            Console.WriteLine("VALORES DO TRIÂNGULO 2:");
            Console.Write("Valor do lado A: ");
            y.A = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Valor do lado B: ");
            y.B = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Valor do lado C: ");
            y.C = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            double areaY = y.Area();

            Console.Clear();
            Console.WriteLine($"Área do Triângulo 1: {areaX.ToString("F4", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"Área de Triângulo 2: {areaY.ToString("F4", CultureInfo.InvariantCulture)}");
            if (areaX > areaY) {
                Console.WriteLine($"Maior Área: TRIANGULO 1!");
            }
            else {
                Console.WriteLine($"Maior Área: TRIANGULO 2!");
            }
        }
    }
}

