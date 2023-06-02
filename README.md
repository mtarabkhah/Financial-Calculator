# Financial Calculator

This repository contains a Python program called `finance_calculators.py` that provides two financial calculators: an investment calculator and a home loan repayment calculator.

## Getting Started

To use the financial calculators, follow these steps:

1. Clone the repository to your local machine or download the `finance_calculators.py` file directly.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory where you saved the `finance_calculators.py` file.

## Usage

To run the program, execute the following command in your terminal or command prompt:

```
python finance_calculators.py
```

Upon running the program, you will see the following initial output:

```
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed:
```

You can choose either 'investment' or 'bond' by typing your selection and pressing Enter. The program is case-insensitive, so you can enter your selection in any case.

### Investment Calculator

If you select 'investment', the program will ask you to input the following information:

1. The amount of money that you are depositing.
2. The interest rate (as a percentage).
3. The number of years you plan on investing.
4. Whether you want "simple" or "compound" interest.

Based on your inputs, the program will calculate and display the appropriate amount that you will get back after the given period, at the specified interest rate.

### Home Loan Repayment Calculator

If you select 'bond', the program will ask you to input the following information:

1. The present value of the house.
2. The interest rate.
3. The number of months you plan to take to repay the bond.

Based on your inputs, the program will calculate and display the amount that you will have to repay on a monthly basis.

Please note that for the home loan repayment calculator, the interest rate should be provided as an annual rate. The program will automatically convert it to a monthly interest rate.

## Examples

Here are a few examples to demonstrate how the program works:

### Example 1: Investment Calculator

```
Enter either 'investment' or 'bond' from the menu above to proceed:invesTment
Enter the amount of money that you are depositing : 5000
Enter the interest rate (as a percentage) : 5
Enter the number of years you plan on investing : 3
Do want "simple" or "compound" interest : compound
You will get back 5788.13 after 3.0 years at the interest rate of 5.0%
```

### Example 2: Home Loan Repayment Calculator

```
Enter either 'investment' or 'bond' from the menu above to proceed:bond
Enter the present value of the house : 200000
Enter the interest rate (as a percentage) : 6
Enter the number of months you plan to take to repay the bond :180
You have to repay 1687.71 each month
```

## Conclusion

With this program, you can easily calculate the interest on your investments or determine the monthly repayment amount for a home loan. Feel free to explore and use this program for your financial calculations.

If you have any questions or suggestions, please don't hesitate to reach out.

Happy calculating!
