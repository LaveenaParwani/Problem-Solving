import java.util.Scanner;

abstract class 
{
    abstract int add(int a, int b);
}
class Adder extends Calculator
{  
        public int add(int a, int b)
        {
            int sum = a + b; 
 
    	}
}
/*
 Write the Adder class here. Do not use an access modifier at the beginning of your class declaration.
 */
public class Add {
    public static void main(String[] args) 
    {
        int a, b;
        try (Scanner scan = new Scanner(System.in)) 
	{
            a = scan.nextInt();
            b = scan.nextInt();
        }

        Calculator adderObject = new Adder();
        System.out.println("The sum is: " + adderObject.add(a, b));
    }
}