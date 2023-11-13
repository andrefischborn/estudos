/* Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva 
um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 
1.Álcool 2.Gasolina 3.Diesel 4.Fim). 
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até 
que seja válido). O programa será encerrado quando o código informado for o número 4. Deve ser escrito a 
mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme 
exemplo
*/

using System;
namespace Desafios {
    class Program {
        static void Main(string[] args) {
            string tipo = "Não foi abastecido";
            int gasolina = 0;
            int alcool = 0;
            int diesel = 0;

            Console.WriteLine("Seja bem vindo!");
            Console.WriteLine("Digite o código do tipo de combustível será abastecido:");
            Console.WriteLine("1.Álcool\t  2.Gasolina\t  3.Diesel\t  4.Cancelar");
            int codigo = int.Parse(Console.ReadLine());

            while (codigo != 4) {
                if (codigo == 1) {
                    tipo = "Você abasteceu com: Álcool.";
                    alcool++;
                }
                else if (codigo == 2) {
                    tipo = "Você abasteceu com: Gasolina.";                  
                    gasolina++;
                }
                else if (codigo == 3) {
                    tipo = "Você abasteceu com: Diesel.";
                    diesel++;
                }
                else if (codigo > 4) {
                    tipo = "Código Inválido";
                }
                Console.Clear();    // comando para limpar o console e deixar enxuto
                Console.WriteLine($"{tipo}");
                Console.WriteLine("Continuar abastecendo?");
                Console.WriteLine("1.Álcool\t  2.Gasolina\t  3.Diesel\t  4.Finalizar");
                codigo = int.Parse(Console.ReadLine());
            }
            if (codigo == 4) {
                Console.WriteLine("Você finalizou o caixa.");
            }
            Console.Clear();
            Console.WriteLine($"VENDAS DO DIA:");
            Console.WriteLine($"PRODUTO:\t VENDAS:");
            Console.WriteLine($"Gasolina...:\t {gasolina}");
            Console.WriteLine($"Alcool.....:\t {alcool}");
            Console.WriteLine($"Diesel.....:\t {diesel}");
            Console.WriteLine("MUITO OBRIGADO.");
        }
    }
}