#pragma once
#include "Admin.h"
class Review
{
private:
	Client author;
	string message;
public:
	Review(string& message, Client& author);
	string getMessage();
};

