#pragma once
#include"Curier.h"
class Driver :public Curier
{
public:
	void Delivery(Client& recipinet, SendItem*& toSend) override;
	Driver() :Curier() {};
};