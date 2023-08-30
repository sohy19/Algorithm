import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, minCost;
	static int[][] cost;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
	
		N = Integer.parseInt(st.nextToken());  // 도시 수
		cost = new int[N][N];  // 비용 
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				cost[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		minCost = Integer.MAX_VALUE;
		dfs(0, 0, 0, 0);
		System.out.println(minCost);
		
	
	}

	
	public static void dfs(int city, int c, int flag, int cnt) {
		if (minCost < c) return;
		if (cnt == N && city == 0) {  // 도시를 다 돌고 돌아옴
			minCost = Math.min(minCost, c);
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if ((flag & 1<<i) != 0) continue;
			if (cost[city][i] != 0) {
				dfs(i, c+cost[city][i], flag|1<<i, cnt+1);
			}
		}
	}
}
