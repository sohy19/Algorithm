import java.io.*;
import java.util.*;

public class Solution {
	static int[] arr, month;
	static int[] dp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			arr = new int[4]; // 이용권 가격
			for (int i = 0; i < 4; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			month = new int[12]; // 한달
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 12; i++) {
				month[i] = Integer.parseInt(st.nextToken());
			}
			
			// 1일 이용권 구매 or 1달 전 구매 or 3달 전 구매 or 1년 구매
			dp = new int[12];
			// 초기화
			// min(1일 이용권 구매, 1달 이용권 구매, 3달 이용권 구매)
			dp[0] = Math.min(month[0] * arr[0], arr[1]); // 1월달
			dp[1] = Math.min(dp[0] + arr[0] * month[1], dp[0] + arr[1]); // 2월달
			dp[2] = Math.min(dp[1] + arr[0] * month[2], Math.min(dp[1] + arr[1], arr[2]));  // 3월달
			
			for(int i = 3; i < 12; i++) {	
				dp[i] = Math.min(dp[i-1] + arr[0] * month[i], Math.min(dp[i-1] + arr[1], dp[i-3] + arr[2]));
			}
			
			dp[11] = Math.min(dp[11], arr[3]);  // 최종값이랑 1년 비교
			System.out.println("#" + test_case + " " + dp[11]);
		}

	}
}
