using System;

class aula06 {
    static void Main() {

        double valorCompra=5.50;
        double valorVenda;
        double lucro=0.3;
        string produto="Pastel";

        valorVenda=valorCompra+(valorCompra*lucro);

        Console.WriteLine("Produto..........: {0,15}",produto);   // 0 = index e 15 = numero de espaços, tipo uma tab
        Console.WriteLine("Valor de compra..: {0,15:c}",valorCompra);   // o c representa que será um valor de dinheiro, vai colocar moeda $
        Console.WriteLine("Lucro............: {0,15:p}",lucro); // o p representa porcentagem e vai colocar o simbolo %
        Console.WriteLine("Valor de Venda...: {0,15:c}",valorVenda);    // o c representa que será um valor de dinheiro, vai colocar moeda $
    }

}