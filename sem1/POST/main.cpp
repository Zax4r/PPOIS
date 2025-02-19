#include "PostOfficeTest.h"
#include "SendItemTest.h"
#include "PostWorkerTest.h"
#include "ClientTest.h"
#include "CombinedTest.h"
#include "LetterTest.h"
#include "PackageTest.h"

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  
  return RUN_ALL_TESTS();
}
