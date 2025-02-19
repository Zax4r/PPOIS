#pragma once
#include"SendItem.h"
#include"Human.h"

class PostWorker : public Human
{
private:
	int selery;
public:
	PostWorker(string name1, int age1, int selery1);
};