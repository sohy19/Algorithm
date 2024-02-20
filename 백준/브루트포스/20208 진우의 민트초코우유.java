import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M, H;

    static int maxCnt;

    static List<int[]> nodes;
    static boolean[] visited;

    static int[] startNode;
    static int[][] dist;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());   // 마을 크기
        M = Integer.parseInt(st.nextToken());   // 초기 체력
        H = Integer.parseInt(st.nextToken());   // 민트초코우유 마실 때 증가하는 체력
        nodes = new ArrayList<>();

        // 민트초코우유 좌표 저장
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int type = Integer.parseInt(st.nextToken());
                if (type == 2) {
                    nodes.add(new int[]{i, j});
                }
                else if (type == 1) {
                    startNode = new int[] {i, j};
                }
            }
        }

        dist = new int[nodes.size()][nodes.size()];
        visited = new boolean[nodes.size()];

        // 거리 계산
        for (int i = 0; i < nodes.size(); i++) {
            for (int j = i+1; j < nodes.size(); j++) {
                dist[i][j] = Math.abs(nodes.get(i)[0] - nodes.get(j)[0]) + Math.abs(nodes.get(i)[1] - nodes.get(j)[1]);
            }
        }


        dfs(startNode[0], startNode[1], M, 0);
        System.out.println(maxCnt);

    }
    
    public static void dfs(int x, int y, int power, int cnt) {
        for (int i = 0; i < dist.length; i++) {
            if (!visited[i] && Math.abs(nodes.get(i)[0] - x) + Math.abs(nodes.get(i)[1] - y) <= power) {
                visited[i] = true;
                dfs(nodes.get(i)[0], nodes.get(i)[1], power - (Math.abs(nodes.get(i)[0] - x) + Math.abs(nodes.get(i)[1] - y)) + H, cnt + 1);
                visited[i] = false;
            }
        }
        if (Math.abs(x - startNode[0]) + Math.abs(y - startNode[1]) <= power) {
            maxCnt = Math.max(maxCnt, cnt);
        }
    }

}
