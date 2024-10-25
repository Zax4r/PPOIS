#include "PostOffice.h"

Building::Building(string& addr)
{
	address = addr;
}

void PostOffice::AddReview(Client& nClient)
{
	string review = "REVIEW";
	reviews.push_back(Review(review, nClient));
	for (auto& a:clients)
	{
		if(a.GetName()==nClient.GetName()){return;}
	}
	clients.push_back(nClient);
}

void PostOffice::GiveAllItems()
{
	for (int i = 0; i < clients.size(); i++) {
		bool recivied = false;
		for (int j = 0; j < items.size();j++) {
			if (clients[i].GetName() == items[j]->GetRecipient())
			{
				recivied = true;
				cout << clients[i].GetName() << " Took a ";
				if (Letter* letter = dynamic_cast<Letter*>(items[j]))
				{
					cout << "Letter";
				}
				else if (Package* package = dynamic_cast<Package*>(items[j]))
				{
					cout << "Package";
				}
				else if (Combined* combined = dynamic_cast<Combined*>(items[j]))
				{
					cout << "Combined";
				}
				cout << ". Named " << items[j]->GetName();
				items.erase(items.begin() + j--);
			}
		}
		if (recivied){
			clients.erase(clients.begin() + i--);
		}
	}
}

PostOffice::PostOffice(string addres1):Building(addres1)
{
	
}

void PostOffice::addClient(Client& nClient)
{
	clients.push_back(nClient);
}

void PostOffice::addItem(SendItem* nSendItem)
{
	items.push_back(nSendItem);
}

void PostOffice::addWorker(PostWorker& nWorker)
{
	workers.push_back(nWorker);
}

void PostOffice::SetMailCar(MailCar& mailcar)
{
	this->mailcar = mailcar;
}

vector<Client> PostOffice::GetClients()
{
	return clients;
}

vector<SendItem*> PostOffice::GetItems()
{
	return items;
}

void ResidentialBuilding::AddResident(Client a)
{
	residents.push_back(a);
}

bool ResidentialBuilding::isLivingThere(Client& resident)
{
	bool isliving = false;
	for (auto& liver : residents) {
		isliving = liver.GetName() == resident.GetName();
		if (isliving)
			return true;
	}
	return false;
}
