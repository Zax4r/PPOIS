#include "Letter.h"

Letter::Letter(const string& name1, const string& type1, const string& sender1, const string& recipient1, \
	const double weight1, const string& message1) :SendItem(name1, type1, sender1, recipient1, weight1)
{
	message = message1;
}

string Letter::GetMessage()
{
	return message;
}
