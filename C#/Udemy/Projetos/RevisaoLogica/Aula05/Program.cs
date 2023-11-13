using System;

namespace Aula5 {
    class Aula5 {
        static void Main(string[] args) {

            int idade = 32;
            double saldo = 10.35784;
            string nome = "Maria";

            Console.WriteLine("{0} tem {1} anos e seu saldo é de {2:F2} reais",nome,idade,saldo); // placeholder
            Console.WriteLine($"{nome} tem {idade} anos e seu saldo é de {saldo:f2} reais."); // interpolação
            Console.WriteLine(nome + " tem " + idade + " anos" + " e seu saldo é de " + saldo.ToString("F2") + " reais."); // concatenação
        }
    }
}