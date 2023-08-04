import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] nums = new int[9];
	static boolean[] isSelected = new boolean[9];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i = 0; i < 9; i++) {
			nums[i] = Integer.parseInt(br.readLine());
		}
		
		setSum(0, 0);
	}
	
	public static boolean setSum(int cnt, int sum) {
		if (cnt == 7) {
			if(sum == 100 ) {
				for (int i = 0; i < 9; i++) {
					if (isSelected[i]) {
						System.out.println(nums[i]);
					}
				}
				return true;
			}
			return false;
		}
		
		for (int i = 0; i < 9; i++) {
			if (isSelected[i]) continue;
			isSelected[i] = true;
			if(setSum(cnt+1, sum+nums[i])) {
				return true;
			}
			isSelected[i] = false;
		}
		
		return false;
	}

}
