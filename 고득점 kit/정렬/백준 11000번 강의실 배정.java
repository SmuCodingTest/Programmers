
/* 강의실 배정
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!
https://www.acmicpc.net/problem/11000
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj11000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] room = new int[n][2];

        for (int j = 0; j < n; j++) {
            String[] str = br.readLine().split(" ");
            room[j][0] = Integer.parseInt(str[0]);
            room[j][1] = Integer.parseInt(str[1]);
        }

        Arrays.sort(room, (o1, o2) -> o1[0] - o2[0]);
        PriorityQueue<Integer> p = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int start = room[i][0];
            int end = room[i][1];
            if (!p.isEmpty() && p.peek() <= start) { 
                p.poll();
            }
            p.offer(end);
        }
        System.out.println(p.size());

    }
}