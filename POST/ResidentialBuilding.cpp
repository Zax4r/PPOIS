#include "ResidentialBuilding.h"


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
