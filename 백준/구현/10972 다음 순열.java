import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] nums;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		nums = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		if (nextNums()) {
			for (int i = 0; i < nums.length; i++) {
				System.out.print(nums[i] + " ");
			}
		} else {
			System.out.println(-1);
		}
		
	}
	
	public static boolean nextNums() {
		// 꼭대기 찾기
		int x = N-1;
		while (x > 0 && nums[x-1] > nums[x]) x--;
		
		if (x == 0) return false;
		
		// 교환할 값 찾기
		int y = N-1;
		while (nums[x-1] >= nums[y]) y--;
		
		swap(x-1, y);
		
		int i = x;
		int j = N-1;
		while (i < j) swap(i++, j--);
		
		return true;
		
		
	}

	public static void swap(int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}
	

}
