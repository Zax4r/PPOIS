#pragma once
#include <string>
#include <iostream>
#include <vector>
using namespace std;

class SendItem
{
protected:
     string name;
     string type;
     string sender;
     string recipient;
     double weight;
public:
    SendItem(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1);
    SendItem() {};
    string GetType();
    string GetName();
    string GetRecipient();
    virtual ~SendItem() {};
};
