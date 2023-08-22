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


#3

#include <stdio.h>

int main() {
	int t;
	printf("enter the no. of test cases : ");
	scanf("%d",&t);
	for(int a=0;a<t;a++){
	
	
    int N;
    printf("Enter a number: ");
    scanf("%d", &N);
    int largest_prime_factor(int num);
    int result = largest_prime_factor(N);
    
    if (result == -1) {
        printf("The number %d doesn't have any prime factors.\n", N);
    } else {
        printf("The largest prime factor of %d is %d.\n", N, result);
    }
}
    return 0;
}


int is_prime(int num) {
    if (num <= 1) {
        return 0;
    }
    
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    
    return 1;
}

int largest_prime_factor(int num) {
    int largest = -1;

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0 && is_prime(i)) {
            largest = i;
        }

        // Remove all occurrences of i from num
        while (num % i == 0) {
            num=num/i;
        }
    }

    if (num > 1 && is_prime(num)) {
        largest = num;
    }

    return largest;
}


#4

#include <stdio.h>

int main() {
	int t;
	printf("enter the no. of test cases : ");
	scanf("%d",&t);
	for(int a=0;a<t;a++){
	
	
    int N;
    printf("Enter a value of N: ");
    scanf("%d", &N);
    int largest_palindrome(int num);
    int result = largest_palindrome(N);

    if (result == -1) {
        printf("No palindrome found.\n");
    } else {
        printf("The largest palindrome less than %d is %d.\n", N, result);
    }
}
    return 0;
    
    
}


int is_palindrome(int num) {
    int original = num;
    int reverse = 0;

    while (num > 0) {
        int digit = num % 10;
        reverse = reverse * 10 + digit;
        num=num/10;
    }

    return original == reverse;
}

int largest_palindrome(int N) {
    int largest = -1;

    for (int i = 999; i >= 100; i--) {
        for (int j = 999; j >= 100; j--) {
            int product = i * j;
            if (product < N && is_palindrome(product)) {
                if (product > largest) {
                    largest = product;
                }
            }
        }
    }

    return largest;
}


	
