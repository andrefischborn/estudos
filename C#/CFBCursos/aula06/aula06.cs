using System;

class aula06 {
    static void Main() {
        int n1,n2,n3;

        n1=10; n2=20; n3=30;

        Console.WriteLine(n1 + "," + n2 + "," + n3); // essa é uma forma de fazer, porém temos outra formatada:
        Console.Write("n1={0}, n2={1}, n3={2}",n1,n2,n3); // aqui utilizamos indices. A n1 tá na posição1, n2 na posição2...
        Console.Write("\nn1={0}\nn2={1}\nn3={2}\n",n1,n2,n3); // Usando caractere de escape \n (mesma coisa que um enter, nova linha)
        Console.Write("\nn1=\t{0}\nn2=\t{1}\nn3=\t{2}\n",n1,n2,n3); // Usando caractere de escape \t (tabulação)
    }
}