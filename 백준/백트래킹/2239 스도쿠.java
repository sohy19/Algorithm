import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

	 static int[][] sudoku;
	    static List<int[]> bin;

	    public static void main(String[] args) throws IOException {
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        StringBuilder sb = new StringBuilder();
	        
	        sudoku = new int[9][9];
	        bin = new ArrayList<>();

	        for (int i = 0; i < 9; i++) {
	            String line = br.readLine();
	            for (int j = 0; j < 9; j++) {
	                sudoku[i][j] = line.charAt(j) - '0';
	                if (sudoku[i][j] == 0) {
	                    bin.add(new int[] {i, j});
	                }
	            }
	        }
	        game(0);
	        for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sb.append(sudoku[i][j]);
				}
				sb.append('\n');
			}
	        System.out.println(sb);
	    }

	    static public boolean game(int idx) {
	  
	        if (idx == bin.size()) {
	            return true;
	        }

	        for (int i = 1; i < 10; i++) {
	            sudoku[bin.get(idx)[0]][bin.get(idx)[1]] = i;
	            if (check(bin.get(idx)[0], bin.get(idx)[1])) {
	                if (game(idx + 1)) {
	                	return true;
	                }
	            }
	            sudoku[bin.get(idx)[0]][bin.get(idx)[1]] = 0;	            	
	            
	        }
	        return false;

	    }

	    static public boolean check(int x, int y) {
	        // 행 확인
	        boolean[] use = new boolean[10];
	        for (int i = 0; i < 9; i++) {
	            if (sudoku[x][i] == 0) continue;
	            if (use[sudoku[x][i]]) {
	                return false;
	            }
	            use[sudoku[x][i]] = true;
	        }

	        // 열 확인
	        use = new boolean[10];
	        for (int i = 0; i < 9; i++) {
	            if (sudoku[i][y] == 0) continue;
	            if (use[sudoku[i][y]]) {
	                return false;
	            }
	            use[sudoku[i][y]] = true;
	        }

	        // 3*3 확인
	        use = new boolean[10];
	        for (int i = x/3*3; i < x/3*3+3; i++) {
	            for (int j = y/3*3; j < y/3*3+3; j++) {
	                if (sudoku[i][j] == 0) continue;
	                if (use[sudoku[i][j]]) {
	                    return false;
	                }
	                use[sudoku[i][j]] = true;
	            }
	        }

	        return true;
	    }
}
