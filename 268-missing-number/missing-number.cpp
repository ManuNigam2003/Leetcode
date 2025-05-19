class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {    
        int nums_size = nums.size();
        int64_t sum = nums_size * (nums_size +1) /2 ;
        for(int i = 0 ; i < nums.size() ; i++)
        {
            sum -= nums[i];
        }
        return sum;
    }
};