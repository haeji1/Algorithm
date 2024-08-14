import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;
	static int[] arr;
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		// 최소 길이 : max값, 최대 길이 : sum값
		int sum = 0;
		int maxLength = 0;
		for (int i = 0; i < n; i++) {
			if (maxLength < arr[i]) maxLength = arr[i];
			sum += arr[i];
		}
		System.out.println(binarySearch(maxLength, sum, m));
	}

	
	private static int binarySearch(int start, int end, int target) {
		while (start < end) {
			// 탐색할 블루레이 길이
			int mid = (start + end) / 2;
			// 블루레이 수 줄여야함 -> 길이 늘리기
			if (getCount(mid) > target) {
				start = mid + 1;
			}
			else {
				end = mid;
			}
		}
		
		return start;
	}


	// 현재 길이에 따른 블루레이의 수
	private static int getCount(int mid) {
		int cnt = 1;
		int sum = mid;
		for (int i = 0; i < n; i++) {
			if (arr[i] > sum) {
				sum = mid;
				cnt += 1;
			}
			sum -= arr[i];
		}
		return cnt;
	}

}
