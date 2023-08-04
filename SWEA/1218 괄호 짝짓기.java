import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 1; t <= 10; t++) {
			int len = Integer.parseInt(br.readLine());  // 문자열 길이
			Stack<String> st = new Stack<String>();
			int result = 1;
			
			// 입력 받기
			String line = br.readLine();
			String ch;
			for (int i = 0; i < len; i++) {
				ch = String.valueOf(line.charAt(i));
				
				if (ch.equals("{") || ch.equals("[") || ch.equals("(") || ch.equals("<")) {
					st.add(ch);
				} else if (ch.equals("}")) {
					if (st.isEmpty() || !st.pop().equals("{")) {
						result = 0;
						break;
					}
				} else if (ch.equals("]")) {
					if (st.isEmpty() || !st.pop().equals("[")) {
						result = 0;
						break;
					}
				} else if (ch.equals(")")) {
					if (st.isEmpty() || !st.pop().equals("(")) {
						result = 0;
						break;
					}
				} else if (ch.equals(">")) {
					if (st.isEmpty() || !st.pop().equals("<")) {
						result = 0;
						break;
						
					}
				}
				
			}
			
			System.out.println("#" + t + " " + result);
		}
		
		
	}

}
