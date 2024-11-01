#include "Combined.h"

Combined::Combined(const string& name1, const string& type1, const string& sender1, const string& recipient1, const double weight1, \
	const string& message1, const double volume1) :Letter(name1, type1, sender1, recipient1, weight1, message1)
{
	volume = volume1;

}
