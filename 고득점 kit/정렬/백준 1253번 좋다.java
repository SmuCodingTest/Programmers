package com.example.demo2;

import java.util.*;
/* 문제 : 좋다
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.
https://www.acmicpc.net/problem/1253
 */
public class boj1253 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int good=0;
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);

        for(int i = 0; i<arr.length; i++) {
            int find = arr[i];


            int left = 0; // 시작지점
            int right = arr.length - 1; // 배열 끝지점
            int sum = 0;


            while(left < right){
                sum = arr[left] + arr[right];
                if(sum == find){
                    if(i == left)
                        left++;
                    else if(right == i)
                        right--;
                    else{
                        good++;
                        break;
                    }
                }

                if(arr[left] + arr[right] > find) //find 보다 크면 높은 값을 가르키는 right--
                    right--;
                else if(arr[left] + arr[right] < find) // find보다 작으면 left++
                    left++;


            }
        }

        System.out.println(good);
    }
}