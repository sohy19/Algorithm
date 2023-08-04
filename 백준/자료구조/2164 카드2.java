import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		ArrayDeque<Integer> q = new ArrayDeque<Integer>();
		for (int i = 0; i < n; i++) {				
			q.addLast(i+1);
		}
		
		/** 어떤 동작 해야 하는지 표시 
		 * 1: 제일 위에 있는 카드 제거, 2: 제일 위에 있는 카드 맨 밑으로 */
		int ch = 1;
		int cnt = n;
		
		while (cnt != 1) {
			if (ch == 1) {
				q.pollFirst();
				ch = 2;
				cnt--;
			} else {
				q.addLast(q.pollFirst());
				ch = 1;
			}
		}
		
		System.out.println(q.pollFirst());
		
	}
		
}
