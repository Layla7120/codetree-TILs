import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    static int[] visited;
    static int n;
    static ArrayList<Integer> ans = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        visited = new int[n+1];
        choose(0);

    }

    public static void choose(int count){
        if(count == n){
            for(int i=0; i<n; i++){
                System.out.print(ans.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for(int i=n; i>0; i--){
            if(visited[i] == 1)
                continue;

            visited[i] = 1;
            ans.add(i);

            choose(count + 1);

            ans.remove(ans.size() - 1);
            visited[i] = 0;
        }
    }
}