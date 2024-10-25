#include "SendItem.h"

SendItem::SendItem(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1)
{
	name = name1;
	type = type1;
	sender = sender1;
	recipient = recipient1;
	weight = weight1;
}

string SendItem::GetType()
{
	return type;
}
string SendItem::GetName()
{
	return name;
}

string SendItem::GetRecipient()
{
	return recipient;
}



Letter::Letter(const string& name1, const string& type1, const string& sender1, const string& recipient1,\
				const double weight1, const string& message1):SendItem(name1,type1,sender1,recipient1,weight1)
{
	message = message1;
}

string Letter::GetMessage()
{
	return message;
}



Package::Package(const string& name1, const string& type1, const string& sender1, const string& recipient1,\
				  const double weight1, const double volume1) :SendItem(name1, type1, sender1, recipient1, weight1)
{
	volume = volume1;
}

double Package::GetVolume()
{
	return volume;
}

Combined::Combined(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1,\
					 const string& message1, const double volume1) :Letter(name1, type1, sender1, recipient1, weight1,message1)
{
	volume = volume1;

}
