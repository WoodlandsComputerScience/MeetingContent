import java.io.IOException;
import java.util.Scanner;
 
public class awildgoosechase {
 
    public static void main(String[] args) throws IOException {
 
        Scanner sc = new Scanner(System.in);
 
        int N = sc.nextInt(); int T = sc.nextInt();
 
        int[] freq = new int[N+1];
        for(int i=0; i<N; i++) {
        	int F = sc.nextInt();
        	int D = sc.nextInt();
 
        	if(D==-1) {
        		T--;
        		freq[F]--;
        	}else {
        		freq[D]++;
        	}
        }
 
        boolean found = false;
        for(int i=1; i<=N; i++) {
        	if(freq[i] == T) {
        		System.out.print(i + " ");
        		found = true;
        	}
        }
 
        if(!found) {
        	System.out.println(-1);
        }
 
 
    }
}
