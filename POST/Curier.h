#pragma once
#include"PostWorker.h"
#include"Client.h"
class Curier :public PostWorker
{
public:
	Curier() :PostWorker("unnamed_worker", 18, 100) {};
	virtual void Delivery(Client& recipinet, SendItem*& toSend);
};
