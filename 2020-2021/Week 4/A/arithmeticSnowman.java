import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
 
public class Test2 {
    
    public static void main(String[] args) throws IOException {
 
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] arr = new int[n+1];
        
        for(int i=1; i<=n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        
        int ans = Integer.MIN_VALUE;
        for(int i = 1; i <= n; ++i) {
            for(int j = i+1; j <= n; ++j) {
                int found = 0;
                int l = j+1; int r = n; 
                while(l<=r) {
                    int mid = (l+r)/2;
                    if(arr[mid] - arr[j] == arr[j] - arr[i]) {
                        found = mid;
                        break; 
                    }
                    else if (arr[mid]-arr[j] > arr[j]-arr[i]) r = mid - 1;
                    else l = mid + 1;
                }
                if(found!=0) ans = Math.max(ans, arr[i]+arr[j]+arr[found]); 
            }
        }
        System.out.println(ans);
        
    }
}
