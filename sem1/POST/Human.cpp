#include "Human.h"

Human::Human(std::string name, int age) :name(name), age(age)
{

}

string Human::GetName()
{
	return name;
}
