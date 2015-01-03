#include "lexer.cpp"
#include "parser.cpp"
#include "interpreter.cpp"
		
int main(int argc, char* argv[])//portable
{
	if (2 != argc)
	{
		cout << "于此书写使用说明" << endl;

		exit(1);
	}
		
	Interpreter interpreter(argv[1]);

	interpreter.Exec();

	interpreter.Print();
	
	//system("pause");

	return 0;
}