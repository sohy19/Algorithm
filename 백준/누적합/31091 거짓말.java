import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static boolean[] lie;
    static int lieCnt;
    static int[] up;
    static int[] down;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        lie = new boolean[N+1];
        up = new int[N+1];
        down = new int[N+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num > 0) {  // 이상
                up[num] += 1;
            } else {  // 이하
                down[-num] += 1;
            }
        }

        // 누적합
        for (int i = 0; i < N; i++) {
            up[i+1] += up[i];
        }
        for (int i = N-1; i > -1; i--) {
            down[i] += down[i+1] ;
        }

        // 거짓말 체크
        for (int i = 0; i <= N; i++) {
            int upCnt = up[N] - up[i];
            int downCnt = down[0] - down[i];
            if (i == upCnt + downCnt) {
                lie[i] = true;
            }
        }

        for (int i = 0; i <= N ; i++) {
            if (lie[i]) {
                lieCnt++;
            }
        }

        sb.append(lieCnt);
        sb.append("\n");
        for (int i = 0; i <= N; i++) {
            if (lie[i]) {
                sb.append(i).append(" ");
            }
        }

        System.out.println(sb);


    }

}
