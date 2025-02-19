#include <gtest/gtest.h>
#include "PostOffice.h"
#include<sstream>

TEST(LetterTest, GetterMessage) {
    Letter letter("1", "2", "3", "4", 1, "5");
    EXPECT_EQ(letter.GetMessage(), "5");
}