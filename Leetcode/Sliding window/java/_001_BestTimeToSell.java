/*
Problem Description : we are given an array of daily stock prices where the i-th element represents the price of a given stock on day i.
                      our goal is to maximize our profit by choosing a single day to buy one stock and a different day in the future to sell
                      that stock. You must return the maximum profit possible from this transaction; if no profit can be achieved, return 0.

Problem Approach : To maximize profit, you want to buy at the absolute lowest price and sell at the highest price after that purchase.
                   You don't need to compare every possible pair of days. Instead, as you walk through the timeline, you only need to know,
                   "What is the cheapest price I could have bought at before today?" If today's price is higher than that minimum, you have 
                   a potential profit.
                   1. Track Minimum: Iterate through the array once while maintaining a variable for the lowest price seen so far (min).
                   2. Update Minimum: If the current day's price is lower than our min, update min (you found a better buying opportunity).
                   3. Calculate Profit: If the current day's price is higher than min, calculate the difference (current_price - min) and
                      update our maximum profit if this difference is the largest seen yet.


*/

// Optimal Approach : 
class Solution {
    public int maxProfit(int[] prices){

        int min = prices[0];
        int profit = 0;

        for(int i = 0; i < prices.length; i++){
            if (prices[i] < min){
                min = prices[i];
            }

            profit = Math.max(profit, prices[i] - min);
        }
        return profit;
    }
}

//Time Complexity : O(n)
//Space Complexity : O(1)