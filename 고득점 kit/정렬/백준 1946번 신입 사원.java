

import java.io.*;
import java.util.*;

public class boj1946 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트케이스
        int count;

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            count = 1;
            int[][] new_member = new int[n][2];

            for (int j = 0; j < n; j++) {
                String[] str = br.readLine().split(" ");
                new_member[j][0] = Integer.parseInt(str[0]);
                new_member[j][1] = Integer.parseInt(str[1]);
            }
            Arrays.sort(new_member, (o1, o2) -> o1[0] - o2[0]);

            int min = new_member[0][1];
            for (int j = 1; j < n; j++) {
                if(min > new_member[j][1]) {
                    min = new_member[j][1];
                    count++;
                }
            }
            System.out.println(count);
        }

    }
}