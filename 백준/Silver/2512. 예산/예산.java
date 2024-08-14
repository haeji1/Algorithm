import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[] arr;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		arr = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		int maxVal = 0;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			sum += arr[i];
			if (arr[i] > maxVal) maxVal = arr[i];
		}
		m = Integer.parseInt(br.readLine());
		
//		print(arr);
		
		// 요청 예산의 합이 총 예산값 이하일 때 그대로 
//		System.out.println(sum);
		if (sum <= m) {
			System.out.println(maxVal);
		} else {
			binarySearch(0,maxVal);
		}
	}

	private static void print(int[] arr) {
		for (int i = 0; i < n; i++) {
			System.out.print(arr[i]+" ");
		}
		
	}
	
	private static void binarySearch(int start, int end) {
		while (start <= end) {
			int mid = (start + end) / 2;
			// mid값을 상한액으로 보고 계산
			if (calcBudget(mid) > m) {
				end = mid - 1;
			}
			else if (calcBudget(mid) <= m) {
				start = mid + 1;
			}
		}
		System.out.println(end);
	}

	private static int calcBudget(int budget) {
		int tmp = 0;
		for (int i = 0; i < n; i++) {
			if (arr[i] <= budget) {
				tmp += arr[i];
			} else {
				tmp += budget;
			}
		}
		return tmp;
	}

}
