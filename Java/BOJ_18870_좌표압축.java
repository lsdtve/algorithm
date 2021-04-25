import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class BOJ_18870_좌표압축 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<Integer> arr = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        AtomicInteger index = new AtomicInteger();

        Map<Integer, Integer> arrMap = arr.stream()
                .distinct()
                .sorted()
                .collect(Collectors.toMap(integer -> integer, (integer) -> index.getAndIncrement()));

        for (Integer s : arr) {
            Integer i = arrMap.get(s);
            bw.write(i + " ");
        }
        bw.flush();
    }
}
