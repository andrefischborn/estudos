using System;
namespace Aulas {
    class Aula12 {
        static void Main(string[] args) {

            Console.WriteLine("Que horas são?:");
            int hora = int.Parse(Console.ReadLine());

            if (hora < 6) {
                Console.WriteLine("Madrugada");
            }
            else if (hora < 12) {
                Console.WriteLine("Bom dia");
            }
            else if (hora < 18) {
                Console.WriteLine("Boa tarde");
            }
            else { 
                Console.WriteLine("Boa noite");
            }
        }
    }
}