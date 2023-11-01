class Solution {
    public int[][] transpose(int[][] arr) {
        int rows=arr[0].length;
        int coloumns=arr.length;

        int Transpose[][]=new int[rows][coloumns];
        for (int i = 0; i<coloumns;i++){
            for (int j =0; j <rows; j++){
               Transpose[j][i]=arr[i][j];
            }
        }

        return Transpose;
    }
}