import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, r;
	static int[][] arr, tempArr;
	static int[][] dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0}};
	static int[] linearArr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());  // 회전 수
		arr = new int[n][m];
		
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		turn();
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.print(tempArr[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void turn() {
		tempArr = new int[n][m];
		int dirNum = 0;
		
		for (int i = 0; i < Math.min(n, m)/2; i++) {
			// 일차원 배열에 저장
			int len = 2 * (n-2*i) + 2 * (m-2*i) - 4;
			int[] temp = new int[len];
			int x = i;
			int y = i;
			temp[0] = arr[i][i];
			for (int j = 1; j < len; j++) {
				int dx = x + dir[dirNum][0];
				int dy = y + dir[dirNum][1];
				if (!(i <= dx && dx < n-i && i <= dy && dy < m-i)) {
					dirNum = (dirNum + 1) % 4;
				}
				x = x + dir[dirNum][0];
				y = y + dir[dirNum][1];
				temp[j] = arr[x][y];
			}

			
			x = i;
			y = i-1;
			dirNum = 0;
			for (int j = 0; j < len; j++) {
				int idx = (r + j) % len;
				
				int dx = x + dir[dirNum][0];
				int dy = y + dir[dirNum][1];
				if (!(i <= dx && dx < n-i && i <= dy && dy < m-i)) {
					dirNum = (dirNum + 1) % 4;
				}
				x = x + dir[dirNum][0];
				y = y + dir[dirNum][1];
				
				tempArr[x][y] = temp[idx];
				
			}
			
		}
		
	
		
	}

}
