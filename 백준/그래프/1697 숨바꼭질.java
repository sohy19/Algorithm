import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int N, K;
	static int[] time;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());  // 수빈 위치
		K = Integer.parseInt(st.nextToken());  // 동생 위치
		time = new int[100001];
		
		System.out.println(bfs()-1);
	}
	
	public static boolean inRange(int x) {
		return 0 <= x && x < 100001;
	}
	
	public static int bfs() { 
		Queue<Integer> q = new LinkedList<>();
		q.offer(N);
		time[N] = 1;
		while (!q.isEmpty()) {
			int v = q.poll();

			if (inRange(v-1) && time[v-1] == 0) {
				q.offer(v-1);
				time[v-1] = time[v] + 1;
			}
			if (inRange(v+1) && time[v+1] == 0) {
				q.offer(v+1);
				time[v+1] = time[v] + 1;
			}
			if (inRange(v*2) && time[v*2] == 0) {
				q.offer(v*2);
				time[v*2] = time[v] + 1;
			}
			
			// 동생 위치 도달
			if (time[K] != 0) {
				break;
			}
			
		}
		return time[K];
	}

}
