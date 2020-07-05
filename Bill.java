/*You are having AWS account for cloud services. Suppose a bill has to be calculated accordingly to following use-
Period
For first 20 Days
1 Month
1 Year
Rate
12 Rs./Day
5 Rs./Day
1 Rs./Day
Assuming you have used it for 128 days. Calculate how much bill you have to pay?// Java implementation to calculate the bill
*/


import java.util.*;
class Bill
{
// Function to calculate the bill
public static int calculateBill(int days)
{
if (days <= 20) {
return days * 12;
}
else if (days <= 30) {
return (20 * 12)
+ (days - 20) * 5;
}
else if (days <= 365) {
return (20 * 12)
+ (10 * 5)
+ (days - 30 ) * 1;
}
return 0;
}

// Driver Code
public static void main(String args[])
{
int days = 128;
System.out.println(calculateBill(days));
}
}