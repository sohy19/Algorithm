import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static StringBuilder sb;
    static PriorityQueue<Integer> pq;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                printElem();
            } else {
                putElem(num);
            }
        }

        System.out.println(sb);

    }
    public static void printElem() {
        if (pq.isEmpty()){
            sb.append(0);
        } else{
            sb.append(pq.poll());
        }
        sb.append("\n");
    }

    public static void putElem(int num) {
        pq.offer(num);
    }
    
}
