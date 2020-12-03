import java.io.IOException;
import java.util.Scanner;
public class Test2 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int L = 1; int R = (int) 2e9;
        while(L <= R) {
            int mid = L + (R-L)/2;
            System.out.println(mid);
            String s = sc.next();
            if(s.equals("OK")) {
                return;
            }else if(s.equals("SINKS")) {
                L = mid + 1;
            }else {
                R = mid - 1;
            }
        }
    }
}

