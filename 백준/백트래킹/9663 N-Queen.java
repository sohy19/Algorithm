import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, col[], ans;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		col = new int[N+1];  // 1행부터 사용
		setQueen(1);
		System.out.println(ans);
		
		
	}
	
	// 같은 행에 퀸을 놓지 않는 버전
	// 놓아진 퀸의 열번호를 기록
	// 해당 퀸을 현재 행에서 가능한 모든 곳에 놓아보기
	// row: 퀸을 놓으려는 행
	private static void setQueen(int row) {
		// 가지 치기 (직전까지 놓아진 상태로)
		if (!isAvailable(row-1)) return;
		
		// 기저 조건
		if (row > N) {
			ans++;
			return;
		}
		
		// 유도 파트
		for (int c = 1; c <= N; c++) {
			col[row] = c;
			setQueen(row+1);
		}
	}
	
	// row: 마지막으로 놓아진 퀸의 행
	private static boolean isAvailable(int row) {
		for (int i = 1; i < row; i++) {
			if (col[i] == col[row] || Math.abs(col[row]-col[i]) == row-i) {
				return false;
			}
		}
		
		return true;
		
	}

}
