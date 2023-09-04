import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());  // 지폐의 금액 
		int k = Integer.parseInt(br.readLine());  // 동전의 가지 수
		int[] p = new int[k];  // 동전 금액 
		int[] n = new int[k];  // 각 동전의 개수 
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			p[i] = Integer.parseInt(st.nextToken());
			n[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[T+1];
		dp[0] = 1;
		
		for (int i = 0; i < k; i++) {
			for (int j = T; j >= p[i] ; j--) {
				for (int l = 1; l <= n[i]; l++) {
					if (j-p[i]*l >= 0) {
						dp[j] += dp[j-p[i]*l];						
					}
				}
				
			}
			
		}
		
		System.out.println(dp[T]);
		
		
	}
	

}
