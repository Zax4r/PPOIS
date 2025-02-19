#include "Package.h"

Package::Package(const string& name1, const string& type1, const string& sender1, const string& recipient1, \
	const double weight1, const double volume1) :SendItem(name1, type1, sender1, recipient1, weight1)
{
	volume = volume1;
}

double Package::GetVolume()
{
	return volume;
}