import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        
        int answer = 0;
        int len = priorities.length;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for(int i=0; i<len; i++){
            q1.offer(i);
            q2.offer(priorities[i]);
        }
        
        int count = 0;
        
        while(!q2.isEmpty()){
            int size = q1.size();
            int n1 = q1.poll();
            int n2 = q2.poll();
            
            for(int a : q2){
                if(n2<a){
                    q1.offer(n1);
                    q2.offer(n2);
                    break;
                }
            }
            if(size == q1.size()+1) answer++;
            if(size == q1.size()+1 && n1 == location) break;
        }
        
        
        return answer;
    }
}