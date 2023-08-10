import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
			// 외부 비교기 작성
			@Override
			// o1 - o2 = 오름차순
			public int compare(Integer o1, Integer o2) {  // 음수 0:그대로, 양수:교환
				int abs1 = Math.abs(o1);
				int abs2 = Math.abs(o2);
				if (abs1 == abs2) {
					return Integer.compare(o1, o2);
				}
				return Integer.compare(abs1, abs2);
			}
		});  
		
		int N = Integer.parseInt(br.readLine());  // 연산의 개수 N
		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(br.readLine());
			if (x == 0) {  // 큐에서 꺼내기
				if (pq.isEmpty()) {
					sb.append("0\n");
				} else {
					sb.append(pq.poll()).append("\n");
				}
				
				
			} else {  // 큐에 넣기
				pq.offer(x);
			}
		}
		
		System.out.println(sb);
		
	}

}
