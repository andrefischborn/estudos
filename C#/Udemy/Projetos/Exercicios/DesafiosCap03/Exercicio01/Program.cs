// Faça um programa para ler dois valores inteiros, e depois mostrar na tela a soma 
// desses números com uma mensagem explicativa, conforme exemplos
//  Entrada: 
//  10
//  30
//  Saída:
//  SOMA = 4

Console.WriteLine("Digite um número inteiro");
int n1 = int.Parse(Console.ReadLine());
Console.WriteLine("Digite outro número inteiro");
int n2 = int.Parse(Console.ReadLine());
int resultado = (int)n1 + (int)n2;
Console.WriteLine($"A soma de {n1} + {n2} é: {resultado}");