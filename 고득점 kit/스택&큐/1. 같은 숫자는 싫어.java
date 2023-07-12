import java.util.*;

public class Solution {
	public int[] solution(int []arr) {
		int[] answer = {};
    ArrayList<Integer> list = new ArrayList<Integer>();

    int check = -1;

    for(int i=0; i<arr.length; i++){
        if(arr[i] != check){
            list.add(arr[i]);
            check = arr[i];
        }
    }
    answer = new int[list.size()];

   for(int i=0; i<list.size(); i++){
        answer[i] = list.get(i);
    }

    return answer;
	}
}