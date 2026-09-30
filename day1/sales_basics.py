n=int(input())
a=[input() for i in range(n)]
d=dict()
total_sales_all=[]
overall_sales=0
for i in a:
  d[i]={'product_name':i,'price':int(input(f"enter {i} price:")),'quantity_sold':int(input("quan sold"))}
  total_sales=d[i]['price']*d[i]['quantity_sold']
  print(f"----total_sales for {d[i]} is:",total_sales)
  print("",end="\n")
  d[i]['total_sales']=total_sales
  total_sales_all.append(total_sales)
  overall_sales+=total_sales
print(d)
print('overall_saels',overall_sales)
print('average sales',overall_sales/n)
max=max(total_sales_all)
min=min(total_sales_all)
print("max sa")
for i in d:
  if d[i]['total_sales']==max:
    print(i)
for i in d:
  if d[i]['total_sales']==min:
    print(i) 

