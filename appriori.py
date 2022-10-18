data = []

attr1 = "Transaction ID"
attr2 = "List of items"

n = int(input("Enter the number of data points : "))

items = []
for i in range(n):
	at1 = input("Enter the transaction ID : ")
	at2 = list(map(str, input("Enter the list of items associated with the input transaction ID : ").split(" ")))
	data.append([at1] + at2)
	for j in at2 :
		if [j] not in items :  
			items.append([j])
	

min_sup = int(input("Enter the minimum support threshold value : "))
for 

		


		
		



	 
			
	
	