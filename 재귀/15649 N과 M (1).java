import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[] nums;
	static boolean[] isSelected;
	static StringBuilder sb;
	
	public static void printNums() {
		for (int i = 0; i < nums.length; i++) {
			sb.append(nums[i]).append(" ");
		}
		sb.append("\n");
	}
	
	public static void sequence(int cnt) {
		if (cnt == m) {
			printNums();
			return;
		}
		for (int i = 1; i <= n; i++) {
			if (isSelected[i]) continue;
			isSelected[i] = true;
			nums[cnt] = i;
			sequence(cnt+1);
			isSelected[i] = false;
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		isSelected = new boolean[n+1];
		nums = new int[m];
		sb = new StringBuilder();
		
		sequence(0);
		System.out.println(sb);
		
	}

}
