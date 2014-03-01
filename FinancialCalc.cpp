/*
 * FinancialCalc.cpp
 *
 *  Created on: Mar 1, 2014
 *      Author: Christian
 */
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

//Declaration of global variables

float APR = 0.0;
float compound = 0.0;
int loan = 0;
long owed = 0;


void Inputfunction ()
{
	/* Using a float precision number for the APR, using anything else will result in
	program not running like expected */

	float InputNumber = 0.0;
	cout << "Enter APR rate: " ;
	cin >> InputNumber;

	int InputNumberm = 0;
	cout << "Enter loan amount: " ;
	cin >> InputNumberm;

	int year = 0;
	cout << "Enter compound period in years: " ;
	cin >> year;

	APR = 1 + InputNumber;
	loan = InputNumberm;
	compound = year;

}

void Multiplyfunction ()
{
	float PV = 0.0;

	PV = pow (APR, compound);

	long total = 0;
	total = loan * PV;

	owed = total;

}
int main ()
{
	Inputfunction();
	Multiplyfunction();

	string name;
	cout << "What is your gansta name: " ;
	cin >> name;

	cout << name << " owes money in the amount of: " << owed;

	return 0;

}

