}import java.util.*;

class Solution {
	public int solution(int[][] jobs) {
		int answer = 0;
		int index = 0;
		int count = 0;
		int end = 0; // 작업 수행 후의 시간
		int len = jobs.length;  
  
		Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
				// 배열을 시작시간 순으로 오름차순 정렬

	  PriorityQueue<int[]> p = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]); 
				// 우선순위 큐를 소요시간 순으로 오름차순 정렬

    while(count < len) {

    	while(index < len && jobs[index][0] <= end) {
       		p.add(jobs[index++]);
       	}

       	if(p.isEmpty()) {
       		end = jobs[index][0]; // 다음 작업의 시작 시간
       	}else {
       		int[] temp = p.poll();
       		answer += temp[1] + end - temp[0];
       		end += temp[1];
       		count++;
       	}
    }

    return answer/len;
	}
}