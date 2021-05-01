import java.util.Scanner;

public class BOJ_1904_01타일 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] ans = {{0,0,1},{0,1,1}};

        for (int i = 3; i <= N; i++) {
            ans[0][i%3] = ans[0][(i-2)%3] + ans[1][(i-2)%3];
            ans[1][i%3] = ans[0][(i-1)%3] + ans[1][(i-1)%3];
            ans[0][i%3] %= 15746;
            ans[1][i%3] %= 15746;
        }
        int result = ans[0][N%3] + ans[1][N%3];
        System.out.println(result%15746);
    }
}
