#include<iostream>
#include<string>
using namespace std;
//Bool fun
//test function
bool checkUnique(string str)
{
	for (int i=0; i<str.length();i++)
	{
		for (int j=i+1;j<str.length();j++)
		{
			if (str[i]==str[j])
			{
			return false;
			}
		}
	}
return true;
}

int main()
{
string test="This";
	if (checkUnique(test))
	{cout<<"Unique string"<<endl;
	}else{
	cout<<"Not Unique"<<endl;
	}

return 0;
}
