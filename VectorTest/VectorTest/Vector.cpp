#include "pch.h"
#include "Vector.h"

Vector::Vector(int Ax, int Ay, int Bx, int By) :A(Ax, Ay), B(Bx, By)
{
	this->Xnapr = B.X - A.X;
	this->Ynapr = B.Y - A.Y;
}

Vector::~Vector()
{

}

std::pair<Point,Point> Vector::getPoint()
{
	return std::pair<Point,Point>(A, B);
}

double Vector::getLength()
{
	return sqrt(Xnapr * Xnapr + Ynapr * Ynapr);
}

Vector Vector::operator+(Vector& other)
{
	int newXnapr = Xnapr + other.Xnapr;
	int newYnapr = Ynapr + other.Ynapr;
	if(newXnapr!=0 && newYnapr!=0)
	return Vector(A.X, A.Y, A.X + newXnapr, A.Y + newYnapr);
	return Vector(0, 0, 0, 0);
}

Vector& Vector::operator+=(Vector& other)
{
	Xnapr += other.Xnapr;
	Ynapr += other.Ynapr;
	return *this;
}

Vector Vector::operator-(Vector& other)
{

	return other * (-1) + *this;
}

Vector& Vector::operator-=(Vector& other)
{
	Vector result = (*this - other);
	*this = result;
	return *this;
}

Vector Vector::operator*(int numb)
{

	return Vector(A.X, A.Y, A.X +(Xnapr*numb), A.Y +(Ynapr* numb));
}

Vector& Vector::operator*=(int numb)
{
	Vector result = *this * numb;
	*this = result;
	return *this;
}

double Vector::operator*(Vector& other)
{
	return (Xnapr * other.Xnapr + Ynapr * other.Ynapr);
}

double Vector::operator^(Vector& other)
{
	double proiz = *this * other;
	auto module1 = sqrt((Xnapr * Xnapr + Ynapr * Ynapr) * (other.Xnapr * other.Xnapr + other.Ynapr * other.Ynapr));
	return (proiz / module1);
}

bool Vector::operator<(Vector& other)
{
	return this->getLength() < other.getLength();
}

bool Vector::operator>(Vector& other)
{
	return this->getLength() > other.getLength();
}

bool Vector::operator==(const Vector& other) const
{
	return A == other.A && B == other.B;
}

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

Vector::Vector(const Vector& other) : A(other.A.X, other.A.Y), B(other.B.X, other.B.Y)
{
	this->Xnapr = B.X - A.X;
	this->Ynapr = B.Y - A.Y;
}

std::ostream& operator<<(std::ostream& out, Vector& a)
{
	out << "Start:" << a.A.X << a.A.Y << " End:" << a.B.X << a.B.Y;
	return out;
}

