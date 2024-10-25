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

class Letter : public SendItem
{
protected:
    string message;
public:
    Letter(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const string& message1);
    Letter() {};
    string GetMessage();
};

class Package : public SendItem
{
protected:
    double volume;
public:
    Package(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const double volume1);
    Package() {};
    double GetVolume();
};

class Combined:public virtual  Letter, public virtual  Package
{
public:
    using Letter::GetName;
    using Letter::GetType;
    using Letter::GetRecipient;
    Combined() {};
    Combined(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const string& message1, const double volume1);
};