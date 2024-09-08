/*!
 * \file Tests.cpp
 * \brief file to test different methods of Vector 
 */

#include "Vector.h"
using namespace std;
/*!
* \brief Test1()
* 
* this Test check the getLength() method
*/
void Test1()
{
	Vector Fir(1,1,3,3),Sec(-1,-1,-3,-3);
	if (Fir.getLength() == sqrt(8) && Sec.getLength()==sqrt(8))
		cout << "getLength method is correct";
	else cout << "getLength method is incorrect";
	cout << endl;
}
/*!
* \brief Test2()
* 
* this Test check the getPoint() method
*/
void Test2()
{
	Vector Fir(1, 1, 3, 3);
	auto para = Fir.getPoint();
	if (para.first.X == 1 && para.first.Y == 1 && para.second.X == 3 && para.second.Y == 3)
		cout << "getPoint method is correct";
	else cout << "getPoint method is incorrect";
	cout << endl;
}
/*!
* \brief Test3()
* 
* this Test check the + operator
*/
void Test3()
{
	Vector Fir(1, 1, 3, 3),Sec(-2,-2,-4,-4);
	if ((Fir+Sec).getLength()==0)
		cout << "+ operator is correct";
	else cout << "+ operator is incorrect";
	cout << endl;
}
/*!
* \brief Test4()
* 
* this Test check the - operator
*/
void Test4()
{
	Vector Fir(1, 1, 3, 3), Sec(-2, -2, -4, -4);
	if ((Fir - Sec).getLength() == Fir.getLength() * 2)
		cout << "- operator is correct";
	else cout << "- operator is incorrect";
	cout << endl;
}
/*!
* \brief Test5()
* 
* this Test check the *(number) operator
*/
void Test5()
{
	Vector Fir(1, 1, 3, 3);
	if ((Fir*2).getLength() == Fir.getLength() * 2 && (Fir*0).getLength()==0)
		cout << "*(number) operator is correct";
	else cout << "*(number) operator is incorrect";
	cout << endl;
}
/*!
* \brief Test6()
* 
* this Test check the *(another vector) operator
*/
void Test6()
{
	Vector Fir(1, 1, 3, 3), Sec(-2, -2, -4, -4);
	if ((Fir*Sec)==-8 && (Sec*Fir)==-8)
		cout << "*(another vector) operator is correct";
	else cout << "*(another vector) operator is incorrect";
	cout << endl;
}
/*!
* \brief Test7()
* 
* this Test check the ^ operator
*/
void Test7()
{
	Vector Fir(1, 1, 3, 3), Sec(-2, -2, -4, -4);
	if ((Fir ^ Sec) == -1 && (Sec^Fir)==-1)
		cout << "^ operator is correct";
	else cout << "^ operator is incorrect";
	cout << endl;
}
/*!
* \brief main()
* 
* in this part of code, all the methods and operators could be checked
*/
int main()
{
	bool esc = false;
	while (!esc) {
		int option = 0;
		cout << "\nChoose an option:\n1.Test getLength method\n2.Test getPoint method"
			 <<endl<<"3.Test +operator \n4.Test -operator\n5.Test *(number)operator"
			 <<endl<<"6.Test *(vector)operator \n7.Test ^operator\n8.Test ALL!!\n0.Leave"<< endl;
		cin >> option;
		switch (option)
		{
		case 1:
			Test1();
			break;
		case 2:
			Test2();
			break;
		case 3:
			Test3();
			break;
		case 4:
			Test4();
			break;
		case 5:
			Test5();
			break;
		case 6:
			Test6();
			break;
		case 7:
			Test7();
			break;
		case 8:
			Test1();
			Test2();
			Test3();
			Test4();
			Test5();
			Test6();
			Test7();
			break;
		case 0:
			esc = true;
			break;
		default:
			cout << "No such option!";
			esc = true;
		}
	}
}