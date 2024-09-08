/*!
*\file Vector.cpp
*\brief Cpp file for Vector class
*/
#include "Vector.h"



/*!
\brief Constructor for Vector
*
\param[in] Ax X coordinate of the start of the vector
\param[in] Ay Y coordinate of the start of the vector
\param[in] Bx X coordinate of the end of the vector
\param[in] By Y coordinate of the end of the vector
*/

Vector::Vector(int Ax, int Ay, int Bx, int By) :A(Ax, Ay), B(Bx, By)
{
	this->Xnapr = B.X - A.X;
	this->Ynapr = B.Y - A.Y;
}

Vector::~Vector()
{

}
/*!
	\brief getPoint() method

	This method is needed to return a pair of points (the start and end of the vector)
	\return pair of Points of the Vector
	\see <utility>
*/
std::pair<Vector::Point, Vector::Point> Vector::getPoint()
{
	return std::pair<Vector::Point, Vector::Point>(A,B);
}
/*!
	\brief getLength() method

	
	This method is needed to return a lentgh of Vector
	\return lentgh of Vector
	\see <math.h>
*/
double Vector::getLength()
{
	return sqrt(Xnapr*Xnapr +Ynapr*Ynapr);
}
/*!
* \brief operator+(Vector& other)
* 
* \return vector that starts from the same point as vector this, and is the result of the sum of two vectors
*/
Vector Vector::operator+(Vector& other)
{
	int newXnapr = Xnapr + other.Xnapr;
	int newYnapr = Ynapr + other.Ynapr;
	return Vector(A.X,A.Y,A.X+newXnapr,A.Y+newYnapr);
}
/*!
* \brief operator+=
* 
* \return same as a operator +, but changes a current vector
* \see operator+(Vector& other)
*/
Vector& Vector::operator+=(Vector& other)
{
	Xnapr += other.Xnapr;
	Ynapr += other.Ynapr;		
	return *this;
}
/*!
* \brief operator-(Vector& other)
*
* \return vector that starts from the same point as vector this, and is the result of the difference of two vectors
*/
Vector Vector::operator-(Vector& other)
{
	Vector temp = other * (-1);
	return temp + *this;
}
/*!
* \brief operator-=(Vector& other)
*
* \return same as a operator -, but changes a current vector
* \see operator-(Vector& other)
*/
Vector& Vector::operator-=(Vector& other)
{
	Vector temp = (*this - other);
	*this = temp;
	return *this;
}
/*!
* \brief operator*(int numb)
* 
* \param [in] numb the number by which the vector is multiplied
* \return vector with multiplied coordinates
*/
Vector Vector::operator*(int numb)
{
	return Vector(A.X*numb, A.Y * numb, B.X * numb, B.Y * numb);
}
/*!
* \brief operator*=(int numb)
* 
* \param [in] numb the number by which the vector is multiplied
* \return same as a operator *, but changes a current vector
* \see operator*(int numb)
*/
Vector& Vector::operator*=(int numb)
{
	Vector temp = *this * numb;
	*this = temp;
	return *this;
}
/*!
* \brief operator*(Vector& other)
*
* \param [in] other the vector by which the vector is multiplied
* \return number, because its a dot product of vectors
*/
double Vector::operator*(Vector& other)
{
	return (Xnapr*other.Xnapr + Ynapr*other.Ynapr);
}
/*!
* \brief operator^(Vector& other)
*
* \param [in] other the vector with which to find the angle
* \return number, cos of angle between out vectors
*/
double Vector::operator^(Vector& other)
{
	double proiz = *this * other;
	auto module1 =sqrt((Xnapr * Xnapr + Ynapr * Ynapr) * (other.Xnapr * other.Xnapr + other.Ynapr * other.Ynapr));
	return (proiz / module1);
}
/*!
* \brief operator<(Vector& other)
*
* in this operator we compare length of vectors
* \param [in] other the vector with which we compare
* \return bool
*/
bool Vector::operator<(Vector& other)
{
	return this->getLength()<other.getLength();
}
/*!
* \brief operator>(Vector& other)
*
* in this operator we compare length of vectors
* \param [in] other the vector with which we compare
* \return bool
*/
bool Vector::operator>(Vector& other)
{
	return this->getLength() > other.getLength();
}
/*!
* \brief operator==(Vector& other)
*
* in this operator we compare length of vectors
* \param [in] other the vector with which we compare
* \return bool
*/
bool Vector::operator==(Vector& other)
{
	return this->getLength() == other.getLength();
}
/*!
* \brief operator=(Vector& other)
*
* in this operator we assign our vector to vector other
* \param [in] other the vector we want to assign
* \return vector
*/
Vector Vector::operator=(Vector& other)
{
	if (&other != this)
	{
		this->A = other.A;
		this->B = other.B;
		this->Xnapr = other.Xnapr;
		this->Ynapr = other.Ynapr;
	}
	return *this;
}
/*!
* \brief Copy constructor
* 
* \param [in] other the vector we want to copy
* \return copied vector 
*/
Vector::Vector(const Vector& other)
{
	Vector temp(other.A.X, other.A.Y,other.B.X,other.B.Y);
	*this = temp;
}
/*!
* \brief operator<<(std::ostream& out,Vector& other)
*
* in this operator we insert to out our start/end point of vector a
* \param [in] a the vector  
* \return out the result output stream 
*/
std::ostream& operator<<(std::ostream& out, Vector& a)
{
	out << "Start:"<<a.A.X<<a.A.Y<<" End:"<<a.B.X<<a.B.Y;
	return out;
}
