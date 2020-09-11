//print ('this program works out the size in kilobytes of a CD quality sound sample')
//duration = input('how long is your sound, in seconds?: ')
//duration = int(duration)
//bits = 16
//channels = 2
//frequency = 44100
//size = frequency * bits * channels * duration
//result = size / 1000
//print(result)
  
import java.util.Scanner;

class Session2 {

    Scanner console = new Scanner(System.in);

    void print(Object o) {System.out.println(o);}
    String input() {return console.nextLine();}

    Integer add(Integer a, Integer b) {
        return a + b;
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
            answer = -1 //???
        }

        print(answer);
    }

    public static void main(String[] args) {new Session2();}
}