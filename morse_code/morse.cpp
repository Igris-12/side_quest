#include <iostream>
#include<sstream>
#include<unordered_map>
#include<string>
using namespace std;
int i=0,j=0,k=0;
class MORSE
{
		unordered_map<string,char> Dmorse_Vocab=
		{
			{".-",'A'},
			{"-...",'B'},
			{"-.-.",'C'},
			{"-..",'D'},
			{".",'E'},
			{"..-.",'F'},
			{"--.",'G'},
			{"....",'H'},
			{"..",'I'},
			{".---",'J'},
			{"-.-",'K'},
			{".-..",'L'},
			{"--",'M'},
			{"-.",'N'},
			{"---",'O'},
			{".--.",'P'},
			{"--.-",'Q'},
			{".-.",'R'},
			{"...",'S'},
			{"-",'T'},
			{"..-",'U'},
			{"...-",'V'},
			{".--",'W'},
			{"-..-",'X'},
			{"-.--",'Y'},
			{"--..",'Z'},
		};
        
		unordered_map<char,string> Emorse_Vocab;
		public:
            MORSE()
            {
                for( auto pair : Dmorse_Vocab )
			            Emorse_Vocab[pair.second]=pair.first;
            }
			void Decode();
			void Encode();
};
void MORSE::Decode()
 {
    string MC,M;
    cout << endl << "Enter the MORSE to be decoded:";
    cin.ignore(); 
    getline(cin, MC);
    cout<<"In English: ";
    
    for ( i = 0; MC[i]!='\0'; i++) 
    {
        if(MC[i]==' ')
            cout<<" ";
        else     
        {
            if (MC[i] != '/') 
                M += MC[i];
        
            else 
            {
                cout << Dmorse_Vocab[M];
                M.clear(); 
            }
        }
    }
    cout << Dmorse_Vocab[M]<<'.';
}

    
    
    

void MORSE :: Encode()
{
	string EN;
	cout<<endl<<"Enter the Sentence: ";
    cin.ignore();
	getline(cin,EN);
	cout<<endl<<"The Morse Code:";
	for(i=0;EN[i]!='\0';i++)
	{
		if(EN[i]==' ')
			cout<<" ";
		else
			cout<<Emorse_Vocab[EN[i]]<<"/";
	}
	cout<<"*";
}


int main()
{
	int ch;
    MORSE m;
	do
	{
		cout<<endl<<"1]Morse Code to English\n2]English to Morse Code\n3]Quit";
        cout<<endl<<"Enter Your Choice:";
		cin>>ch;
		switch(ch)
		{
			case 1: m.Decode();break;
		
			case 2: m.Encode();break;
		
			case 3: break;
		
			default:cout<<"\n Incorrect Option";
		}
	}while(ch!=3);
}		
