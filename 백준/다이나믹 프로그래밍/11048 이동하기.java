import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
	
	
public class Main {
	
	static int N, M;
	static int[][] map, dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());  // 행
		M = Integer.parseInt(st.nextToken());  // 열
		
		map = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dp = new int[N][M];
		dp[0][0] = map[0][0];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (0 <= i-1 && i-1 < N && 0 <= j && j < M) {
					dp[i][j] = Math.max(dp[i][j], map[i][j] + dp[i-1][j]);					
				}
				if (0 <= i && i < N && 0 <= j-1 && j-1 < M) {
					dp[i][j] = Math.max(dp[i][j], map[i][j] + dp[i][j-1]);					
				}
				if (0 <= i-1 && i-1 < N && 0 <= j-1 && j-1 < M) {
					dp[i][j] = Math.max(dp[i][j], map[i][j] + dp[i-1][j-1]);					
				}
				
			}
		}
		
		System.out.println(dp[N-1][M-1]);
	}

}
