using System;

class aula05 {
    static void Main(){
        bool res0=(11<3)|(5<8); // False + True = True
        bool res1=(1<3)|(5<8); // True + True = True
        bool res2=(11<3)|(15<8); // False + False = False

        bool res3=(11<3)&(5<8); // False + True = False
        bool res4=(1<3)&(5<8); // True + True = True
        bool res5=(11<3)&(15<8); // False + False = False
        
        Console.WriteLine("Usando |:");
        Console.WriteLine(res0);
        Console.WriteLine(res1);
        Console.WriteLine(res2);
        Console.WriteLine("Usando &:");
        Console.WriteLine(res3);
        Console.WriteLine(res4);
        Console.WriteLine(res5);
    }
}