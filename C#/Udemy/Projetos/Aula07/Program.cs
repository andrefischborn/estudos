using System;

namespace Operadores {

    class Aritmeticos {
        static void Main() {

            double a = 17;
            double b = 3;
            double calculo = a % (b+b); 
            double calculo2 = a % b; // resto de 17 divido por 3 (mod) 

            Console.WriteLine(calculo);
            Console.WriteLine(calculo2);
        }
    }
}