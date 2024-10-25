#pragma once
#include <string>
#include"PostWorker.h"
using namespace std;
class Review
{
private:
	string message;
	Client author;
public:
	Review(string msg,Client& authr);
};

