import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_1194_달이차오른다가자 {

    static int N;
    static int M;
    static char[][] map;
    static boolean[][][] visited;
    static int[] dy = {1,-1,0,0};
    static int[] dx = {0,0,1,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        Node startNode = null;
        map = new char[N][M];
        visited = new boolean[N][M][64];

        for (int y = 0; y < N; y++) {
            map[y] = br.readLine().toCharArray();
        }

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (map[y][x]=='0') {
                    startNode = new Node(x,y,0,0);
                }
            }
        }
        System.out.println(bfs(startNode));
    }

    public static int bfs(Node startNode) {
        Queue<Node> q = new LinkedList<>();
        q.add(startNode);
        visited[startNode.y][startNode.x][startNode.key] = true;

        while(!q.isEmpty()) {
            Node node = q.poll();
            if (map[node.y][node.x]=='1') {
                return node.cnt;
            }

            for (int i = 0; i < 4; i++) {
                int ny = node.y + dy[i];
                int nx = node.x + dx[i];
                if (ny<0 || N<=ny || nx<0 || M<=nx) {
                    continue;
                }
                if (map[ny][nx]=='#' || visited[ny][nx][node.key]) {
                    continue;
                }
                if ('a' <= map[ny][nx] && map[ny][nx] <='f') {
                    int key = (1 << (map[ny][nx]-'a')) | node.key;
                    if (!visited[ny][nx][key]) {
                        visited[ny][nx][key] = true;
                        q.add(new Node(nx,ny,node.cnt+1,key));
                    }
                } else if ('A' <= map[ny][nx] && map[ny][nx] <='F') {
                    int door = (1 << (map[ny][nx] - 'A')) & node.key;
                    if (door > 0) {
                        visited[ny][nx][node.key] = true;
                        q.add(new Node(nx,ny,node.cnt+1,node.key));
                    }
                } else {
                    visited[ny][nx][node.key] = true;
                    q.add(new Node(nx,ny,node.cnt+1,node.key));
                }
            }
        }
        return -1;
    }

    static class Node {
        int x;
        int y;
        int cnt;
        int key;

        public Node(int x, int y, int cnt, int key) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.key = key;
        }
    }
}
