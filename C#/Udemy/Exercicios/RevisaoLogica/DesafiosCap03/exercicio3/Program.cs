/*
 Fazer um programa para ler quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto 
de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada:
5
6
7
8
Saída: DIFERENCA = -26

 */
using System;
Console.WriteLine("Digite um númeiro inteiro para A:");
int a = int.Parse(Console.ReadLine());
Console.WriteLine("Digite um númeiro inteiro para B:");
int b = int.Parse(Console.ReadLine());
Console.WriteLine("Digite um númeiro inteiro para C:");
int c = int.Parse(Console.ReadLine());
Console.WriteLine("Digite um númeiro inteiro para D:");
int d = int.Parse(Console.ReadLine());
double diferenca = (a * b - c * d);

Console.WriteLine($"A diferença entre os números {a},{b},{c},{d} é: {diferenca}");