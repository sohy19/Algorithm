import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, K;
	static int[][] map;
	static int[][] newMap;
	static int[][] com;
	static int[] comPer;
	static int min = Integer.MAX_VALUE;
	static int [] dx = {0, 1, 0, -1};
	static int [] dy = {1, 0, -1, 0};

	public static void main(String[] args) throws IOException {
		
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());  // 행
		M = Integer.parseInt(st.nextToken());  // 열
		K = Integer.parseInt(st.nextToken());  // 회전 연산 개수
		map = new int[N][M];  // 배열
		com = new int[K][3];  // 회전 연산
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken()); 
			}
		}
		
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				com[i][j] = Integer.parseInt(st.nextToken()); 
			}
		}

		comPer = new int[K];  // 회전 연산 순열
		
		
		// 회전 연산 순열 구하기
		makeCom(0, 0);
		System.out.println(min);
		
	}
	
	public static void makeCom(int cnt, int flag) {
		if (cnt == K) {
			// 회전된 배열 저장할 새 배열 
			newMap = new int[N][M];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					newMap[i][j] = map[i][j];
				}
			}
			
			for (int i = 0; i < K; i++) {
				turn(com[comPer[i]][0]-1, com[comPer[i]][1]-1, com[comPer[i]][2]);
			}
			findMin();
			return;
		}
		
		for (int i = 0; i < K; i++) {
			if ((flag & 1<<i) != 0) continue;
			comPer[cnt] = i;
			makeCom(cnt+1, flag | 1<<i);
		}
	}
	
	// 회전 연산
	public static void turn(int r, int c, int s) {
		
		for (int i = 1; i < s+1; i++) {
			// 일차원 배열에 값 담기
			int len = (int)(Math.pow(1 + i * 2, 2) - Math.pow(1 + (i-1) * 2, 2));
			int[] line = new int[len];
			int x = r-i;
			int y = c-i-1;
			int dirNum = 0;
			for (int j = 0; j < len; j++) {
				int nx = x + dx[dirNum];
				int ny = y + dy[dirNum];
				if (!(r-i <= nx && nx <= r+i && c-i <= ny && ny <= c+i)) {
					dirNum = (dirNum + 1) % 4;
				}
				x = x + dx[dirNum];
				y = y + dy[dirNum];
				line[j] = newMap[x][y];
			}
			
			// 시계 방향으로 돌려서 넣기
			x = r-i;
			y = c-i;
			dirNum = 0;
			for (int j = 0; j < len; j++) {
				int nx = x + dx[dirNum];
				int ny = y + dy[dirNum];
				if (!(r-i <= nx && nx <= r+i && c-i <= ny && ny <= c+i)) {
					dirNum = (dirNum + 1) % 4;
				}
				x = x + dx[dirNum];
				y = y + dy[dirNum];
				newMap[x][y] = line[j];
			}
		}
		
		
	}
	
	
	// 각 행 최솟값 반환
	public static void findMin() {
		for (int i = 0; i < N; i++) {
			int sum = 0;
			for (int j = 0; j < M; j++) {
				sum += newMap[i][j];
			}
			min = Math.min(min, sum);
		}
		return;
	
		
	} 
}  // end of class
