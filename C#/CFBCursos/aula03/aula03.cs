using System;

class Aula03
{
    static void Main()
    {
        int num=10;              // Usado para números inteiros
        char letra='c';          // usado para apenas UM CARACTERE. Deve ser usado entre ASPAS SIMPLES
        float valor=5.3f;        // Usado para números não inteiros
        string nome="Gabriel";   // usado para Frases ou palavras. Deve ser colocado com ASPAS DUPLAS
        var aux=num;             // Aqui podemos colocar qualquer dado no Var. Pode ser outra variável, um INT, uma STRING...

        Console.WriteLine(aux + " " + nome + " Teste");  // Podemos concatenar dados, usando o +. No exemplo concatenamos 2 variáveis e uma palavra.
    }
}