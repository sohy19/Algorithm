import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	
	static class Shark {
		int row;
		int col;
		int speed;
		int dir;
		int size;
		int idx;
		
		public Shark(int row, int col, int speed, int dir, int size, int idx) {
			super();
			this.col = col;
			this.row = row;
			this.speed = speed;
			this.dir = dir;
			this.size = size;
			this.idx = idx;
		}
		
	}
	

	static int R, C, M, maxSize;
	static Shark[] shark;
	static Shark[][] map;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());  // 격자판 행
		C = Integer.parseInt(st.nextToken());  // 격자판 열
		M = Integer.parseInt(st.nextToken());  // 격자판 상어 수
		shark = new Shark[M];
		map = new Shark[R][C];  // 격자판 상어 표시
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());  // 행
			int c = Integer.parseInt(st.nextToken());  // 열
			int s = Integer.parseInt(st.nextToken());  // 속력
			int d = Integer.parseInt(st.nextToken());  // 이동 방향
			int z = Integer.parseInt(st.nextToken());  // 크기
			d = d == 1? 0 : d == 2? 3: d == 3? 1 : 2;
			Shark sh = new Shark(r-1, c-1, s, d, z, i);
			map[r-1][c-1] = sh;
			shark[i] = sh;
		}
		
		fishing();
		System.out.println(maxSize);
		
	}
	
	public static void fishing() {
		for (int i = 0, j; i < C; i++) {
			for (j = 0; j < R; j++) {
				if (map[j][i] != null) {
					maxSize += map[j][i].size;
					break;
				}
			}
			move(i, j);
		}
	}
	
	
	// x, y 방금 잡은 물고기 위치
	public static void move(int x, int y) {
		int dx[] = {-1, 0, 0, 1};
		int dy[] = {0, 1, -1, 0};
		int dirNum;
		Shark[][] newMap = new Shark[R][C];
		
		// 상어 이동
		for (int i = 0; i < shark.length; i++) {
			if (shark[i] == null) continue;
			if (shark[i].row == y && shark[i].col == x) {
				shark[i] = null;
				continue;
			}
			Shark s = shark[i];
			dirNum = s.dir;
			for (int j = 0; j < s.speed ; j++) {
				int nr = s.row + dx[dirNum];
				int nc = s.col + dy[dirNum];
				if (!(0 <= nr && nr < R && 0 <= nc && nc < C)) {
					dirNum = (3-dirNum) % 4 ;  // 방향 바꿔주기
					s.dir = dirNum;
				}
				s.row = s.row + dx[dirNum];
				s.col = s.col + dy[dirNum];
			}
		}
		
		for (int i = 0; i < shark.length; i++) {
			if (shark[i] == null) continue;
			// 다른 상어가 있을 경우
			if (newMap[shark[i].row][shark[i].col] != null) {
				if (newMap[shark[i].row][shark[i].col].size < shark[i].size) {
					Shark sh = newMap[shark[i].row][shark[i].col];
					shark[sh.idx] = null;
					newMap[shark[i].row][shark[i].col] = shark[i];
				} else {
					shark[i] = null;
				}
			}
			else {
				newMap[shark[i].row][shark[i].col] = shark[i];					
			}
		}
		
		map = newMap;
	
	}

	

}
