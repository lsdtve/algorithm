import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1717_집합의표현 {

    static int[] node;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        node = new int[N+1];

        for (int i = 0; i <= N; i++) {
            node[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int check = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (check == 1) {
                System.out.println(find(a)==find(b) ? "YES" : "NO");
            }else {
                merge(a, b);
            }
        }

    }

    static void merge(int a, int b) {
        node[find(a)] = find(b);
    }
    static int find(int a) {
        if (node[a]==a) {
            return a;
        }
        return node[a] = find(node[a]);
    }
}
