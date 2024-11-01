#pragma once
#include "SendItem.h"
class Package : public SendItem
{
protected:
    double volume;
public:
    Package(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const double volume1);
    Package() {};
    double GetVolume();
};