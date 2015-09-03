/*
*Leetcode exercise
*Written by aresowj
*
*[Plus One]
*Given a non-negative number represented as an array of digits, plus one to the number.
*The digits are stored such that the most significant digit is at the head of the list.
*/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
 
var plusOne = function(digits) {
    len = digits.length;
    digits[len-1] += 1;
    for (var i = len-1; i >= 0; i--) {
        if (digits[i] >= 10) {
            if (i == 0) {
                digits[i] = 0;
                digits.unshift(1);
            }
            else {
                digits[i-1] += 1;
                digits[i] = 0;
            }
        }
    }
    return digits;
};