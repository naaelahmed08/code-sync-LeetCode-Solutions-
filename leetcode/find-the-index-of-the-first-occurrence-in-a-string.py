int strStr(char* haystack, char* needle) {
    int len1 = strlen(haystack);
    int len2 = strlen(needle);

    if(len1 < len2){
        return -1;
    }

    int j = 0;

    for(int i = 0; i <= len1; ++i ){
        if(haystack[i] != needle[j]){
            continue;
        }else{
            for(int m = i; m <= i + len2 - 1; ++m){
                if(haystack[m] == needle[j]){
                    ++j;
                    if(j == len2){
                        return i;
                    }
                }else{
                    break;
                }
            }
            j = 0;
        }
    }
return -1;
}


// int strStr(char* haystack, char* needle) {
//     int len1 = strlen(haystack);
//     int len2 = strlen(needle);

//     // If the needle is empty, return 0 (empty string is always found at index 0).
//     if (len2 == 0) return 0;

//     // If haystack is shorter than needle, return -1 (impossible to find).
//     if (len1 < len2) return -1;

//     // Iterate through the haystack, ensuring we don't go out of bounds.
//     for (int i = 0; i <= len1 - len2; ++i) {
//         int j = 0;

//         // Check if the substring starting at i matches needle.
//         while (j < len2 && haystack[i + j] == needle[j]) {
//             j++;
//         }

//         // If we matched the entire needle, return the starting index.
//         if (j == len2) {
//             return i;
//         }
//     }

//     // If no match was found, return -1.
//     return -1;
// }