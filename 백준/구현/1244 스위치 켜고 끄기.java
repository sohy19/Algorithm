import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 입력 받기 
		int n = Integer.parseInt(br.readLine());  // 스위치 개수
		int[] state = new int[n+1];  // 스위치 상태 (0은 사용 x)
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i < state.length; i++) {
			state[i] = Integer.parseInt(st.nextToken());
		}
		int stuNum = Integer.parseInt(br.readLine());  // 학생 수
		int[][] stuInfo = new int[stuNum][2];  // [성별, 받은 수]
		for (int i = 0; i < stuNum; i++) {
			st = new StringTokenizer(br.readLine());
			stuInfo[i][0] = Integer.parseInt(st.nextToken());
			stuInfo[i][1] = Integer.parseInt(st.nextToken());
			
		}
		
		
		// 풀이
		for (int i = 0; i < stuNum; i++) {
			if (stuInfo[i][0]  == 1) {  // 남학생 
				int num = stuInfo[i][1];  // 받은 수 
				while (num <= n) {
					state[num] = state[num] == 0 ? 1 : 0;
					num += stuInfo[i][1];
				}
			} else {  // 여학생 
				int num = stuInfo[i][1];  // 받은 수 
				int range = n - num < num - 1 ? n - num : num - 1;  // 대조할 수 있는 최대 거리
				int possibleRange = 0;
				for (int j = 1; j <= range; j++) {
					if (state[num-j] == state[num+j]) {
						possibleRange = j;
					} else {
						break;
					}
				}
				state[num] = state[num] == 0 ? 1 : 0;
				for (int j = 1; j <= possibleRange; j++) {
					state[num+j] = state[num+j] == 0 ? 1 : 0;
					state[num-j] = state[num-j] == 0 ? 1 : 0;
				}
				
			}
			
		}  // end of for
		
		// 출력 
		for (int i = 1; i < state.length; i++) {
			System.out.printf("%d ", state[i]);
			if (i % 20 == 0) {
				System.out.println();  // 한 줄에 스위치가 20개 이상 넘어가면 줄바꿈
			}
		}
		
	}  // end of main
}  // end of class
