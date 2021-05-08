import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_5525_IOIOI {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        char[] str = br.readLine().toCharArray();

        int ans = 0;
        int cnt = 0;
        for (int i = 2; i < M; i++) {
            if (str[i]=='I' && str[i-1]=='O' && str[i-2]=='I') {
                cnt++;
                if (cnt == N) {
                    ans++;
                    cnt--;
                }
                i++;
            }
            else {
                cnt = 0;
            }
        }
        System.out.println(ans);
    }
}
