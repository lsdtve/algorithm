import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1043_거짓말 {

    static List<List<Integer>> party;
    static int[] p;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        party = new ArrayList<>();
        p = new int[N+1];
        Arrays.fill(p, -1);

        st = new StringTokenizer(br.readLine(), " ");

        int truthPeopleSize = Integer.parseInt(st.nextToken());

        for (int i = 0; i < truthPeopleSize; i++) {
            int temp = Integer.parseInt(st.nextToken());
            p[temp] = temp;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            List<Integer> lst = new ArrayList<>();

            int size = Integer.parseInt(st.nextToken());
            for (int j = 0; j < size; j++) {
                lst.add(Integer.parseInt(st.nextToken()));
            }
            party.add(lst);

            int a = lst.get(0);
            for (int j = 1; j < lst.size() ; j++) {
                union(a, j);
            }
        }

        int ans = 0;
        for (List<Integer> lst : party) {
            System.out.println(lst);
            for (int a : lst) {
                if (p[a]!=-1) {
                    ans++;
                    break;
                }
            }
        }
        System.out.println(ans);
        for (int t :
                p) {
            System.out.println(t);
        }
    }

    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a < b) {
            p[b] = a;
        }else {
            p[a] = b;
        }
    }

    private static int find(int a) {
        if (p[a] == a || p[a] < 0) {
            return a;
        }
        return p[a] = find(p[a]);
    }

}
