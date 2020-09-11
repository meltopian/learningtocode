import java.util.Scanner;

class Session2 {

    Scanner console = new Scanner(System.in);

    void print(Object o) {System.out.println(o);}
    String input() {return console.nextLine();}

    Integer add(Integer a, Integer b) {
        return a + b;
    }

    Integer multiply(Integer a, Integer b) {
        return a * b;
    }

    Session2() {
        print("input_a: ");
        String input_a = input();
        print("input_b: ");
        String input_b = input();
        print("what operation do you want to perform (+ or *): ");
        String operation = input();

        Integer a = Integer.parseInt(input_a);
        Integer b = Integer.parseInt(input_b);
        Integer answer = 0;
        if (operation.equals("+")) {
            answer = add(a, b);
        }
        if (operation.equals("*")) {
            answer = multiply(a, b);
        }
        else print("unknown operation type");

        print(answer);
    }

    public static void main(String[] args) {new Session2();}
}