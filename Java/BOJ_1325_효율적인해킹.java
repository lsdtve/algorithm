import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class BOJ_1325_효율적인해킹 {

    static int N;
    static int M;
    static Map<Integer, List<Integer>> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            map.get(end).add(start);
        }

        int maxSize = 0;
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            int temp = bfs(i);
            if (temp > maxSize) {
                maxSize = temp;
                result = new ArrayList<>();
                result.add(i);
            }else if (temp==maxSize) {
                result.add(i);
            }
        }
        System.out.println(String.join(" ", result.stream().map(String::valueOf).collect(Collectors.toList())));
    }

    public static int bfs(int n) {
        Queue<Integer> q = new LinkedList();
        boolean[] visited = new boolean[N+1];
        q.add(n);
        visited[n] = true;
        int result = 0;

        while(!q.isEmpty()) {
            int num = q.poll();
            result++;
            for (int next : map.get(num)) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.add(next);
                }
            }
        }
        return result;
    }
}