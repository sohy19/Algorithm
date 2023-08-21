import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  // 입력 받기
		
		int T = Integer.parseInt(br.readLine());  // 요리시간 초
		int A = 0;  // A 조작 횟수
		int B = 0;  // B 조작 횟수
		int C = 0;  // C 조작 횟수
		
		if (T % 10 == 0) {
			A = T / 300;  // A 조작 횟수 계산
			B = (T % 300) / 60;  // B 조작 횟수 계산
			C = ((T % 300) % 60) / 10;  // C 조작 횟수 계산
		}
		
		if (A == 0 && B == 0 && C == 0) {
			// 초가 10초 단위로 떨어지지 않아 3개의 버튼으로 맞출 수 없는 경우
			System.out.println(-1);
		} else {
			System.out.print(A + " ");  // A 조작 횟수 출력
			System.out.print(B + " ");  // B 조작 횟수 출력
			System.out.print(C + " ");  // C 조작 횟수 출력
		}

	}

}
