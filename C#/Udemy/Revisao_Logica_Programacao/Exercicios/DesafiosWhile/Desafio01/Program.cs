/*
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha 
incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser 
impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.
*/
using System;

namespace Desafios {
    class Program {
        static void Main(string[] args) {

            Console.Write("Para continuar, digite sua senha: ");
            int senha = int.Parse(Console.ReadLine());

            int senhaSalva = 2002;

            while (senha != senhaSalva) {
                Console.WriteLine("senha Inválida!");

                Console.Write("Digite novamente: ");
                senha = int.Parse(Console.ReadLine());
            }
            Console.WriteLine("Senha Correta! Pode prosseguir.");
        }

    }
}