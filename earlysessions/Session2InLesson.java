import java.util.Scanner;


public class Session2 {

        Scanner console = new Scanner(System.in);

    //void life_story(String name) {
    //    System.out.println("My name is");
    //    System.out.println(name);
    //    System.out.println("I live in a pineapple under the sea");
    // }


    public Session2() {
        // System.out.println("Hello World");
        // //life_story("Spongebob Squarepants");
        // System.out.println("What is your name");
        // String answer = console.nextLine();
        // System.out.println("Your name is");
        // System.out.println(answer);

        // }

        System.out.println("Input1");
        String input1 = console.nextLine();
        Integer input1_integer = Integer.parseInt(input1);

        System.out.println("Input2");
        String input2 = console.nextLine();
        Integer input2_integer = Integer.parseInt(input2);

        System.out.println(input1_integer + input2_integer);

    }


    public static void main(String[] args) {
        new Session2();

        }
}