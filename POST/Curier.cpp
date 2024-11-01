#include "Curier.h"

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
	cout << " " << toSend->GetName() << ". By Curier";
}