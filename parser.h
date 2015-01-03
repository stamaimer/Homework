#ifndef PARSER_H
#define PARSER_H

#include "lexer.h"//explicit for Lexer

class Parser
{
public:
	Parser(const char*);
	~Parser();

	void Exec();
	void Print();
private:
	Lexer* lexer_;
	queue<Token> tokens_;
};

#endif // PARSER_H 

		