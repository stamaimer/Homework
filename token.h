#ifndef TOKEN_H
#define TOKEN_H

#include "global.h"

class Token
{
public:
	Token (TokenType token_type, TokenValue token_value)
	{
		token_type_ = token_type;
		token_value_ = token_value;
	}

	~Token (){}

	TokenType get_token_type ()
	{
		return token_type_; 
	}

	TokenValue get_token_value ()
	{
		return token_value_; 
	}

	void set_token_type (TokenType token_type)
	{
		token_type_ = token_type; 	
	} 

	void set_token_value (TokenValue token_value)
	{
		token_value_ = token_value; 	
	}

	string ToString ()
	{
		return g_token_type_literal[token_type_] + "                    " + token_value_;
	}
			
private:
	TokenType token_type_;
	TokenValue token_value_;
};

#endif // TOKEN_H 

		