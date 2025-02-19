#pragma once

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <sstream>
#include "Vector.h"
TEST(Vector_Test, TestVectorGetLengthPos) {
	Vector a(0, 0, 3, 4);
  EXPECT_EQ(a.getLength(), 5);
}

TEST(Vector_Test, TestVectorGetLengthNeg) {
	Vector a(0, 0, -3, -4);
	EXPECT_EQ(a.getLength(), 5);
}

TEST(Vector_Test, TestVectorGetLengthDif) {
	Vector a(0, 0, -3, 4);
	EXPECT_EQ(a.getLength(), 5);
}

TEST(Vector_Test, TestVectorGetPoint) {
	Vector a(0, 0, 3, 4);
	Point A(0, 0), B(3, 4);
	auto Para = std::pair<Point, Point>(A,B);
	EXPECT_EQ(a.getPoint(),Para);
}

TEST(Vector_Test, TestGetPointCoordinates) {
    Vector a(0, 0, 3, 4);
    auto points = a.getPoint();
    EXPECT_EQ(points.first.X, 0);
    EXPECT_EQ(points.first.Y, 0);
    EXPECT_EQ(points.second.X, 3);
    EXPECT_EQ(points.second.Y, 4);
}


TEST(Vector_Test, TestVectorSumOperatorWithPos) {
	Vector a(0, 0, 3, 4),b(0,0,2,8);
	EXPECT_EQ((a+b).getLength(),13);
}

TEST(Vector_Test, TestVectorSumOperatorWithNeg) {
	Vector a(0, 0, 3, 4), b(0, 0, -3,-4);
	EXPECT_EQ((a+b).getLength(), 0);
}

TEST(Vector_Test, TestVectorSubtOperatorWithPos) {
	Vector a(5, 2, 3, 4), b(5, 2, 3, 4),nulVec(0, 0, 0, 0);
	EXPECT_EQ((a-b), nulVec);
	EXPECT_TRUE(true);
}


TEST(Vector_Test, TestVectorSubtOperatorWithNeg) {
	Vector a(5, 2, 3, 4), b(-5,- 2, -3, -4);
	EXPECT_EQ((a - b).getLength(),sqrt(32));
}

TEST(Vector_Test, TestVectorMultOperWithPosNumb) {
	Vector a(0, 0, 3, 4);
	EXPECT_EQ((a*2).getLength(), 10);
}

TEST(Vector_Test, TestVectorMultOperWithNegNumb) {
	Vector a(0, 0, 3, 4);
	EXPECT_EQ((a*-2).getLength(), 10);
}

TEST(Vector_Test, TestVectorDotOperWithPosVect) {
	Vector a(0, 0, 3, 4),b(1,2,5,10);
	EXPECT_EQ(a*b,44);
}


TEST(Vector_Test, TestVectorDotOperWithNegVect) {
	Vector a(2,1, 3, 4), b(-1, -2, -5, -10);
	EXPECT_EQ(a * b, -28);
}

TEST(Vector_Test, TestVectorAngleOperWithOpposVect) {
	Vector a(2, 1, 3, 4), b(-2, -1,- 3,- 4);
	EXPECT_EQ(a^b,-1);
}

TEST(Vector_Test, TestVectorAngleOperWithSameVect) {
	Vector a(2, 1, 3, 4), b(4, 2, 6, 8);
	EXPECT_EQ(a ^ b, 1);
}

TEST(Vector_Test, TestVectorGreThOperatorWithVect) {
	Vector a(0, 0, 3, 4), b(0, 0, -3, -4);
	EXPECT_EQ(a>b,false);
}

TEST(Vector_Test, TestVectorCopyConstr) {
	Vector a(0, 0, 3, 4);
	Vector b(a);
	EXPECT_EQ(a,b);
}

TEST(Vector_Test, TestVectorAssigmentOper) {
	Vector a(0, 0, 3, 4);
	Vector b(0,0,0,0);
	b = a;
	EXPECT_EQ(a ,b);
}

TEST(Vector_Test, TestVectorMulEqNum) {
	Vector a(0, 0, -3, 4);
	a*=2;
	EXPECT_EQ(a.getLength(), 10);
}

TEST(Vector_Test, TestVectorSumEql) {
	Vector a(0, 0, 3, 4);
	a+=a;
	EXPECT_EQ(a.getLength(), 10);
}

TEST(Vector_Test, TestVectorSubtEql) {
	Vector a(0, 0, 3, 4),b(0,0,3,4);
	a-=b;
	EXPECT_EQ(a.getLength(),0);
}


TEST(Vector_Test, TestVectorEqualOper) {
	Vector a(0, 0, 3, 4);
	Vector b(0, 0, 3, 4);
	EXPECT_EQ(a==b,true);
}

TEST(Vector_Test, TestVecLessOper) {
	Vector a(0, 0, 3, 4),b(0,0,1,2);
	EXPECT_EQ(a<b,false);
	EXPECT_EQ(a>b,true);
}

TEST(Vector_Test, TestVecOutputOper) {
	Vector a(0, 0, 1, 2);
	std::ostringstream oss;
	oss<<a;
	EXPECT_EQ(oss.str(),"Start:(0,0) End:(1,2)");
}




