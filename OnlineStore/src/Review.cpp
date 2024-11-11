#include "Review.h"

Review::Review(string& message, Client& author):message(message),author(author)
{
}

string Review::getMessage(){
    return message;
}