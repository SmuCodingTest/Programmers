import java.util.*;

class Solution {
	public int solution(int[] scoville, int K) {
		PriorityQueue<Integer> p = new PriorityQueue<>();
		int answer = 0;
    for(int i=0;i<scoville.length; i++)
        p.add(scoville[i]);

    while(p.peek() < K){
        if(p.size()==1) return -1;
        if(!p.isEmpty())
            p.add(p.poll()+p.poll()*2);
        answer++;
    }

    return answer;
 }
}