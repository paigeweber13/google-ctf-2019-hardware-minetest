#include <iostream>
#include <sqlite3.h> 

using namespace std;

int main(int argc, char* argv[]) {
   sqlite3 *db;
   char *zErrMsg = 0;
   int rc;

   rc = sqlite3_open("google-ctf-2019-hardware-minetest-map/map.sqlite", &db);

   if( rc ) {
      cerr << "Can't open database: " << sqlite3_errmsg(db) << endl;
      return(0);
   } else {
      cerr << "opened database successfully!" << endl;
   }
   sqlite3_close(db);
}
