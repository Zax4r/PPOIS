#pragma once
#include "Letter.h"
#include "Package.h"
class Combined :public virtual  Letter, public virtual  Package
{
public:
    using Letter::GetName;
    using Letter::GetType;
    using Letter::GetRecipient;
    Combined() {};
    Combined(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, const string& message1, const double volume1);
};