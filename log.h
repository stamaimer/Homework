#ifndef LOG_H
#define LOG_H

#include <string>
#include <fstream>

using namespace std;

class Log
{
    public:

        static void E(string error)
        {
        	error_.open("../log/error.log", ofstream::app);

        	error_ << error << endl;

        	error_.close();
        }

    private:

        static ofstream error_;
};

#endif // LOG_H 		