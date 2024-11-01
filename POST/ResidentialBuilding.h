#include "Building.h"
class ResidentialBuilding :public Building
{
private:
	vector<Client> residents;
public:
	ResidentialBuilding(string address) :Building(address) {};
	void AddResident(Client a);
	bool isLivingThere(Client& resident);
};