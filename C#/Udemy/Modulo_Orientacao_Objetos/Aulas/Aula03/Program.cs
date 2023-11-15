using Aula03;
using System;
using System.Globalization;

namespace Curso {
    class Program {
        static void Main(string[] args) {

            Produto p = new Produto();

            Console.WriteLine("Entre os dados do produto:");
            Console.Write("Nome do Produto: ");
            p.Nome = Console.ReadLine();
            Console.Write("Preço do Produto: ");
            p.Preco = double.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
            Console.Write("Quantidade no estoque: ");
            p.Quantidade = int.Parse(Console.ReadLine());

            Console.WriteLine("Dados do produto:");
            Console.WriteLine(p);

            Console.WriteLine();
            Console.Write("Digite o número de produtos a ser adicionados ao estoque: ");
            int qte = int.Parse(Console.ReadLine());
            p.AdicionarProdutos(qte);

            Console.Clear();
            Console.WriteLine($"Dados atualizados: {p}");
            Console.Write("Digite o número de produtos a ser removidos ao estoque: ");
            int rmv = int.Parse(Console.ReadLine());
            p.RemoverProdutos(rmv);

            Console.Clear();
            Console.WriteLine($"Dados atualizados: {p}");
        }
    }
}