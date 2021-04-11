import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_16236_아기상어 {

    static int N;
    static int[][] map;
    static Shark shark;
    static int[] dy = {-1,0,1,0};
    static int[] dx = {0,-1,0,1};
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        shark = new Shark();

        for (int y = 0; y < N; y++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int x = 0; x < N; x++) {
                map[y][x] = Integer.parseInt(st.nextToken());
                if (map[y][x]==9) {
                    shark.pos = new Pos(y,x);
                    map[y][x] = 0;
                }
            }
        }


        while(bfs()) {

        }
        System.out.println(ans);

    }

    static class Shark {
        public Pos pos;
        public int size = 2;
        public int sizeCount = 0;

        public void eat() {
            sizeCount++;
            if (sizeCount==size) {
                sizeCount = 0;
                size++;
            }
        }
    }
    static class Pos {
        public int y;
        public int x;

        public Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static boolean bfs() {
        Queue<Pos> q = new LinkedList();
        boolean[][] visitied = new boolean[N][N];
        visitied[shark.pos.y][shark.pos.x] = true;
        q.add(shark.pos);

        int distinace = 0;
        Pos result = null;

        while (!q.isEmpty()) {
            int qSize = q.size();
            distinace++;
            for (int i = 0; i < qSize; i++) {
                Pos now = q.poll();
                for (int d = 0; d < 4; d++) {
                    int ny = now.y + dy[d];
                    int nx = now.x + dx[d];
                    if (0<=ny && ny<N && 0<=nx && nx<N) {
                        if (!visitied[ny][nx]) {
                            visitied[ny][nx] = true;
                            if (shark.size>=map[ny][nx]) {
                                q.add(new Pos(ny,nx));
                                if (map[ny][nx]<shark.size && map[ny][nx]!=0) {
                                    if (result==null) {
                                        result = new Pos(ny,nx);
                                    }else {
                                        if (result.y > ny) {
                                            result = new Pos(ny,nx);
                                        }else if (result.y == ny && result.x > nx) {
                                            result = new Pos(ny,nx);
                                        }
                                    }
                                }
                            }

                        }
                    }
                }
            }
            if (result!=null){
                shark.eat();
                shark.pos.y = result.y;
                shark.pos.x = result.x;
                map[result.y][result.x] = 0;
                ans += distinace;
                return true;
            }

        }
        return false;
    }
}
