import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static int n, start;
	static List<ArrayList<Integer>> contact;
	static int[] depth;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int t = 1; t <= 10; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());  // 데이터 길이 
			start = Integer.parseInt(st.nextToken());  // 시작점 
			contact = new ArrayList<ArrayList<Integer>>();  // 연락망 정보 
			depth = new int[101];  // 방문 표시 
			for (int i = 0; i < 101; i++) {
				contact.add(new ArrayList<Integer>());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n/2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				contact.get(from).add(to);
			}
		
			sb.append("#").append(t).append(" ").append(bfs()).append("\n");
		}
		System.out.println(sb);
		
		
	}  // end of main
	
	public static int bfs() {
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(start);
		depth[start] = 1;
		int num = 0;
		int nowDepth = 0;
		while (!q.isEmpty()) {
			int w = q.poll();
			for (int v : contact.get(w)) {
				if (depth[v] != 0) continue;
				q.offer(v);
				depth[v] = depth[w] + 1;
				if (nowDepth < depth[v] || nowDepth == depth[v] && num < v) {
					num = v;
					nowDepth = depth[v];
				} 
			}
		}
		return num;
	}
	
}  // end of class
