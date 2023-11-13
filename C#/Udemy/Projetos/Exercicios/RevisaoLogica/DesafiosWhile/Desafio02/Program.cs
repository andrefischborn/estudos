/* Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema 
cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo 
menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma)

*/
using System;
namespace Desafios {
    class Program {
        static void Main(string[] args) {

            Console.WriteLine("Entre dois números para as coordenadas (X e Y): ");

            string[] coordenadas = Console.ReadLine().Split(' ');
            double x = double.Parse(coordenadas[0]);
            double y = double.Parse(coordenadas[1]);

            while (x != 0 && y != 0) {

                if (x > 0 && y > 0) {
                    Console.WriteLine($"Essas coordenadas estão no quadrante 1");
                }
                else if (x < 0 && y > 0) {
                    Console.WriteLine($"Essas coordenadas estão no quadrante 2");
                }
                else if (x < 0 && y < 0) {
                    Console.WriteLine($"Essas coordenadas estão no quadrante 3");
                }
                else {
                    Console.WriteLine($"Essas coordenadas estão no quadrante 4");
                }
                Console.WriteLine("Entre dois números para as coordenadas (X e Y): ");

                coordenadas = Console.ReadLine().Split(' ');
                x = double.Parse(coordenadas[0]);
                y = double.Parse(coordenadas[1]);
            }
            Console.WriteLine("Coordenadas nulas!");
        }
    }
}