import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_3085_사탕게임 {

    static int N;
    static char[][] map;
    static int ans = 1;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new char[N][N];

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }

        char temp;
        for (int y = 0; y < N; y++) {
            for (int x = 1; x < N; x++) {
                if (map[y][x] == map[y][x - 1]) {
                    continue;
                }
                temp = map[y][x];
                map[y][x] = map[y][x - 1];
                map[y][x - 1] = temp;
                go();
                map[y][x - 1] = map[y][x];
                map[y][x] = temp;
            }
        }
        go();
        for (int y = 1; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (map[y][x] == map[y - 1][x]) {
                    continue;
                }
                temp = map[y - 1][x];
                map[y - 1][x] = map[y][x];
                map[y][x] = temp;
                go();
                map[y][x] = map[y - 1][x];
                map[y - 1][x] = temp;
            }
        }
        System.out.println(ans);

    }

    public static void go() {
        int result = 1;

        for (int y = 0; y < N; y++) {
            result = 1;
            for (int i = 1; i < N; i++) {
                if (map[y][i - 1] == map[y][i]) {
                    result++;
                    ans = Math.max(ans, result);
                } else {
                    result = 1;
                }
            }

        }
        for (int x = 0; x < N; x++) {
            result = 1;
            for (int i = 1; i < N; i++) {
                if (map[i - 1][x] == map[i][x]) {
                    result++;
                    ans = Math.max(ans, result);
                } else {
                    result = 1;
                }
            }
        }

    }
}