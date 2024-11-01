#pragma once
#include "Driver.h"
using namespace std;
class Review
{
private:
	string message;
	Client author;
public:
	Review(string msg,Client& authr);
};

