import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

// public class Main {
// 	static int R, C, maxDist;
// 	static char[][] map;
// 	static HashMap<Character, Integer> alpha;
// 	static int[] dx = {0, 0, 1, -1};
// 	static int[] dy = {1, -1, 0, 0};
	
// 	public static void main(String[] args) throws IOException {
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 		StringTokenizer st = new StringTokenizer(br.readLine());
// 		StringBuilder sb = new StringBuilder();
		
// 		R = Integer.parseInt(st.nextToken());  // 행
// 		C = Integer.parseInt(st.nextToken());  // 열
// 		map = new char[R][C];
// 		for (int i = 0; i < R; i++) {
// 			String line = br.readLine();
// 			for (int j = 0; j < C; j++) {
// 				map[i][j] = line.charAt(j);
// 			}
// 		}
// 		// 알파벳 hash map 생성
// 		// 지나간 알파벳은 1, 지나가지 않은 알파벳은 0 으로 표시
// 		alpha = new HashMap<Character, Integer>();
// 		char ch = 'A';
// 		for (int i = 0; i <26 ; i++) {
// 			alpha.put((char)(ch + i), 0);
// 		}
				
// 		alpha.put(map[0][0], 1);
// 		dfs(0, 0, 1);
// 		sb.append(maxDist);
// 		System.out.println(sb);
// 	}
	
// 	public static boolean inRange(int x, int y) {
// 		return 0 <= x && x < R && 0 <= y && y < C;
// 	}
	
// 	public static void dfs(int x, int y, int dist) {
// 		for (int i = 0; i < 4; i++) {			
// 			int nx = x + dx[i];
// 			int ny = y + dy[i];
// 			if (inRange(nx, ny)) {
// 				if (alpha.get(map[nx][ny]) == 1) {  // 이미 지나간 알파벳일 경우
// 					maxDist = Math.max(maxDist, dist);
// 					continue;
// 				}
// 				alpha.put(map[nx][ny], 1);
// 				dfs(nx, ny, dist+1);
// 				alpha.put(map[nx][ny], 0);
// 			}
// 		}
// 		return;
// 	}
// }


public class Main {
	static int R, C, maxDist;
	static char[][] map;
	static boolean[] visited;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		R = Integer.parseInt(st.nextToken());  // 행
		C = Integer.parseInt(st.nextToken());  // 열
		map = new char[R][C];
		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = line.charAt(j);
			}
		}
		
		// 지나온 알파벳 표시하는 visited 배열
		// index: 알파벳 - 65
		visited = new boolean[26];
		visited[map[0][0]-65] = true;
				
		dfs(0, 0, 1);
		sb.append(maxDist);
		System.out.println(sb);
	}
	
	public static boolean inRange(int x, int y) {
		return 0 <= x && x < R && 0 <= y && y < C;
	}
	
	public static void dfs(int x, int y, int dist) {

		for (int i = 0; i < 4; i++) {			
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (inRange(nx, ny)) {
				if (visited[map[nx][ny]-65]) {  // 이미 지나간 알파벳일 경우
					maxDist = Math.max(maxDist, dist);
					continue;
				}
				visited[map[nx][ny]-65] = true;
				dfs(nx, ny, dist+1);
				visited[map[nx][ny]-65] = false;
			}
		}
		return;
	}
}
