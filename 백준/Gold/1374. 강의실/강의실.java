import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] arr = new int[n][2];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		

		// 시작시간과 끝시간에 맞춰 정렬
		Arrays.sort(arr, new Comparator<int[]>() {
			public int compare(int[] o1, int[] o2) {
				if (o1[0] == o2[0]) return o1[1] - o2[1];
				return o1[0] - o2[0];
			}
		});
		
//		print(arr, n);
		
//		int end = arr[0][1];
		
		// 우선순위 큐 생성
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		pq.add(arr[0][1]);
		
		// 다음 강의시간부터 탐색
		for (int i = 1; i < arr.length; i++) {
			if (pq.peek() <= arr[i][0]) pq.poll();
			pq.add(arr[i][1]);
		}
		System.out.println(pq.size());
	}

	private static void print(int[][] arr, int n) {
		for (int i = 0; i < n; i++) {
			System.out.println(arr[i][0]+" "+ arr[i][1]);
		}
		
	}

}
