#pragma once
#include "ResidentialBuilding.h"
class PostOffice:public Building
{
private:
	vector<PostWorker> workers;
	vector<Client> clients;
	vector<SendItem*> items;
	vector<ResidentialBuilding> houses;
	MailCar mailcar;
	vector<Review> reviews;
public:
	void AddReview(Client& nClient);
	void GiveAllItems();
	PostOffice(string addres1);
	void addClient(Client& nClient);
	void addItem(SendItem* nSendItem);
	void addWorker(PostWorker& nWorker);
	void SetMailCar(MailCar& mailcar);
	vector<SendItem*> GetItems();
	vector<Client> GetClients();
};