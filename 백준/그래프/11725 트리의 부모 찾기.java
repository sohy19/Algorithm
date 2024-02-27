import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static List<List<Integer>> tree;
    static boolean[] visited;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(st.nextToken());
        tree = new ArrayList<>();
        parent = new int[n+1];
        visited = new boolean[n+1];
        for (int i = 0; i <= n; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            tree.get(v1).add(v2);
            tree.get(v2).add(v1);
        }

        dfs(1);
        for (int i = 2; i <= n; i++) {
            sb.append(parent[i]).append("\n");
        }

        System.out.println(sb);



    }

    static public void dfs(int v) {
        visited[v] = true;

        for (int w : tree.get(v)) {
            if (!visited[w]) {
                 parent[w] = v;
                 dfs(w);
            }
        }



    }

}
