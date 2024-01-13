import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    static String docs;
    static String keyword;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        docs = br.readLine();
        keyword = br.readLine();

        System.out.println(calcCnt());
    }

    public static int calcCnt() {
        int cnt = 0;

        for (int i = 0; i <= docs.length()-keyword.length(); i++) {
            boolean flag = true;
            for (int j = 0; j < keyword.length(); j++) {
                if (docs.charAt(i+j) != keyword.charAt(j)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cnt++;
                i = i + keyword.length() - 1;
            }
        }

        return  cnt;
    }
}
