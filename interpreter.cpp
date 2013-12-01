#include "interpreter.h"

Interpreter::Interpreter(const char* src)
{
	parser_ = new Parser(src);
}

Interpreter::~Interpreter()
{
	delete parser_;
}

void Interpreter::Exec()
{
	parser_ -> Exec();

	parser_ -> Print();

	cout << "interpreter started" << endl;

	//...

	cout << "interpreter finished" << endl;
}

void Interpreter::Print()
{
	cout << "print something in interpreter..." << endl;
}