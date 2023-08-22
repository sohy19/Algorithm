import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int L, C;
	static String[] candi, code;

	public static void main(String[] args) throws IOException {
		
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());  // 암호 길이 
		C = Integer.parseInt(st.nextToken());  // 암호에 사용된 알파 후보 개수 
		candi = new String[C];  // 암호에 사용된 알파 후보 
		String line = br.readLine();
		candi = line.split(" ");
		
		code = new String[L];  // 암호 
		Arrays.sort(candi);
		makeCode(0, 0, 0, 0, 0);
		
	}  // end of main
	
	// 암호 문자 개수, 모음 개수, 자음 개수, 중복 체크 
	private static void makeCode(int start, int cnt, int vowel, int consonant, int flag) {
		if (cnt == L) {
			if (vowel >= 1 && consonant >= 2) {
				for (int i = 0; i < L; i++) {
					System.out.print(code[i]);
				}
				System.out.println();
			}
			return;
		}
		
		for (int i = start; i < C; i++) {
			if ((flag & 1 << i) != 0) continue;
			code[cnt] = candi[i];
			if (candi[i].equals("a") || candi[i].equals("e") || candi[i].equals("i") || candi[i].equals("o") || candi[i].equals("u")) {
				makeCode(i+1, cnt+1, vowel+1, consonant, flag | 1<<i);
			} else {
				makeCode(i+1, cnt+1, vowel, consonant+1, flag | 1<<i);
			}
		}
		
	}
	
}  // end of class
