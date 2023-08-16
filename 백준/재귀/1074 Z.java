import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, r, c, cnt;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		int size = (int) Math.pow(2, N);
		calc(0, 0, size);
	}
	
	public static void calc(int x, int y, int size) {
		if (size == 2) {
			calcZ(x, y, size);
			return;
		}
		
		size /= 2;
		if (r < x+size && c < y+size) {
			calc(x, y, size);  // 제1사분면			
		} else if (r < x+size && c >= y+size) {
			cnt += size * size;
			calc(x, y+size, size);  // 제2사분면			
		} else if (r >= x+size && c < y+size) {
			cnt += (size * size) * 2;
			calc(x+size, y, size);  // 제3사분면			
		} else {
			cnt += (size * size) * 3;
			calc(x+size, y+size, size);  // 제4사분면			
		}
		
	}
	
	public static void calcZ(int x, int y, int size) {
		int[] dx = {0, 0, 1, 1};
		int[] dy = {0, 1, 0, 1};
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx == r && ny == c) {
				System.out.println(cnt);
				System.exit(0);
			} else {
				cnt++;
			}
		}
		
	}

}
