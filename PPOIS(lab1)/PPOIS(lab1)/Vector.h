/**
 * \file Vector.h
 * \author Zahar Bedarik
 * \brief header file for class Vector
 */
#pragma once

#include<iostream> ///<iostream> library for console input/output
#include<utility> ///<iostream> library for console input/output
#include<math.h> ///<math.h> Library for mathematical sqrt
	class Vector
	{
	private:
		class Point///\brief Creating a supporting Point class
		{
		public:
			int X, Y;
			Point(int X, int Y) :X(X), Y(Y) {}
			Point() {};
		};
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
		bool operator ==(Vector& other);
		Vector operator=(Vector& other);
		friend std::ostream& operator <<(std::ostream& out,Vector& a);
		Vector(const Vector& other);
	};
