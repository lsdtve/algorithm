import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_17398_통신망분할 {

    static int[] p;
    static int[] rank;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        int[] order = new int[Q];
        int[][] node = new int[M][2];
        boolean[] check = new boolean[M];

        p = new int[N+1];
        rank = new int[N+1];

        Arrays.fill(rank,1);

        for (int i = 0; i <= N; i++) {
            p[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            node[i][0] = Integer.parseInt(st.nextToken());
            node[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < Q; i++) {
            order[i] = Integer.parseInt(br.readLine()) - 1;
            check[order[i]] = true;
        }

        for (int i = 0; i < M; i++) {
            if (check[i]) {
                continue;
            }
            union(node[i][0], node[i][1]);
        }

        long ans = 0;
        for (int t = Q-1; t >= 0 ; t--) {
            int index = order[t];
            if (find(node[index][0]) != find(node[index][1])) {
                ans += (long)rank[find(node[index][0])] * (long)rank[find(node[index][1])];
            }
            union(node[index][0], node[index][1]);
        }
        System.out.println(ans);

    }

    static void union(int a, int b) {
        int x = find(a);
        int y = find(b);

        if (x == y) {
            return;
        }
        if (rank[x] < rank[y]) {
            int temp = x;
            x = y;
            y = temp;
        }
        rank[x] += rank[y];
        p[y] = x;
    }

    static int find(int a) {
        if (p[a] == a) {
            return a;
        }
        return p[a] = find(p[a]);
    }
}
