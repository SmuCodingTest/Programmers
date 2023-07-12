import java.util.*;

/* 문제 : 최소 힙 1927번
널리 잘 알려진 자료구조 중 최소 힙이 있다.
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

    1. 배열에 자연수 x를 넣는다.
    2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

 */
public class boj1926 {
    public static void main(String[] args) {
        PriorityQueue<Integer> p = new PriorityQueue<>();

        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        int[] arr = new int[count];
        int zero = 0;
        while(count>0){
            int v = sc.nextInt();
            if(v > 0 )
                p.offer(v);
            if(v == 0){
                if(p.isEmpty()) {
                    arr[zero] = 0;
                    zero++;
                } else{
                    arr[zero] = p.poll();
                    zero++;
                }
            }
            count--;
        }
        for (int i = 0; i < zero; i++) {
            System.out.println(arr[i]);
        }

    }
}