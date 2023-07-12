import java.util.*;

class Solution {
	public int[] solution(String[] operations) {
		int[] answer = {0,0};
    PriorityQueue<Integer> minp = new PriorityQueue<>(); // 최소 힙
    PriorityQueue<Integer> maxp = new PriorityQueue<>(Collections.reverseOrder()); 
																												// 최대 힙

    for(String op : operations){
        String[] split_op = op.split(" "); // 공백을 제외하여 배열로 저장

        if(split_op[0].equals("I")){ // 첫 문자가 I 일때 삽입
            minp.add(Integer.parseInt(split_op[1]));
            maxp.add(Integer.parseInt(split_op[1]));
        }

        if(split_op[0].equals("D")){
            if(!minp.isEmpty()){
                if(split_op[1].equals("1")){
                    int max = maxp.peek(); 
										// 최대 힙에서 최댓값을 뽑아내고 이를 각 큐에서 제거
                    maxp.remove(max);
                    minp.remove(max);
                }else{
                    int min = minp.peek(); 
										// 최소 힙에서 최솟값을 뽑아내고 이를 각 큐에서 제거
                    minp.remove(min);
                    maxp.remove(min);
                }
            }
        }

    }

    if(!maxp.isEmpty()){
        answer[0] = maxp.peek();
        answer[1] = minp.peek();
    }

    return answer;
	}
}