import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int n, m, maxWeight;
	static int[] weight;
	static boolean[] isSelected;
	
	public static void calc(int cnt, int sum) {
		if (cnt == 2) {
			if (sum <= m) {
				maxWeight = Math.max(maxWeight, sum);
			}
			return;
		}
		
		for (int i = 0; i < n; i++) {
			if (isSelected[i]) continue;
			isSelected[i] = true;
			calc(cnt+1, sum+weight[i]);
			isSelected[i] = false;
			
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer	st;
		
		int TC = Integer.parseInt(br.readLine());  // 테스트 케이스 개수
		for (int i = 1; i <= TC; i++) {
			
			// 입력
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());  // 봉지 개수
			m = Integer.parseInt(st.nextToken());  // 무게 합 제한
			
			weight = new int[n];
			isSelected = new boolean[n];  // 선택 됐는지 표시
			maxWeight = -1;  // 초기화
			
			st = new StringTokenizer(br.readLine());  // 무게
			for (int j = 0; j < weight.length; j++) {
				weight[j] = Integer.parseInt(st.nextToken());
			}
			
			
			calc(0, 0);
			System.out.println("#" + i + " " + maxWeight);
			
			
			
		}
		
	}

}
