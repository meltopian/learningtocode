import java.util.Scanner;

class Session2 {

    Scanner console = new Scanner(System.in);

    void print(Object o) {
        System.out.println(o);
    }

    String input() {
        return console.nextLine();
    }

    Integer add(Integer a, Integer b) {
        return a + b;
    }

    Integer multiply(Integer a, Integer b) {
        return a * b;
    }

    Integer subtract(Integer a, Integer b) {
        return a - b;
    }

    Session2() {
        print("Find out the number of kilobytes in a raw pcm file");
        print("frequency: ");
        String input_a = input();
        print("channels: ");
        String input_b = input();
        print ("bits: ");
        String input_c = input();
        print ("duration in seconds: ");
        String input_d = input();

        Integer a = Integer.parseInt(input_a);
        Integer b = Integer.parseInt(input_b);
        Integer c = Integer.parseInt(input_c);
        Integer d = Integer.parseInt(input_d);
        Integer answer = 0;
        answer = a * b * c * d / 8000;

        print(answer);
    }

    public static void main(String[] args) {
        new Session2();
    }
}
