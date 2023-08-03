import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int n;
	static int m;
	static int[][] grid;
	
	public static int count(int x, int y) {
		int sum = 0;
		int nx, ny;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < m; j++) {
				nx = x + i;
				ny = y + j;
				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					sum += grid[nx][ny];
				}
			}
		}
		
		return sum;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			
			grid = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					grid[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int maxSum = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					maxSum = maxSum < count(i, j) ? count(i, j) : maxSum;
				}
			}
			
			System.out.println("#" + t + " " + maxSum);
		}
		
	}  // end of main
}  // end of class
