using System;
namespace Aula02 {
    internal class Triangulo {

        public double A;    // O encapsulamento public permite que esse item seja acessado por outros arquivos .cs
        public double B;
        public double C;

        public double Area() {

            double P = (A + B + C) / 2.0;

            double raiz = Math.Sqrt(P * (P - A) * (P - B) * (P - C));
            return raiz;
        }
    }
}
