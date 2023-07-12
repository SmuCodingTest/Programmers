import java.util.*;

// 1. Arraylist 버전 (2번보다 더 빠름)
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int j=0;j<commands.length;j++){
            ArrayList<Integer> arr = new ArrayList<>();

            for(int i=commands[j][0]; i<=commands[j][1]; i++){
                arr.add(array[i-1]);    
            }
            Collections.sort(arr);
            answer[j] = arr.get(commands[j][2]-1);
        }
                
        return answer;
    }
}
// 2. 배열 버전
//-------------------------------------------------------------------
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int j=0;j<commands.length;j++){
            int[] arr = new int[commands[j][1]-commands[j][0]+1];
            int count = 0;
            for(int i=commands[j][0]; i<=commands[j][1]; i++){
                arr[count] = array[i-1];    
                count++;
            }
            Arrays.sort(arr);
            answer[j] = arr[commands[j][2]-1];
        }
                
        return answer;
    }
}