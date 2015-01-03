//#include <regex>//supported in gcc 4.8.2+ 
#include <cctype>//isspace, isalpha, isalnum, isdigit 
#include <algorithm>//find

#include "lexer.h"//nature

Lexer::Lexer(const char* src)
{
	src_.open(src);
}

Lexer::~Lexer()
{
	src_.close();

	clear(tokens_);
}

void Lexer::Exec()
{
	cout << "lexer started" << endl;

	if (src_.good())//这里判断条件如何是好
	{
		for (current_char_ = src_.get(); current_char_ != -1; current_char_ = src_.get())
		{
			while(isspace(current_char_))//handle white space characters
			{
				current_char_ = src_.get();		
			}

			switch(current_char_)
			{
				//separators

				case '(' : tokens_.push(Token(LPAREN, "(")); break;
				case ')' : tokens_.push(Token(RPAREN, ")")); break;
				case '{' : tokens_.push(Token(LBRACE, "{")); break;
				case '}' : tokens_.push(Token(RBARCE, "}")); break;
				case '[' : tokens_.push(Token(LBRACKET, "[")); break;
				case ']' : tokens_.push(Token(RBRACKET, "]")); break;

				case ',' : tokens_.push(Token(COMMA, ",")); break;
				case ';' : tokens_.push(Token(SEMICOLON, ";")); break;

				//operators

				case '~' : tokens_.push(Token(BITWISE_NEGATION, "~")); break;
				case '^' : tokens_.push(Token(BITWISE_XOR, "^")); break;

				case '!' : tokens_.push(Token(NOT, "!")); break;

				case '&' : 

					current_char_ = src_.peek();//prefetch

					if ('&' == current_char_)
					{
						src_.get();//实取

						tokens_.push(Token(AND, "&&"));
					}
					else
					{
						tokens_.push(Token(BITWISE_AND, "&"));
					}

				break;

				case '|' : 

					current_char_ = src_.peek();

					if ('|' == current_char_)
					{
						src_.get();

						tokens_.push(Token(OR, "||"));
					}
					else
					{
						tokens_.push(Token(BITWISE_OR, "|"));
					}

				break;

				case '+' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '+' : src_.get(); tokens_.push(Token(INCRE, "++")); break;//INCRE

						case '=' : src_.get(); tokens_.push(Token(ADDEQ, "+=")); break;//ADDEQ

						default  : tokens_.push(Token(ADD, "+")); break;
					}

				break;

				case '-' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '-' : src_.get(); tokens_.push(Token(DECRE, "--")); break;//DECRE

						case '=' : src_.get(); tokens_.push(Token(MINEQ, "-=")); break;//MINEQ
						
						default  : tokens_.push(Token(MIN, "-")); break;
					}

				break;

				case '*' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '/' : src_.get(); tokens_.push(Token(MULTIPLE_LINE_COMMENT_END, "*/")); break;

						case '=' : src_.get(); tokens_.push(Token(MULEQ, "*=")); break;//MULEQ

						default  : tokens_.push(Token(MUL, "*")); break;
					}

				break;

				case '/' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '/' : src_.get(); tokens_.push(Token(SINGLE_LINE_COMMENT, "//")); break;

						case '*' : src_.get(); tokens_.push(Token(MULTIPLE_LINE_COMMENT_BEGIN, "/*")); break;

						case '=' : src_.get(); tokens_.push(Token(DIVEQ, "/=")); break;//DIVEQ
						
						default  : tokens_.push(Token(DIV, "/")); break;
					}

				break;

				case '%' : 

					current_char_ = src_.peek();

					if ('=' == current_char_)
					{
						src_.get();

						tokens_.push(Token(MODEQ, "%="));//MODEQ
					}
					else
					{
						tokens_.push(Token(MOD, "%"));
					}

				break;	

				case '=' : 

					current_char_ = src_.peek();

					if ('=' == current_char_)
					{
						src_.get();

						tokens_.push(Token(EQ, "=="));
					}
					else
					{
						tokens_.push(Token(ASSIGN, "="));
					}

				break;

				case '>' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '>' : src_.get(); tokens_.push(Token(RIGHT_SHIFT, ">>")); break;

						case '=' : src_.get(); tokens_.push(Token(GE, ">=")); break;
						
						default  : tokens_.push(Token(GT, ">")); break;
					}

				break;

				case '<' : 

					current_char_ = src_.peek();

					switch(current_char_)
					{
						case '<' : src_.get(); tokens_.push(Token(LEFT_SHIFT, "<<")); break;

						case '>' : src_.get(); tokens_.push(Token(NE, "<>")); break;

						case '=' : src_.get(); tokens_.push(Token(LE, "<=")); break;
						
						default  : tokens_.push(Token(LT, "<")); break;
					}

				break;	

				default : 

					if (isalpha(current_char_) || current_char_ == '_')
					{
						do
						{
							token_.push_back(current_char_);

							current_char_ = src_.get();
						} 
						while (isalnum(current_char_) || current_char_ == '_');//拼词

						src_.unget();

						if (g_keywords.find(token_) != g_keywords.end())//match keywords
						{
							tokens_.push(Token(g_keywords[token_], token_));

							token_.clear();
						}
						else
						{
							// if (token_.front() == '_' || token_.back() == '_')//check the validity of identifier
							// {
							// 	tokens_.push(Token(UNDEFINED, token_));

							// 	token_.clear();		
							// }
							// else
							// {
							// 	tokens_.push(Token(IDENTIFIER, token_));

							// 	token_.clear();
							// }
						}
					}
					else if (isdigit(current_char_))
					{
						do
						{
							token_.push_back(current_char_);

							current_char_ = src_.get();
						} 
						while (isdigit(current_char_) || current_char_ == '.');//拼数

						src_.unget();

						// regex integer("^[1-9]\\d*|0$");
						// regex doubler("^[1-9]\\d*\\.\\d+|0\\.\\d*[1-9]\\d*|0?\\.0+|0$");

						// if (regex_match(token_, integer))
						// {
						// 	tokens_.push(Token(INTEGER, token_));

						// 	token_.clear();
						// }
						// else if (regex_match(token_, doubler))
						// {
						// 	tokens_.push(Token(DOUBLER, token_));

						// 	token_.clear();
						// }
						// else
						// {
						// 	tokens_.push(Token(UNDEFINED, token_));

						// 	token_.clear();
						// }
					}

				break;		
			}
		}

		tokens_.push(Token(END_OF_FILE, "EOF"));

		cout << "lexer finished" << endl;
	}
	else
	{
		cout << "文件打开失败或者存在错误" << endl;

		//throw "文件打开失败或者存在错误";
	}
}

void Lexer::Print()//这个函数效率低下
{
	cout << "print tokens" << endl;

	queue<Token> tmp = tokens_;

	int size = tmp.size();

	for (int i = 0; i < size; ++i)
	{
		cout << tmp.front().ToString() << endl;

		tmp.pop();
	}
}