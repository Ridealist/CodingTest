#include <stdio.h>

int binary_search(int arr[], int target, int start, int end) {

    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (arr[mid] == target)
            return (mid + 1);
        else if (arr[mid] > target)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return -1;
}

int main() {

    int arr[13] = {1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15};

    int answer = binary_search(arr, 15, 0, 15);

    printf("%d\n", answer);

    return 0;
}