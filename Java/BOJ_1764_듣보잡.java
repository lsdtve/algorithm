import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class BOJ_1764_듣보잡 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] st = br.readLine().split(" ");
        int N = Integer.parseInt(st[0]);
        int M = Integer.parseInt(st[1]);
        Set<String> setA = new HashSet<>();
        Set<String> setB = new HashSet<>();

        for (int i = 0; i < N; i++) {
            setA.add(br.readLine());
        }
        for (int i = 0; i < M; i++) {
            setB.add(br.readLine());
        }

        setA.retainAll(setB);
        List<String> result = setA.stream()
                .sorted()
                .collect(Collectors.toList());

        System.out.println(result.size());
        for (String ans : result) {
            System.out.println(ans);
        }

    }
}
