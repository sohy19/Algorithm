import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int N, ans;
	static boolean line[], left[], right[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		line = new boolean[N+1];
		right= new boolean[2*N+1];		
		left = new boolean[2*N+1];
		setQueen(1);
		System.out.println(ans);
		
	}

	private static void setQueen(int row) {
		if (row > N) {
			ans++;
			return;
		}
		
		for (int c = 1; c <= N; c++) {
			if (line[c] || right[row+c] || left[row-c+N]) continue;
			line[c] = true;
			right[row+c] = true;
			left[row-c+N] = true;
			setQueen(row+1);
			line[c] = false;
			right[row+c] = false;
			left[row-c+N] = false;
		}
	}

}
