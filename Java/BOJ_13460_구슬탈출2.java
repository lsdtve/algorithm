import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_13460_구슬탈출2 {

    static int N;
    static int M;
    static char[][] map;
    static boolean[][][][] visited;
    static int[] dy = {0,0,-1,1};
    static int[] dx = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);

        map = new char[N][M];
        visited = new boolean[N][M][N][M];

        for (int y = 0; y < N; y++) {
            map[y] = br.readLine().toCharArray();
        }

        Node startNode = new Node(null,null);

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (map[y][x] == 'R') {
                    map[y][x] = '.';
                    startNode.red = new Ball(x, y);
                }else if(map[y][x] =='B') {
                    map[y][x] = '.';
                    startNode.blue = new Ball(x, y);
                }
            }
        }
        System.out.println(bfs(startNode));
    }

    public static int bfs(Node n) {
        Queue<Node> q = new LinkedList<>();
        int time = 0;
        q.add(n);
        visited[n.red.y][n.red.x][n.blue.y][n.blue.x] = true;

        while(!q.isEmpty()) {
            int qSize = q.size();
            time++;
            if (time > 10) {
                break;
            }
            for (int t = 0; t < qSize; t++) {
                Node node = q.poll();

                for (int i = 0; i < 4; i++) {
                    Ball redBall = new Ball(node.red.x, node.red.y);
                    Ball blueBall = new Ball(node.blue.x, node.blue.y);
                    int check = 0;
                    while(true) {
                        redBall.x += dx[i];
                        redBall.y += dy[i];
                        if (map[redBall.y][redBall.x]=='O') {
                            check = 1;
                            break;
                        }else if (map[redBall.y][redBall.x]=='#') {
                            redBall.x -= dx[i];
                            redBall.y -= dy[i];
                            break;
                        }
                    }
                    while (true) {
                        blueBall.x += dx[i];
                        blueBall.y += dy[i];
                        if (map[blueBall.y][blueBall.x]=='O') {
                            check = -1;
                            break;
                        }else if (map[blueBall.y][blueBall.x]=='#') {
                            blueBall.x -= dx[i];
                            blueBall.y -= dy[i];
                            break;
                        }
                    }
                    if (check == 1) {
                        return time;
                    }
                    if (check == -1) {
                        continue;
                    }
                    if (redBall.equals(blueBall)) {
                        int redDistance = Math.abs(redBall.x - node.red.x) + Math.abs(redBall.y - node.red.y);
                        int blueDistance = Math.abs(blueBall.x - node.blue.x) + Math.abs(blueBall.y - node.blue.y);
                        if (redDistance > blueDistance) {
                            redBall.x -= dx[i];
                            redBall.y -= dy[i];
                        }else if (redDistance < blueDistance) {
                            blueBall.x -= dx[i];
                            blueBall.y -= dy[i];
                        }
                    }
                    if (!visited[redBall.y][redBall.x][blueBall.y][blueBall.x]) {
                        q.add(new Node(redBall, blueBall));
                        visited[redBall.y][redBall.x][blueBall.y][blueBall.x] = true;
                    }
                }
            }
        }
        return -1;
    }

    static class Node {
        Ball red;
        Ball blue;

        public Node(Ball red, Ball blue) {
            this.red = red;
            this.blue = blue;
        }
    }

    static class Ball {
        int x;
        int y;

        public Ball(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            Ball b = (Ball) obj;
            return y==b.y && x==b.x;
        }
    }
}