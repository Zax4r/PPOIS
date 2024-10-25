#include "PostWorker.h"

Human::Human(std::string name, int age) :name(name), age(age)
{

}

string Human::GetName()
{
	return name;
}


PostWorker::PostWorker(string name1, int age1, int selery1):Human(name1,age1)
{
	selery = selery1;
}


Client::Client(string name , int age , string telephone1, string address1) :Human(name, age)
{
	telephone = telephone1;
	address = address1;
}

string Client::GetAddress()
{
	return address;
}

void Curier::Delivery(Client& recipinet, SendItem*& toSend)
{
	cout << "Recipient " << recipinet.GetName() << " recivied an item: ";
	if (Letter* letter = dynamic_cast<Letter*>(toSend))
	{
		cout << "Letter";
	}
	else if (Package* package = dynamic_cast<Package*>(toSend))
	{
		cout << "Package";
	}
	else if (Combined* combined = dynamic_cast<Combined*>(toSend))
	{
		cout << "Combined";
	}
	cout << " " << toSend->GetName()<<". By Curier";
}

void Driver::Delivery(Client& recipinet, SendItem*& toSend)
{
	cout << "Recipient " << recipinet.GetName() << " recivied an item:  ";
	if (Letter* letter = dynamic_cast<Letter*>(toSend))
	{
		cout << "Letter";
	}
	else if (Package* package = dynamic_cast<Package*>(toSend))
	{
		cout << "Package ";
	}
	else if (Combined* combined = dynamic_cast<Combined*>(toSend))
	{
		cout << "Combined ";
	}
	cout << " " << toSend->GetName()<<". By Driver";
}
