
#include<iostream> 
#include<fstream>
#include<iomanip>  
using namespace std;  
const int SIZE=50;  
const int MAXINT=999;  
int main(){  
      
while(1){  
int N,a[SIZE],b[SIZE],SumA[SIZE],SumB[SIZE];  
int tempSumA,tempSumB,MinSum;  
int i=0,j,k;  
tempSumA=tempSumB=0;
int data;
int oriData[SIZE]; 
//记录A，B完成当前任务所需时间  
//Read input.txt
 ifstream ifile;
    ifile.open("input.txt");  
 if(ifile.eof()) 
    {
        cerr<<"Fail to open the file input.txt"<<endl;
        return 1;
    }
while(ifile>>data)
    {
  oriData[i++]=data;    //Recording data
    }
 
 N=(int)oriData[0];    //the number of task
// i=0;
 for (i=1;i<=N;i++)
 {
  a[i]=oriData[i];
  tempSumA+=a[i];  
  SumA[i]=tempSumA;
 }
 for (i=1,j=N+1;j<=2*N;j++,i++)
 {
  b[i]=oriData[j];
  tempSumB+=b[i];  
  SumB[i]=tempSumB;
 }
 
 //Show data of input.txt and data will process.
 cout<<"Input.txt Data:"<<endl;
 cout<<oriData[0]<<endl;
 for (i=1;i<=2*N; )
 {
  cout<<oriData[i]<<" ";
  i++;
  cout<<oriData[i]<<endl;
  i++;  
 }
/* cout<<"Data will process:"<<endl;
 for (i=0;i<cnt;i++)
 {
  cout<<proData[i]<<" ";
 }*/
 cout<<endl;
    ifile.close();
/*cin>>N;  
if(N<=0)break;  
int tempSumA,tempSumB,MinSum;  
int i,j,k;  
tempSumA=tempSumB=0;  
for(i=1;i<=N;i++){  
cin>>a[i];  
tempSumA+=a[i];  
SumA[i]=tempSumA;  
}  
for(i=1;i<=N;i++){  
cin>>b[i];  
tempSumB+=b[i];  
SumB[i]=tempSumB;  
}  */
MinSum=(tempSumB>tempSumA)?tempSumA:tempSumB;  
//时间上限AB总和的最小值  
///动态二维数组   
int *MaxTime=new int [MinSum+1];  
int **F=new int*[N+1];  
for(i=0;i<N+1;i++)  
F[i]=new int [MinSum+1];  
SumB[0]=0;  
for(i=0;i<=N;i++){  
F[i][0]=SumB[i];//SumB[0]没赋值，调试时会输出地址   
for(j=1;j<=MinSum;j++)  
F[i][j]=0;  
}  
/*for(i=0;i<=N;i++){ 
for(j=0;j<=MinSum;j++) 
cout<<setw(2)<<F[i][j]<<" "; 
cout<<endl; 
} 
cout<<endl;*/  
int temp;  
for(k=1;k<=N;k++){  
   temp=(SumA[k]>SumB[k])?SumB[k]:SumA[k];  
   for(i=1;i<=temp;i++){ //A最多用AB前k任务的最小值，如果B最少就全用B做。  
      if(i>=a[k])//等于号不能少   
    F[k][i]=(F[k-1][i]+b[k]<F[k-1][i-a[k]])?F[k-1][i]+b[k]:F[k-1][i-a[k]];  
      else F[k][i]=F[k-1][i]+b[k];  
                        }   
                  }  
                    
/*for(i=0;i<=N;i++){ 
for(j=0;j<=MinSum;j++) 
cout<<setw(2)<<F[i][j]<<" "; 
cout<<endl; 
                  } 
cout<<endl;      */  
        
temp=MAXINT;  
for(i=0;i<=MinSum;i++){  
 MaxTime[i]=(i>F[N][i])?i:F[N][i];  
if(temp>MaxTime[i])  
temp=MaxTime[i];  
                       }  
//cout<<temp<<endl;
 
//out.txt
ofstream ofile;  //write file
 ofile.open("output.txt");
/* int result=0;
 for(int i=0;i<c;i++)
 {
  result+=abs(Data[i]-m);
 }*/
 ofile<<temp<<endl;
ofile.close();
cout<<"最优时间为："<<temp<<endl;
while(1);
///////////////////////////////////  
/*for(i=0;i<N+1;i++)  
delete [] F[i];  
delete [] F;  
delete [] MaxTime;  
F=NULL;   */
}  
////////////////////////////////  
//system("pause");  
//return 0;      
}
