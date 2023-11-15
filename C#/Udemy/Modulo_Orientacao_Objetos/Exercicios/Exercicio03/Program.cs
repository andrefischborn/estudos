/* Fazer um programa para ler os valores da largura e altura 
de um retângulo. Em seguida, mostrar na tela o valor de 
sua área, perímetro e diagonal. Usar uma classe como 
mostrado no projeto ao lado. Exemplo:
Entre a largura e altura do retângulo
3.00
4.00
AREA = 12.00
PERÍMETRO = 14.00
DIAGONAL = 5.00
*/
using System;
using System.Globalization;

namespace Exercicios {
    class Program {
        static void Main(string[] args) {

            Retangulo ret;
            ret = new Retangulo();
            

            Console.Write("Entre o valor da Largura: ");
            ret.Largura = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Entre o valor da Altura: ");
            ret.Altura = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);

            

            Console.WriteLine($"AREA = {ret.Area().ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"PERIMETRO = {ret.Perimetro().ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"DIAGONAL = {ret.Diagonal().ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}