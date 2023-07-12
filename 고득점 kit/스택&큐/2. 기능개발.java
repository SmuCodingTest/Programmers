import java.util.*;
class Solution {
	public int[] solution(int[] progresses, int[] speeds) {
	int[] answer = {};
	int[] temp = new int[100];
	int day=0;
  for(int i=0; i<progresses.length; i++){
        while(progresses[i] + speeds[i] * day < 100){
            day++;
        }
        temp[day]++;
    }

    int count=0;
    for(int i : temp){
        if(i != 0)
            count++;
    }

    answer = new int[count];

    count=0;
    for(int i : temp){
        if(i != 0){
            answer[count++] = i;
        }
    }

    return answer;
	}
}