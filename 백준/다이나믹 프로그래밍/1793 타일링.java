import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String line;
		
		while ((line = br.readLine()) != null) {
			StringTokenizer st = new StringTokenizer(line, " ");
			int n = Integer.parseInt(st.nextToken());
			
			BigInteger[] dp = new BigInteger[251];
			dp[0] = new BigInteger("1");
			dp[1] = new BigInteger("1");
			
			for (int i = 2; i < 251; i++) {
				dp[i] = dp[i-1].add(dp[i-2].multiply(new BigInteger("2")));
			}
               
            sb.append(dp[n]).append('\n');
			
		}
		
		System.out.println(sb);

	}

}
