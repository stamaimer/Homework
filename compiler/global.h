#ifndef GLOBAL_H
#define GLOBAL_H

#include <map>//keywords
#include <queue>//clear
#include <string>//typedef
#include <fstream>//fstream

//#include "token.h"//use forward declaration instead of include

class Token;//forward declaration(incomplete declaration)

using namespace std;//string

typedef string TokenValue;//only for tidy with TokenType

enum TokenType 
{
	UNDEFINED,//未定义

	IDENTIFIER,//标识符

	INTEGER,//整数
	DOUBLER,//实数

	END_OF_FILE,//文件尾

	INT,//整型
	REAL,//实型
	BOOL,//布尔型
	TRUE,//真
	FALSE,//假
	IF,//if
	ELSE,//else
	WHILE,//while
	READ,//read
	WRITE,//write

	LPAREN,//(
	RPAREN,//)
	LBRACE,//{
	RBARCE,//}
	LBRACKET,//[
	RBRACKET,//]

	COMMA,//,
	SEMICOLON,//;

	BITWISE_NEGATION,//~
	BITWISE_XOR,//^
	BITWISE_AND,//&
	BITWISE_OR,//|

	RIGHT_SHIFT,//>>
	LEFT_SHIFT,//<<

	AND,//&&
	OR,//||
	NOT,//!

	ADD,//+
	MIN,//-
	MUL,//*
	DIV,///
	MOD,//%

	INCRE,//++
	DECRE,//--

	ADDEQ,//+=
	MINEQ,//-=
	MULEQ,//*=
	DIVEQ,///=
	MODEQ,//%=

	ASSIGN,//=

	GT,//>
	LT,//<
	EQ,//==
	GE,//>=
	LE,//<=
	NE,//<>

	SINGLE_LINE_COMMENT,////
	MULTIPLE_LINE_COMMENT_BEGIN,///*
	MULTIPLE_LINE_COMMENT_END//*/
};//54

string g_token_type_literal[] = 
{
	"UNDEFINED",

	"IDENTIFIER",

	"INTEGER",
	"DOUBLER",

	"END_OF_FILE",

	"INT",
	"REAL",
	"BOOL",
	"TRUE",
	"FALSE",
	"IF",
	"ELSE",
	"WHILE",
	"READ",
	"WRITE",

	"LPAREN",
	"RPAREN",
	"LBRACE",
	"RBARCE",
	"LBRACKET",
	"RBRACKET",

	"COMMA",
	"SEMICOLON",

	"BITWISE_NEGATION",
	"BITWISE_XOR",
	"BITWISE_AND",
	"BITWISE_OR",

	"RIGHT_SHIFT",
	"LEFT_SHIFT",

	"AND",
	"OR",
	"NOT",

	"ADD",
	"MIN",
	"MUL",
	"DIV",
	"MOD",

	"INCRE",
	"DECRE",
	"ADDEQ",
	"MINEQ",
	"MULEQ",
	"DIVEQ",
	"MODEQ",

	"ASSIGN",

	"GT",
	"LT",
	"EQ",
	"GE",
	"LE",
	"NE",

	"SINGLE_LINE_COMMENT",
	"MULTIPLE_LINE_COMMENT_BEGIN",
	"MULTIPLE_LINE_COMMENT_END"
};

std::map<string, TokenType> g_keywords;

void init()
{
	g_keywords["int"] = INT;
	g_keywords["real"] = REAL;	
	g_keywords["bool"] = BOOL;
	g_keywords["true"] = TRUE;
	g_keywords["false"] = FALSE;
	g_keywords["if"] = IF;
	g_keywords["else"] = ELSE;
	g_keywords["while"] = WHILE;
	g_keywords["read"] = READ;
	g_keywords["write"] = WRITE;	
}

//a efficiently way to clear a std::queue

inline void clear(queue<Token> tokens)
{
	queue<Token> empty;

	swap(tokens, empty);
}

enum GrammerTreeNodeType {TERMINAL, NONTERMINAL};

enum NonTerminalType {  };

#endif // GLOBAL_H 

		