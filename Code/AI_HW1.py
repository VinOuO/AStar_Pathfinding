#-------------------------前置                                                                 #---Node(self, _x, _y, _Can_Pass, _Weight, _Pre)   W for 地圖寬度 H for 地圖高度  Map for 以Node形成的2D array 
from pathlib import Path                                                                       #---Start for Start Node  End for End Node Now for The current Node
from Node import Node
import sys
import math

f = open(r"test1.txt", encoding = 'utf8')
File_String = f.read()
#print(File_String.split())
W = int(File_String.split()[0])
H = int(File_String.split()[1])

Map = [[Node(0, 0, 0, 0, None, -1) for i in range(W)] for j in range(H)]
	
for i in range(H):
	for j in range(W):
		Map[i][j].__init__(j, i, int(File_String.split()[i + 2][j]), math.inf, None, -1)
'''
for i in range(H):
	for j in range(W):
		if j != W - 1:
			print(Map[i][j].Can_Pass(), end ="|")
		else:
			print(Map[i][j].Can_Pass())
'''
txt = input("Enter the Start and End: \n")
try:
	Start = Map[int(txt.split()[1])][int(txt.split()[0])]
	End = Map[int(txt.split()[3])][int(txt.split()[2])]
except:
	print("Error! Please be sure that you fallowed the input format: Start.x Start.y End.x End.y  and that your input was not out of boundary. ")
	sys.exit()
#----------------------------防呆
if Start.Get_Can_Pass() == 1:
	print("Error! Start point is an obstacle!")
	sys.exit()
if End.Get_Can_Pass() == 1:
	print("Error! End point is an obstacle!")
	sys.exit()
#----------------------------防呆
print("\n")	
#-------------------------前置

def Weight_around(_Node):
	if _Node.Pos()[1] < H - 1:
		Map[_Node.Pos()[1] + 1][_Node.Pos()[0]].Set_Weight(_Node.Get_Cost(), _Node, End)
	if _Node.Pos()[1] > 0:
		Map[_Node.Pos()[1] - 1][_Node.Pos()[0]].Set_Weight(_Node.Get_Cost(), _Node, End)
	if _Node.Pos()[0] < W - 1:
		Map[_Node.Pos()[1]][_Node.Pos()[0] + 1].Set_Weight(_Node.Get_Cost(), _Node, End)
	if _Node.Pos()[0] > 0:
		Map[_Node.Pos()[1]][_Node.Pos()[0] - 1].Set_Weight(_Node.Get_Cost(), _Node, End)
			
'''
def Print_Weight_around(_Node):
	print(Map[_Node.Pos()[1] + 1][_Node.Pos()[0]].Get_Weight(), end =" ")
	print(Map[_Node.Pos()[1] - 1][_Node.Pos()[0]].Get_Weight(), end =" ")
	print(Map[_Node.Pos()[1]][_Node.Pos()[0] + 1].Get_Weight(), end =" ")
	print(Map[_Node.Pos()[1]][_Node.Pos()[0] - 1].Get_Weight(), end =" ")
'''
#-------------------------A* pathfinding
Start.Set_Cost(0)
Now = Start
Can_Find_A_Path = 1
while End.Get_Pre() == None:
	Weight_around(Now)
	temp = math.inf
	for i in range(H):
		for j in range(W):
			if Map[i][j].Get_Is_chosed() == 0 and Map[i][j].Get_Weight() < temp:
				temp = Map[i][j].Get_Weight()
				Now = Map[i][j]
	Now.Set_Is_chosed(1)
	
	if temp == math.inf:
		Can_Find_A_Path = 0
		break

if 	Can_Find_A_Path == 0:
	print("Can not find any path from Start to End!")
	sys.exit()
	
Now = End
Path = [End]
Dir = ['A', 'B']
while Now != Start:
	Now.Set_Is_chosed(2)
	Now = Now.Get_Pre()
	Path.insert(0, Now)
Start.Set_Is_chosed(2)
#-------------------------A* pathfinding

for i in range(H):
	for j in range(W):
		if Map[i][j].Get_Is_chosed() == 2:
			'''
			if j != W - 1:
				cprint(Map[i][j].Get_Can_Pass(), 'red', attrs=['blink'], end =" ")
			else:
				cprint(Map[i][j].Get_Can_Pass(), 'red', attrs=['blink'])
			'''
			if j != W - 1:
				if Map[i][j] == Start:
					print("S", end =" ")
				elif  Map[i][j] == End:
					print("E", end =" ")
				else:
					print(Map[i][j].Get_Dir(), end =" ")
			else:
				if Map[i][j] == Start:
					print("S")
				elif  Map[i][j] == End:
					print("E")
				else:
					print(Map[i][j].Get_Dir())
		else:
			if j != W - 1:
				print(Map[i][j].Get_Can_Pass(), end =" ")
			else:
				print(Map[i][j].Get_Can_Pass())

print("\n")	
				
for i in range(len(Path)):
	if i == len(Path) - 1:
		print(Path[i].Pos())
	else:
		print(Path[i].Pos(), end ="->")
		
print("\n")	
		
print("Totally " + str(len(Path) - 1) + " step.")		
		
		
		
txt = input("\nPress Enter to End\n")
