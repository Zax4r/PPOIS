#pragma once
#include <string>
#include <vector>
using namespace std;
class Item
{
protected:
	int id;
	string name;
public:
	Item(int& id,string& name);
	string getName();
	int getId();
};

