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

print(torch.zeros(5))#0으로 꽉찬 5차원 벡터 생성
print(torch.zeros(5,2))
