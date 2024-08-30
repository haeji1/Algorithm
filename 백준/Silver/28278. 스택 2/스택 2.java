import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		LinkedList<Integer> stack = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			if (num == 1) {
				stack.push(Integer.parseInt(st.nextToken()));
			} else if (num == 2) {
				if (!stack.isEmpty()) {
					sb.append(stack.pop()+"\n");
				} else {
					sb.append(-1+"\n");
				}
			} else if (num == 3) {
				sb.append(stack.size()+"\n");
			} else if (num == 4) {
				if (stack.isEmpty()) {
					sb.append(1+"\n");
				} else sb.append(0+"\n");
			} else if (num == 5) {
				if (!stack.isEmpty()) {
					sb.append(stack.peek()+"\n");
				} else sb.append(-1+"\n");
			}
		}
		System.out.println(sb);

	}

}
