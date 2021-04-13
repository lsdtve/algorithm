import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_17144_미세먼지안녕 {

    static int R;
    static int C;
    static int T;
    static int[][] map;
    static List<Pos> airCleaner = new ArrayList<>();
    static int[][] topWind = {{0,1},{-1,0},{0,-1},{1,0}};
    static int[][] buttomWind = {{0,1},{1,0},{0,-1},{-1,0}};
    static int[] dy = {0,0,-1,1};
    static int[] dx = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        R = Integer.parseInt(str[0]);
        C = Integer.parseInt(str[1]);
        T = Integer.parseInt(str[2]);
        map = new int[R][C];

        for (int y = 0; y < R; y++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int x = 0; x < C; x++) {
                map[y][x] = Integer.parseInt(st.nextToken());
                if (map[y][x]==-1) {
                    airCleaner.add(new Pos(x,y));
                }
            }
        }

        for (int i = 0; i < T; i++) {
            diffusion();
            airClean(airCleaner.get(0), topWind);
            airClean(airCleaner.get(1), buttomWind);
        }

        int ans = Arrays.stream(map)
                .flatMapToInt(Arrays::stream)
                .reduce(0,Integer::sum);

        System.out.println(ans+2);

    }

    public static void diffusion() {
        int[][] temp = new int[R][C];

        for (Pos pos : airCleaner) {
            temp[pos.y][pos.x] = -1;
        }

        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                int cnt = 0;
                int num = map[y][x]/5;
                if (map[y][x]<=0) {
                    continue;
                }

                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];

                    if (0 > ny || ny >= R || 0 > nx || nx >= C) {
                        continue;
                    }
                    if (map[ny][nx] == -1) {
                        continue;
                    }
                    cnt++;
                    temp[ny][nx] += num;
                }
                temp[y][x] += map[y][x] - num*cnt;
            }
        }
        map = temp;
    }

    public static void airClean(Pos cleaner, int[][] wind) {
        Pos now = new Pos(cleaner.x + 1, cleaner.y);
        int temp = map[cleaner.y][cleaner.x+1];
        map[cleaner.y][cleaner.x+1] = 0;

        for (int i = 0; i < 4; i++) {
            while(true) {
                int ny = now.y + wind[i][0];
                int nx = now.x + wind[i][1];

                if(0 > ny || ny >=R || 0 > nx || nx >=C) {
                    break;
                }
                if (map[ny][nx] == -1) {
                    return;
                }
                int num = map[ny][nx];
                map[ny][nx] = temp;
                temp = num;
                now.y = ny;
                now.x = nx;
            }
        }
    }


    static class Pos {
        int x;
        int y;
        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
