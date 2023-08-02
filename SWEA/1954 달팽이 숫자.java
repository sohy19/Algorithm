import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	
	static int n;
	static int[][] grid;
	
	public static boolean inRange(int x, int y) {
		return 0 <= x && x < n && 0 <= y && y < n;
	}
	
	public static void moving() {
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, 1, 0, -1};
		int dirNum = 1;
		int x = 0;
		int y = -1;
		int nx, ny;
		for (int i = 1; i < n*n+1; i++) {
			nx = x + dx[dirNum];
			ny = y + dy[dirNum];
			if (!inRange(nx, ny) || grid[nx][ny] != 0) {
				dirNum = (dirNum + 1) % 4;
			}
			x = x + dx[dirNum];
			y = y + dy[dirNum];
			grid[x][y] = i;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());  // 테스트케이스 수
		for (int i = 1; i <= T; i++) {
			n = Integer.parseInt(br.readLine());  // 달팽이의 크기
			grid = new int[n][n];
			moving();
			System.out.println("#" + i);
			
			for (int j = 0; j < n; j++) {
				for (int j2 = 0; j2 < n; j2++) {
					System.out.printf("%d ", grid[j][j2]);
				}
				System.out.println();
			}
		}
		
		
	}

}
