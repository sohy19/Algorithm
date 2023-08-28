import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static char[][] map;
	static int[] dx = {0 , 1};
	static int[] dy = {1, 0};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		map = new char[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = st.nextToken().charAt(0);
			}
		}
		
	}
	
	public static void dfs(int x, int y, int num, int op) {
		if (x == N-1 && y == N-1) {
			
			return;
		}
		for (int i = 0; i < 2; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < N && ny < N) {
				switch (map[nx][ny]) {
				case '*':
					
					break;

				default:
					break;
				}
			}
		}
	}

}
