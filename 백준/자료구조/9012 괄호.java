import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			String str = br.readLine();
			sb.append(isValid(str) ? "YES" : "NO").append('\n');
		}
		
		System.out.println(sb);
	}
	
	public static boolean isValid (String str) {
		Stack<Character> st = new Stack<>();
		
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == '(') {
				st.push('(');
			} else {
				if (!st.isEmpty()) {
					st.pop();
				} else {
					return false;
				}
				
			}
		}
		
		if (!st.isEmpty()) return false;
		return true;
		
	}
}
