class Solution {
    public int getSum(int a, int b) {
        int op1 = a ^ b;
        int op2 = a & b;
        while (op2 != 0) {
            int tmp = op1 ^ (op2 << 1);
            op2 = op1 & (op2 << 1);
            op1 = tmp ;  
        }
        
        return op1;
        
    }
}