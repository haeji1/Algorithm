import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	static int[] target;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int m = Integer.parseInt(br.readLine());
		target = new int[m];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			target[i] = Integer.parseInt(st.nextToken());
		}
		
//		print(target, m);
		
		for (int i = 0; i < m; i++) {
			if (binarySearch(target[i]) >= 0) System.out.println(1);
			else System.out.println(0);
		}
		
	}

	private static int binarySearch(int i) {
		int start = 0;
		int end = arr.length - 1;
		while (start <= end) {
			// 중간부터 탐색시작
			int mid = (start + end) / 2;
			if (i > arr[mid]) {
				start = mid + 1;
			}
			else if (i < arr[mid]){
				end = mid - 1;
			}
			else {
				return mid;
			}
		}
		return -1;
	}

	private static void print(int[] arr, int n) {
		for (int i = 0; i < n; i++) {
			System.out.print(arr[i]+" ");
		}
		
	}

}
