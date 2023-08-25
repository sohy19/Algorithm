import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, d, k, c;
	static int[] sushi;
	static int[] eat;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());  // 접시 수
		d = Integer.parseInt(st.nextToken());  // 초밥 가짓수
		k = Integer.parseInt(st.nextToken());  // 연속해서 먹는 접시 수
		c = Integer.parseInt(st.nextToken());  // 쿠폰 번호
		
		sushi = new int[N+k];  // 초밥 종류
		eat = new int[d+1];  // 초밥 인덱스 저장
		
		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}
		
		for (int i = 0; i < k; i++) {
			sushi[N+i] = sushi[i];
		}
		
		int cnt = 0;  // 먹을 수 있는 초밥 가짓수
		int maxCnt = 0;  // 먹을 수 있는 초밥 최대 가짓수
		
		eat[c] = 1;  // 쿠폰 처리
		
		for (int i = 0; i < k; i++) {
			if (++eat[sushi[i]] == 1) cnt++;
		}
		
		maxCnt = cnt;
		for (int i = 1; i <= N; i++) {
			eat[sushi[i-1]]--;  // 구간 맨 앞 스시 제외
			if (eat[sushi[i-1]] == 0) cnt--;  // 구간 내 중복 스시 없음
			
			eat[sushi[i+k-1]]++;
			if (eat[sushi[i+k-1]] == 1) cnt++; 
			
			maxCnt = Math.max(maxCnt, cnt);
		}
		
		System.out.println(maxCnt + 1);
	
	
	
	}

}
