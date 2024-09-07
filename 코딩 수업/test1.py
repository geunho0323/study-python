# # 1
# a=input()
# b=""
# # for i in range(len(a)):
# #     b+=a[len(a)-1-i]
# #     print(b)
# print(a[0:2:1])
# if a==b:
#     print(True)
# else:
#     print(False)

#2
# a=[1,3,2,1,5,1,3,3,2,1]
# count={}
# for i in range(len(a)-1):
#     if a[i] not in count:
#         count[a[i]]=1
#     else:
#         count[a[i]]+=1

#     print(count)   
#3
# a=[4,7,2,9,5]
# max=0
# min=999999999999999999999999
# print(max(a),min(a))
# for i in range(len(a)):
#     if a[i]>max:
#         max=a[i]
#     elif a[i]<max:
#         continue
#     else:
#         continue
# for i in range(len(a)):
#     if a[i]>min:
#         continue
#     elif a[i]<min:
#         min=a[i]
#     else:
#         continue
# print(max)
# print(min)
# for i in range(1,11):
#     if i%2==1:
#         print(i)
#     else:
#         pass
# a=[1,2,3,4,5]
# for i in range(len(a)):
#     print(a[i])
# a=[10,25,5,75,50]
# Max=0
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         Max=a[i]
#     elif a[i]<a[i+1]:
#         Max=a[i+1]
#     else:
#         Max=a[i]
# print(Max)
# a=int(input())
# for i in range(a+1):
#     b=" "
#     print(b*(a-i)+"*"*i)
a=["apple","banana","apple","cherry","banana","apple"]
b={}
for i in range(len(a)):
    if a[i] in b:
        b[a[i]]+=1
    else:
        b[a[i]]=1
    print(b)
print(b)