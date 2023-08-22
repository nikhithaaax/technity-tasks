#1

#include<stdio.h>


int main(){

	int t;
    int ans;
    int sum;
	printf("enter the no. of test cases : ");
	scanf("%d",&t);
	for(int a=0;a<t;a++){
		int n;
		printf("enter upto what natural numbers : ");
		scanf("%d",&n);
		
	

		int sum3=0,sum5=0,sumcommon=0;
		for(int i=0;i<n;i++){
			if(i%3==0){
				sum3=sum3+i;
			}
			if(i%5==0){
				sum5=sum5+i;
			}
			if(i%3==0&&i%5==0){
				sumcommon=sumcommon+i;
			}
ans=sum3+sum5-sumcommon;
	}
	printf("%d\n",ans);
}
return 0;

}


#2
  
#include <stdio.h>

int main() {
	int t;
	printf("enter the no. of test cases : ");
	scanf("%d",&t);
	for(int a=0;a<t;a++){
		
	
    int N;
    printf("Enter the value of N: ");
    scanf("%d", &N);

    int a1 = 1; 
    int a2 = 2; 
    int sum = 0; 
    
    while (a2 <= N) {
        if (a2 % 2 == 0) {
            sum += a2;
        }
        
        
        int next = a1 + a2;
        a1 = a2;
        a2 = next;
    }
    
    printf("Sum of even-valued Fibonacci terms not exceeding %d is: %d\n", N, sum);
}
    return 0;
}
