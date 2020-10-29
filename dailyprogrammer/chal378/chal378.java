import java.util.Arrays;

//https://www.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/

public class chal378
{
  //returns an array that has all zeroes from arr removed
  public static int[] eliminateZero(int[] arr)
  {
    int numNotZeroes = 0;
    for(int i = 0; i < arr.length; i++)
    {
      if(arr[i] != 0)
      {
        numNotZeroes++;
      }
    }

    int[] temp = new int[numNotZeroes];
    int tempIndex = 0;
    for(int i = 0; i < arr.length; i++)
    {
      if(arr[i] != 0)
      {
        temp[tempIndex] = arr[i];
        tempIndex++;
      }
    }
    return temp;
  }

  //returns an array that has been sorted in descending order
  public static int[] sortDesc(int[] arr)
  {
    int[] temp = new int[arr.length];
    int[] temp2 = new int[arr.length];

    //deep copy arr into temp
    for(int i = 0; i < arr.length; i++)
    {
      temp[i] = arr[i];
    }

    Arrays.sort(temp);

    //reverse temp and store in temp2
    for(int i = temp.length - 1; i >= 0; i--)
    {
      temp2[temp.length - 1 - i] = temp[i];
    }

    return temp2;
  }

  //returns whether length of arr is less than num
  public static boolean lengthCheck(int num, int[] arr)
  {
    return arr.length < num;
  }

  //subtracts 1 from the first num indexes of arr
  public static void frontReduction(int num, int[] arr)
  {
    int index = num;
    if(index > arr.length)
    {
      index = arr.length;
    }
    for(int i = 0; i < index; i++)
    {
      arr[i]--;
    }
  }

  //returns the arr without the index given
  public static int[] removeIndex(int[] arr, int index)
  {
    int[] temp = new int[arr.length - 1];

    if(index >= 0 && index < arr.length)
    {
      int count = 0;
      for(int i = 0; i < arr.length; i++)
      {
        if(i != index)
        {
          temp[count] = arr[i];
          count++;
        }
      }
    }

    return temp;
  }

  //Havel-Hakimi Alg
  //returns whether everyone is telling the truth or someone is lying
  public static boolean hh(int[] arr)
  {
    while(true)
    {
      arr = eliminateZero(arr);
      if(arr.length == 0)
      {
        return true;
      }
      else
      {
        arr = sortDesc(arr);
        int N = arr[0];
        arr = removeIndex(arr, 0);
        if(lengthCheck(N, arr))
        {
          return false;
        }
        else
        {
          frontReduction(N, arr);
        }
      }
    }
  }

  //return an array as a String for easy printing
  public static String printArray(int[] arr)
  {
    String arrayStr = "[ ";
    if(arr.length > 0)
    {
      for(int i = 0; i < arr.length-1; i++)
      {
        arrayStr += arr[i] + ", ";
      }
      arrayStr += arr[arr.length-1] + " ";
    }
    arrayStr += "]";
    return arrayStr;

  }

  public static void main(String[] args)
  {
    //test zero elim function [WORKS]
    //int[] arr = {4, 0, 0, 1, 3}; //[0] #[1, 0, 2, 3, 4, 0, 8]
    //arr = eliminateZero(arr);
    //System.out.println(printArray(arr));

    //test sortDesc function [WORKS]
    //int[] arr = {};
    //arr = sortDesc(arr);
    //System.out.println(printArray(arr));

    //test lengthCheck function [WORKS]
    //int[] arr = {};
    //System.out.println(lengthCheck(1, arr));

    //test frontReduction function [WORKS]
    //int[] arr = {5, 4, 3, 2, 1};
    //frontReduction(5, arr);
    //System.out.println(printArray(arr));

    //test hh function [WORKS]
    int[] arr = {5, 3, 0, 2, 6, 2, 0, 7, 2, 5};
    System.out.println(printArray(arr) + " => " + hh(arr));
    int[] arr2 = {4, 2, 0, 1, 5, 0};
    System.out.println(printArray(arr2) + " => " + hh(arr2));
    int[] arr3 = {3, 1, 2, 3, 1, 0};
    System.out.println(printArray(arr3) + " => " + hh(arr3));
    int[] arr4 = {16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16};
    System.out.println(printArray(arr4) + " => " + hh(arr4));
    int[] arr5 = {14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12};
    System.out.println(printArray(arr5) + " => " + hh(arr5));
    int[] arr6 = {15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3};
    System.out.println(printArray(arr6) + " => " + hh(arr6));
    int[] arr7 = {6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1};
    System.out.println(printArray(arr7) + " => " + hh(arr7));
    int[] arr8 = {2, 2, 0};
    System.out.println(printArray(arr8) + " => " + hh(arr8));
    int[] arr9 = {3, 2, 1};
    System.out.println(printArray(arr9) + " => " + hh(arr9));
    int[] arr10 = {1, 1};
    System.out.println(printArray(arr10) + " => " + hh(arr10));
    int[] arr11 = {1};
    System.out.println(printArray(arr11) + " => " + hh(arr11));
    int[] arr12 = {};
    System.out.println(printArray(arr12) + " => " + hh(arr12));
  }
}
