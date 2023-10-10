import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int r, c, t;
    static int[][] map;
    static int[] cleaner;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());  // 행
        c = Integer.parseInt(st.nextToken());  // 열
        t = Integer.parseInt(st.nextToken());  // 초
        map = new int[r][c];  // 방의 정보
        cleaner = new int[2];  // 공기청정기 위치

        int idx = 0;
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == -1) {
                    cleaner[idx++] = i;
                }
            }
        }

        for (int T = 0; T < t; T++) {
            spread();
            clean();
        }

        int sum = 2;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (map[i][j] != 0) {
                    sum += map[i][j];
                }
            }
        }

        System.out.println(sum);


    }


    public static void spread() {
        int[] dx = {0, -1, 0, 1};
        int[] dy = {1, 0, -1, 0};

        int[][] newMap = new int[r][c];

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (map[i][j] != -1 && map[i][j] != 0) {
                    int cnt = 0;
                    for (int k = 0; k < 4; k++) {
                        int x = i + dx[k];
                        int y = j + dy[k];
                        if (0 <= x && x < r && 0 <= y && y < c && map[x][y] != -1) {
                            newMap[x][y] += map[i][j] / 5;
                            cnt++;
                        }
                    }

                    map[i][j] = map[i][j] - (map[i][j] / 5) * cnt;

                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                map[i][j] += newMap[i][j];
            }
        }
    }

    public static void clean() {
        int[] dx, dy;

        for (int i = 0; i < 2; i++) {
            if (i == 0) {
                // 동 > 북 > 서 > 남
                dx = new int[] {0, -1, 0, 1};
                dy = new int[] {1, 0, -1, 0};
            }
            else {
                // 동 > 남 > 서 > 북
                dx = new int[] {0, 1, 0, -1};
                dy = new int[] {1, 0, -1, 0};
            }

            int x = cleaner[i];
            int y = 1;
            int dir = 0;
            int num = 0;
            while (true) {
                if (x == cleaner[i] && y == 0) break;

                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (!(0 <= nx && nx < r && 0 <= ny && ny < c)) {
                    dir += 1;
                    continue;
                }

                int temp = map[x][y];
                map[x][y] = num;
                num = temp;
                x = nx;
                y = ny;

            }
        }
    }


}
