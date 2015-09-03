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