import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_2589_보물섬 {

    static int N;
    static int M;
    static char[][] map;
    static int[] dy = {1,-1,0,0};
    static int[] dx = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        map = new char[N][M];

        for (int y = 0; y < N; y++) {
            map[y] = br.readLine().toCharArray();
        }

        int ans = 0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (map[y][x]=='L') {
                    ans = Math.max(ans, bfs(new Node(y,x)));
                }
            }
        }
        System.out.println(ans);

    }

    public static int bfs(Node startNode) {
        boolean[][] visited = new boolean[N][M];
        Queue<Node> q = new LinkedList<>();
        q.add(startNode);
        visited[startNode.y][startNode.x] = true;
        int distance = -1;

        while(!q.isEmpty()) {
            int qSize = q.size();
            distance++;
            for (int i = 0; i < qSize; i++) {
                Node node = q.poll();
                for (int d = 0; d < 4; d++) {
                    int ny = node.y + dy[d];
                    int nx = node.x + dx[d];
                    if (0 > ny || ny >= N || 0 > nx || nx >= M) {
                        continue;
                    }
                    if (visited[ny][nx] || map[ny][nx]=='W') {
                        continue;
                    }
                    visited[ny][nx] = true;
                    q.add(new Node(ny,nx));
                }
            }
        }

        return distance;
    }

    static class Node {
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}

