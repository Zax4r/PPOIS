#include "pch.h"
#include "Vector.h"
TEST(TestCaseName, TestVectorGetLengthPos) {
	Vector a(0, 0, 3, 4);
  EXPECT_EQ(a.getLength(), 5);
  EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorGetLengthNeg) {
	Vector a(0, 0, -3, -4);
	EXPECT_EQ(a.getLength(), 5);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorGetLengthDif) {
	Vector a(0, 0, -3, 4);
	EXPECT_EQ(a.getLength(), 5);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorGetPoint) {
	Vector a(0, 0, 3, 4);
	Point A(0, 0), B(3, 4);
	auto Para = std::pair<Point, Point>(A,B);
	EXPECT_EQ(a.getPoint(),Para);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorSumOperatorWithPos) {
	Vector a(0, 0, 3, 4),b(0,0,2,8);
	EXPECT_EQ((a+b).getLength(),13);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorSumOperatorWithNeg) {
	Vector a(0, 0, 3, 4), b(0, 0, -3,-4);
	EXPECT_EQ((a+b).getLength(), 0);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorSubtOperatorWithPos) {
	Vector a(5, 2, 3, 4), b(5, 2, 3, 4),nulVec(0, 0, 0, 0);
	EXPECT_EQ((a-b), nulVec);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorSubtOperatorWithNeg) {
	Vector a(5, 2, 3, 4), b(-5,- 2, -3, -4);
	EXPECT_EQ((a - b).getLength(),sqrt(32));
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorMultOperWithPosNumb) {
	Vector a(0, 0, 3, 4);
	EXPECT_EQ((a*2).getLength(), 10);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorMultOperWithNegNumb) {
	Vector a(0, 0, 3, 4);
	EXPECT_EQ((a*-2).getLength(), 10);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorDotOperWithPosVect) {
	Vector a(0, 0, 3, 4),b(1,2,5,10);
	EXPECT_EQ(a*b,44);
	EXPECT_TRUE(true);
}


TEST(TestCaseName, TestVectorDotOperWithNegVect) {
	Vector a(2,1, 3, 4), b(-1, -2, -5, -10);
	EXPECT_EQ(a * b, -28);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorAngleOperWithOpposVect) {
	Vector a(2, 1, 3, 4), b(-2, -1,- 3,- 4);
	EXPECT_EQ(a^b,-1);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorAngleOperWithSameVect) {
	Vector a(2, 1, 3, 4), b(4, 2, 6, 8);
	EXPECT_EQ(a ^ b, 1);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorGreThOperatorWithVect) {
	Vector a(0, 0, 3, 4), b(0, 0, -3, -4);
	EXPECT_EQ(a>b,false);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorCopyConstr) {
	Vector a(0, 0, 3, 4);
	Vector b(a);
	EXPECT_EQ(a==b,true);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorAssigmentOper) {
	Vector a(0, 0, 3, 4);
	Vector b(0,0,0,0);
	b = a;
	EXPECT_EQ(a == b, true);
	EXPECT_TRUE(true);
}

TEST(TestCaseName, TestVectorAssigmentOperDel) {
	Vector a(0, 0, 3, 4);
	Vector b(0, 0, 0, 0);
	b = a;
	a.~Vector();
	EXPECT_EQ(b.getLength(), 5);
	EXPECT_TRUE(true);
	std::cin.get();
}