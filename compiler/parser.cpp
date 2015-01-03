#include "parser.h"

Parser::Parser(const char* src)
{
	lexer_ = new Lexer(src);
}

Parser::~Parser()
{
	delete lexer_;
}

void Parser::Exec()
{
	lexer_ -> Exec();

	lexer_ -> Print();

	cout << "parser started" << endl;

	//...

	cout << "parser finished" << endl;
}

void Parser::Print()
{
	cout << "print something in parser..." << endl;
}