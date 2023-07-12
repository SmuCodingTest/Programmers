

/*
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

1.  배열에 정수 x (x ≠ 0)를 넣는다.
2.  배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
    절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
 */

import java.util.*;

public class boj11286 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PriorityQueue<Integer> p = new PriorityQueue<>((o1, o2) -> {
            int abs1 = Math.abs(o1);
            int abs2 = Math.abs(o2);
            if(abs1==abs2) return o1 > o2 ? 1 : -1;
            return abs1-abs2;
        });

        int count = sc.nextInt();
        int zero = 0;
        int[] arr = new int[count];
        while(count >0){
            int v = sc.nextInt();
            if(v == 0){
                if(!p.isEmpty()) {
                    arr[zero] = p.poll();
                    zero++;
                }else{
                    arr[zero] = 0;
                    zero++;
                }
            }else{
                p.add(v);
            }
            count--;
        }

        for (int i = 0; i < zero; i++) {
            System.out.println(arr[i]);
        }

    }
}