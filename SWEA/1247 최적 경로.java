import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	private static int N, minDist;
	private static int[] office;
	private static int[] home;
	private static int[][] cust;
	private static int[] nums;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		for (int t = 1; t <= T; t++) {
			N = Integer.parseInt(br.readLine());  // 고객 수
			office = new int[2];  // 회사 좌표
			home = new int[2];  // 집 좌표
			cust = new int[N][2];  // 고객 좌표
			st = new StringTokenizer(br.readLine());
			office[0] = Integer.parseInt(st.nextToken());
			office[1] = Integer.parseInt(st.nextToken());
			home[0] = Integer.parseInt(st.nextToken());
			home[1] = Integer.parseInt(st.nextToken());
			for (int i = 0; i < N; i++) {
				cust[i][0] = Integer.parseInt(st.nextToken());
				cust[i][1] = Integer.parseInt(st.nextToken());
			}
			nums = new int[N];
			minDist = Integer.MAX_VALUE;
			makePermutation(0, 0);
			System.out.println("#" + t + " " + minDist);
		}
		
	}
	
	public static void makePermutation(int cnt, int flag) {
		if (cnt == N) {
			calcDist();
			return;
		}
		for (int i = 0; i < N; i++) {
			if ((flag & 1<<i) != 0) continue;
			nums[cnt] = i;
			makePermutation(cnt+1, flag|1<<i);
		}
	}
	
	public static void calcDist() {
		int[] now = office;
		int dist = 0;
		for (int i = 0; i < N; i++) {
			dist += Math.abs(now[0] - cust[nums[i]][0]) + Math.abs(now[1] - cust[nums[i]][1]);
			now = cust[nums[i]];
		}
		dist += Math.abs(home[0] - now[0]) + Math.abs(home[1] - now[1]);
		minDist = Math.min(minDist, dist);

	}

}
