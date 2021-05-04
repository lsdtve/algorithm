import java.util.Scanner;

public class BOJ_2909_캔디구매 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double C = sc.nextLong();
        int K = sc.nextInt();
        long temp = (long) Math.pow(10,K);
        System.out.println(Math.round(C/temp)*temp);
    }
}
