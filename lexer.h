#ifndef LEXER_H
#define LEXER_H

#include <iostream>

#include "token.h"//explicit for Token
				  //implicit include global.h for std namespace, string, queue
				  
class Lexer
{
public:
	Lexer(const char*);
	~Lexer();

	void Exec();
	void Print();
private:
	ifstream src_;
	char current_char_;
	string token_;
	queue<Token> tokens_;
};

#endif // LEXER_H 

		