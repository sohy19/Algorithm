
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
    private static int H, W, posX, posY;
    private static char dir;
	private static char[][] map;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());  // 테스트 케이스 수
		for (int t = 1; t <= T; t++) {
			// 입력
			st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());  // 맵 높이
			W = Integer.parseInt(st.nextToken());  // 맵 너비
			map = new char[H][W];

			
			for (int i = 0; i < H; i++) {
				String line = br.readLine();
				for (int j = 0; j < W; j++) {
					char ch = line.charAt(j);
					map[i][j] = ch;
					// 현재 전차 위치 및 방향 저장
					if (ch == '<') {
						posX = i;
						posY = j;
						dir = '<';
					}
					else if (ch == '>') {
						posX = i;
						posY = j;
						dir = '>';
					}
					else if (ch == '^') {
						posX = i;
						posY = j;
						dir = '^';
					}
					else if (ch == 'v'){
						posX = i;
						posY = j;
						dir = 'v';
					}
					
				}
			}
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());  // 사용자 입력 개수
			char[] com = new char[N];  // 사용자 입력
			String line = br.readLine();
			for (int i = 0; i < N; i++) {
				com[i] = line.charAt(i);
			}
			
			
			// 사용자 입력 시작
			for (char c : com) {
				if (c == 'U') up();
				else if (c == 'D') down();
				else if (c == 'L') left();
				else if (c == 'R') right();
				else shoot();
			}
			
			System.out.print("#" + t + " ");
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
			
		}
		

	}
	
	public static boolean inRange(int x, int y) {
		return 0 <= x && x < H && 0 <= y && y < W;
	}
	
	public static void up() {
		dir = '^';
		if (inRange(posX-1, posY) && map[posX-1][posY] == '.') {
			map[posX][posY] = '.';
			map[posX-1][posY] = '^';
			posX -= 1;
		} else {
			map[posX][posY] = '^';
		}
		
	}
	
	public static void down() {
		dir = 'v';
		if (inRange(posX+1, posY) && map[posX+1][posY] == '.') {
			map[posX][posY] = '.';
			map[posX+1][posY] = 'v';
			posX += 1;
		} else {
			map[posX][posY] = 'v';
		}
	}
	
	public static void left() {
		dir = '<';
		if (inRange(posX, posY-1) && map[posX][posY-1] == '.') {
			map[posX][posY] = '.';
			map[posX][posY-1] = '<';
			posY -= 1;
		} else {
			map[posX][posY] = '<';
		}
	}
	
	public static void right() {
		dir = '>';
		if (inRange(posX, posY+1) && map[posX][posY+1] == '.') {
			map[posX][posY] = '.';
			map[posX][posY+1] = '>';
			posY += 1;
		} else {
			map[posX][posY] = '>';
		}
	}
	
	public static void shoot() {
		if (dir == '^') {
			for (int x = posX-1; x >= 0; x--) {
				if (map[x][posY] == '#') break;  // 강철 벽
				if (map[x][posY] == '*') {
					map[x][posY] = '.';
					break;
				}
			}
		}
		else if (dir == 'v') {
			for (int x = posX+1; x < H; x++) {
				if (map[x][posY] == '#') break;  // 강철 벽
				if (map[x][posY] == '*') {
					map[x][posY] = '.';
					break;
				}
			}
		}
		else if (dir == '<') {
			for (int y = posY-1; y >= 0; y--) {
				if (map[posX][y] == '#') break;  // 강철 벽
				if (map[posX][y] == '*') {
					map[posX][y] = '.';
					break;
				}
			}
		}
		else if (dir == '>') {
			for (int y = posY+1; y < W; y++) {
				if (map[posX][y] == '#') break;  // 강철 벽
				if (map[posX][y] == '*') {
					map[posX][y] = '.';
					break;
				}
			}
		}
	}

}
