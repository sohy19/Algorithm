import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_백준_16395_배열돌리기3_엄소현_796ms {
	
	static int n, m, r, com, len;
	static int[][] map, resultMap;
	
	public static void main(String[] args) throws IOException {
		
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		len = Math.max(n, m);
		map = new int[len][len];
		resultMap = new int[len][len];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			com = Integer.parseInt(st.nextToken());
			turn(com);
			// 결과 반영
			for (int i = 0; i < resultMap.length; i++) {
				for (int j = 0; j < resultMap.length; j++) {
					map[i][j] = resultMap[i][j];
				}
			}
			
		}
		
		// 출력
		for (int i = 0; i < resultMap.length; i++) {
			for (int j = 0; j < resultMap.length; j++) {
				if (resultMap[i][j] == 0) continue;
				System.out.print(resultMap[i][j] + " ");
			}
			System.out.println();
		}
		
	}
	
	
	static public void turn(int num) {
		resultMap = new int[len][len];
		
		// 상하 반전
		if (num == 1) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					resultMap[n-i-1][j] = map[i][j];
				}
			}
		}
		
		// 좌우 반전
		else if (num == 2) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					resultMap[i][m-j-1] = map[i][j];
				}
			}
		}
		
		// 오른쪽 90도 반전
		else if (num == 3) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					resultMap[j][n-i-1] = map[i][j];						
				}
			}
			int temp = n;
			n = m;
			m = temp;
			
		}
		
		// 왼쪽 90도 반전
		else if (num == 4) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					resultMap[m-j-1][i] = map[i][j];
				}
			}
			int temp = n;
			n = m;
			m = temp;
			
		}
		
		// 1사분면 > 2사분면, 2사분면 > 3사분면, 3사분면 > 4사분면, 4사분면 > 1사분면
		else if (num == 5) {
			// 1사분면 > 2사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i][j+m/2] = map[i][j];
				}	
			}
			// 2사분면 > 3사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = m/2; j < m; j++) {
					resultMap[i+n/2][j] = map[i][j];
				}
			}
			// 3사분면 > 4사분면
			for (int i = n/2; i < n ; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i][j] = map[i][j+m/2];
				}
			}
			// 4사분면 > 1사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i][j] = map[i+n/2][j];
				}
			}
			
			
		}
		
		// 1사분면 > 4사분면, 4사분면 > 3사분면, 3사분면 > 2사분면, 2사분면 > 1사분면
		else if (num == 6) {
			// 1사분면 > 4사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i+n/2][j] = map[i][j];
				}
			}			
			// 4사분면 > 3사분면
			for (int i = n/2; i < n; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i][j+m/2] = map[i][j];
				}
			}			
			// 3사분면 > 2사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = m/2; j < m; j++) {
					resultMap[i][j] = map[i+n/2][j];
				}
			}			
			// 2사분면 > 1사분면
			for (int i = 0; i < n/2; i++) {
				for (int j = 0; j < m/2; j++) {
					resultMap[i][j] = map[i][j+m/2];
				}
			}
		}
		
		
		
	}
	
	
	
}
