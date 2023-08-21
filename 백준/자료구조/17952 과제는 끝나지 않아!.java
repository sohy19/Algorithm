import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  // 입력 받기
		StringTokenizer st = new StringTokenizer(br.readLine());  // 입력 받기
		
		// 입력
		int N = Integer.parseInt(st.nextToken());  // 분
		int work[][] = new int[N][3];  // 업무 정보
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());  // 입력 받기
			int w = Integer.parseInt(st.nextToken());  // 업무 주어졌는지 여부
			work[i][0] = w;  // 업무 주어졌는지 여부 저장
			if (w == 1) {
				// 업무가 주어진 경우 점수와 시간 저장
				work[i][1] = Integer.parseInt(st.nextToken());  // 만점 점수 저장
				work[i][2] = Integer.parseInt(st.nextToken());  // 시간 저장
				
			}
		}
		
		
		int score = 0;  // 업무 평가 점수 저장
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < N; i++) {
			if (work[i][0] == 1) {
				work[i][2]--;
				if (work[i][2] == 0) {
					score += work[i][1];
				} else {
					stack.push(i);
				}
			}
			else {
				if (!stack.isEmpty()) {
					int idx = stack.pop();
					work[idx][2]--;
					if (work[idx][2] == 0) {
						score += work[idx][1];
					} else {
						stack.push(idx);
					}
				}
			}
		}
		
		System.out.println(score);
		
	}

}
