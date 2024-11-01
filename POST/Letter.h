#pragma once
#include"SendItem.h"
class Letter : public SendItem
{
protected:
    string message;
public:
    Letter(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const string& message1);
    Letter() {};
    string GetMessage();
};