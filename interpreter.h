#ifndef INTERPRETER_H
#define INTERPRETER_H

#include "parser.h"//explicit for Parser

class Interpreter
{
public:
	Interpreter(const char*);
	~Interpreter();

	void Exec();
	void Print();
private:
	Parser* parser_;
};

#endif // INTERPRETER_H 

		