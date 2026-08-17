import torch
a = torch.tensor([1,2,3,4])#이런 식으로 벡터 생성
print(a.dtype)# data type
print(a.shape)#크기를 알려줌
b = torch.tensor([1,2,3.1,4])
print(b.dtype)#하나라도 실수면 다 실수 타입

A = torch.tensor([[1,2,3],[4,5,6]])
#A = torch.tensor([[1,2],[3,4,5]]) 벡터와 달리 행렬이라서 각 항에 해당하는 숫자의 갯수가 같아야함
print(A.shape)
print(A.ndim)#차원의 수
print(A.numel())#전체 원소의 수

print(torch.zeros(5))#0으로 꽉찬 ([5]) shape의 벡터 생성
print(torch.zeros(5,2))#0으로 꽉찬 ([5,2]) shape의 행렬 생성
print(torch.zeros_like(A))#A와 같은 shape의 0으로 채워진 행렬 생성
print(torch.ones(5))#1로 꽉찬 ([5]) shape의 벡터 생성
print(torch.arange(3,10,2))#range와 비슷하게 작동 3부터 시작하여서 10 전까지 2의 간격으로 벡터 생성
print(torch.arange(0,1,0.1))#소숫점도 가능 range에서는 안됨
print(torch.linspace(0,1,10))#0에서부터 1포함하여서 10개 생성

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])
c = a+b
print(c)#5,7,9 출력 

A = torch.tensor([[1,2,3],[1,2,3]])
B = torch.tensor([[4,5,6],[1,1,1]])
C = A+B
D = A-B
print(C)
print(D)
print(A*B)#진짜 행렬 곱과느 다른 얘 (Hadamard product)라고 불림
print(A/B)
print(B**2)
#사칙연산은 다 같은 방식으로 수행

A = torch.tensor([[1,2],[3,4]])
B = torch.tensor([[1,2],[3,4]])
print(A*B)
print(A@B)#이게 진짜 행렬 곱
