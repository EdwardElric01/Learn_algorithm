#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const int LEFT_UP = 0;
const int LEFT = 1;
const int UP = 2; 

void LCS_LENGTH(int **b, int **c, string X, string Y);
void PRINT_LCS(int **b, string X, int m, int n);

int main()
{
    string X = "belong", Y = "cnblogs";
    int m = X.length();
    int n = Y.length();
    int i, j;

    int **b = new int*[m], **c = new int*[m+1];

    // initialize b, c
    for (i=0; i<m; i++)
        b[i] = new int[n];
    for (j=0; j<=m; j++)
        c[j] = new int[n+1];

    LCS_LENGTH(b, c, X, Y);
    PRINT_LCS(b, X, m, n);
    cout << endl;

    // delete b, c
    for (i=0; i<m; i++)
        delete [] b[i];
    for (j=0; j<=m; j++)
        delete [] c[j];
}

void LCS_LENGTH(int **b, int **c, string X, string Y)
{
    using namespace std;
    int i,j;
    int m = X.length();
    int n = Y.length();

    for (i=0; i<=m; i++)
        c[i][0] = 0;
    for (j=0; j<=n; j++)
        c[0][j] = 0;

    for (i=1; i<=m; i++)
    {
        for (j=1; j<=n; j++)
        {
            if (X[i-1] == Y[j-1])
            {
                c[i][j] = c[i-1][j-1] + 1;
                b[i-1][j-1] =  LEFT_UP;
            } 
            else if(c[i-1][j] >= c[i][j-1]) 
            {
                c[i][j] = c[i-1][j];
                b[i-1][j-1] = UP;
            } else 
            {
                c[i][j] = c[i][j-1];
                b[i-1][j-1] = LEFT;
            }
        }
    }

    // print c
    //for (i=0; i<=m; i++)
    //{
        //for (j=0; j<=n; j++)
        //{
           //cout << setw(5) << c[i][j] ;
        //}
        //cout << endl;
    //}
        
    // print b
    //for (i=0; i<m; i++)
    //{
        //for (j=0; j<n; j++)
        //{
           //cout << setw(5) << b[i][j] ;
        //}
        //cout << endl;
    //}
}

void PRINT_LCS(int **b, string X, int m, int n)
{
    if (m==0 || n==0)
    {
        return;
    }
    else
    {
        if (b[m-1][n-1]==LEFT_UP)
        {
            PRINT_LCS(b, X, m-1, n-1);
            cout << X[m-1] << " ";
        }
        else
        {
            if (b[m-1][n-1] == UP)
            {
                PRINT_LCS(b, X, m-1, n);
            }
            else 
            {
                PRINT_LCS(b, X, m, n-1);
            }

        }
    }
}
