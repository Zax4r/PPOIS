
#pragma once

#include<iostream> 
#include<utility>
#include<math.h> 
class Point
{
public:
	int X, Y;
	Point(int X, int Y) :X(X), Y(Y) {}
	Point() {};
	bool operator==(const Point& other) const
	{
		return X == other.X && Y == other.Y;
	}
};

class Vector
{
private:
	Point A, B;
	int Xnapr, Ynapr;
public:
	Vector(int Ax, int Ay, int Bx, int By);
	~Vector();
	std::pair<Point, Point> getPoint();
	double getLength();
	Vector operator+(Vector& other);
	Vector& operator+=(Vector& other);
	Vector operator*(int numb);
	Vector& operator*=(int numb);
	Vector operator-(Vector& other);
	Vector& operator-=(Vector& other);
	double operator*(Vector& other);
	double operator^(Vector& other);
	bool operator<(Vector& other);
	bool operator>(Vector& other);
	bool operator ==(const Vector& other) const;
	Vector operator=(Vector& other);
	friend std::ostream& operator <<(std::ostream& out, Vector& a);
	Vector(const Vector& other);
};
