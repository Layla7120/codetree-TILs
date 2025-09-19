import java.util.Scanner;
public class Main {
    static int N, answer=0;
    static int[] arr;
    static int[][] grid;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        N = n;
        arr = new int[n];
        choose(0, 0);

        System.out.println(answer);
    }

    public static void choose(int count, int acc){
        if(count == N){
            answer = Math.max(answer, acc);
            return;
        }

        for(int i=0; i<N; i++){
            if(arr[i] != 1){
                arr[i] = 1;
                choose(count + 1, acc + grid[count][i]);
                arr[i] = 0;
            }

        }
    }
}