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
