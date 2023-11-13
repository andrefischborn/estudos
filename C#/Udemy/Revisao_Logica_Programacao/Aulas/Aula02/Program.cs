using System;

namespace DadosBasicos {
    class DadosBasicos {
        static void Main(string[] args) {

            bool completo = false;
            byte n1 = 125;
            int n2 = 1000;
            int n3 = 2147483647;
            long n4 = 2147483648l;  // devemos colocar l no final para o programa entender que é um dado long.
            char genero = 'F';
            char letra = '\u0041';  // Ver a tabela unicode no google.
            float n5 = 4.5f;    // para float devemos colocar o f no final, ou o programa entende que é double.
            double n6 = 4.5;
            string nome = "Maria João";
            object obj1 = "João";
            object obj2 = 4.5f;
            int max = int.MaxValue; // esse dado faz imprimir o maior valor que aquela variável suporta
            int min = int.MinValue; // esse faz o contrário.
            decimal maxdecimal = decimal.MaxValue;

            Console.WriteLine(completo);
            Console.WriteLine(n1);
            Console.WriteLine(n2);
            Console.WriteLine(n3);
            Console.WriteLine(n4);
            Console.WriteLine(genero);
            Console.WriteLine(letra);
            Console.WriteLine(n5);
            Console.WriteLine(n6);
            Console.WriteLine(nome);
            Console.WriteLine(obj1);
            Console.WriteLine(obj2);
            Console.WriteLine(min);
            Console.WriteLine(max);
            Console.WriteLine(maxdecimal);
        }
    }
}