import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10775_공항 {

    static int[] lst;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int G = Integer.parseInt(br.readLine());
        int P = Integer.parseInt(br.readLine());

        lst = new int[G+1];
        for (int i = 0; i <= G; i++) {
            lst[i] = i;
        }
        int ans = 0;

        for (int i = 0; i < P; i++) {
            int n = Integer.parseInt(br.readLine());

            int num = find(n);
            if (num == 0) {
                break;
            }
            ans++;
            union(num, num-1);
        }
        System.out.println(ans);

    }

    static void union(int a, int b) {
        lst[find(a)] = find(b);
    }

    static int find(int a) {
        if (a == lst[a]) {
            return a;
        }

        return lst[a] = find( lst[a]);
    }
}
