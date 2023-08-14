import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, white, blue;
	static int[][] map;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		calc(0, 0, N);
		System.out.println(white);
		System.out.println(blue);
	}
	
	public static void calc(int r, int c, int size) {
		
		int sum = 0;
		for (int i = r; i < r+size; i++) {
			for (int j = c; j < c+size; j++) {
				sum += map[i][j];
			}
		}
		if (sum == 0) {  // 전체 흰색
			white++;
		} else if (sum == size*size) {  // 전체 파란색
			blue++;
		} else {
			int half = size / 2;
			calc(r, c, half);
			calc(r, c+half, half);
			calc(r+half, c, half);
			calc(r+half, c+half, half);
		}
		
	}

}
