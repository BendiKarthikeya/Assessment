/*Given three numbers a, b and m. Calculate (ab % m)
Example input :
2 5 3
Example output :
2
Explanation :
25 % 3 = 32 % 3 = 2*/
 
  #include<stdio.h>
  #include<math.h>
  int main(){
    int a,b,m;
    scanf("%d %d %d",&a,&b,&m);
    int x=power(a,b)%m;
    printf("%d",x);
  }
  int power(int a,int b){
    if(b==0){
      return 1;
    }
    return a*power(a,b-1);
  }

