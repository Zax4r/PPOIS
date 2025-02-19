#include "Store.h"

Store::Store(string& name): name(name)
{
}

string Store::getName()
{
    return name;
}