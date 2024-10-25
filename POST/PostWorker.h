#pragma once
#include"SendItem.h"
using namespace std;
class Human
{
private:
	string name;
	int age;
public:
	Human(string name, int age);
	Human() {};
	string GetName();
};

class PostWorker : public Human
{
private:
	int selery;
public:
	PostWorker(string name1, int age1, int selery1);
};

class Client :public Human
{
private:
	string telephone;
	string address;
public:
	Client(string name, int age, string telephone, string address);
	Client() {};
	string GetAddress();
};

class Curier:public PostWorker
{
public:
	Curier():PostWorker("unnamed_worker",18,100) {};
	virtual void Delivery(Client& recipinet, SendItem*& toSend);
};

class Driver :public Curier
{
public:
	void Delivery(Client& recipinet, SendItem*& toSend) override;
	Driver():Curier() {};
};