List=list()
Data=list()
Team=0

#班級同學的朋友編號
def InData():
	InputData=input()
	global Data
	Data=InputData.split()
#建立'未查詢的表單'
def InList():
	global List
	InputList=int(input())
	List=[False for i in range(InputList)]
#指標，會自動忽略已經測試過的團體，傳回下個要測試的團體
def Pointer():
	global List
	for i in range(len(List)):
		if List[i]==False:
			return i
			break
#會找出每個人的朋友之間的聯繫，如果形成一個小團體時Team加1
def Finder(ptr):
	global Data
	global List
	global Team
	Head=ptr*1
	Next=0
	while True:
		Next=int(Data[ptr])
		List[ptr]=True
		ptr=Next
		if ptr==Head:
			Team=Team+1
			break

#輸入人數，建立＂未查詢表單＂
InList()
#輸入每個人的朋友資料
InData()
#迴圈,在指標回傳None值前,持續運作pointer跟finder
while True:
	if Pointer()==None:
		print(Team)
		break
	else:
		Finder(Pointer())






