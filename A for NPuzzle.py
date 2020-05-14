class Node:
    def __init__(self,data,level,fval,pre,move):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval
        self.pre=pre
        self.move=move
    def generate_child(self):
            """ Generate child nodes from the given node by moving the blank space
                either in the four directions {up,down,left,right} """
            x1,y1,x2,y2 = self.find(self.data,'-')
            """ val_list contains position values for moving the blank space in either of
                the 4 directions [up,down,left,right] respectively. """
            val_list = [[x1,y1-1],[x1,y1+1],[x1-1,y1],[x1+1,y1],[x2,y2-1],[x2,y2+1],[x2-1,y2],[x2+1,y2]]
            children = []
            cntt=0
            for i in val_list:
                cntt+=1
                if(cntt==1):
                    child = self.shuffle(self.data,x1,y1,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x1][y1-1],"right"])
                        children.append(child_node)
                elif(cntt==2):
                    child = self.shuffle(self.data,x1,y1,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x1][y1+1],"left"])
                        children.append(child_node)
                elif(cntt==3):
                    child = self.shuffle(self.data,x1,y1,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x1-1][y1],"down"])
                        children.append(child_node)
                elif(cntt==4):
                    child = self.shuffle(self.data,x1,y1,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x1+1][y1],"up"])
                        children.append(child_node)
                elif(cntt==5):
                    child = self.shuffle(self.data,x2,y2,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x2][y2-1],"right"])
                        children.append(child_node)
                elif(cntt==6):
                    child = self.shuffle(self.data,x2,y2,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x2][y2+1],"left"])
                        children.append(child_node)
                elif(cntt==7):
                    child = self.shuffle(self.data,x2,y2,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x2-1][y2],"down"])
                        children.append(child_node)
                elif(cntt==8):
                    child = self.shuffle(self.data,x2,y2,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0,self,[self.data[x2+1][y2],"up"])
                        children.append(child_node)
                ##print (child)
            return children
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data) and x2!="-" and y2!="-":
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy(self,root):
            """ Copy function to create a similar matrix of the given node"""
            temp = []
            for i in root:
                t = []
                for j in i:
                    t.append(j)
                temp.append(t)
            return temp    
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        cnt=0
        ls=[]
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    ls.append(i)
                    ls.append(j)
                    cnt+=1
                    if (cnt==2):
                        return ls[0],ls[1],ls[2],ls[3]
class Puzzle:
    def __init__(self,size,start,goal):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.start=start
        self.goal=goal
        self.open = []
        self.closed = []
    def accept(self):
            """ Accepts the puzzle from the user """
            puz = []
            for i in range(0,self.n):
                temp = input().split(" ")
                puz.append(temp)
            return puz
    def f(self,start,goal,tp):
            """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
            if(tp=="manhatten"):
                return self.mh(start.data,goal)+start.level
            else:
                return self.h(start.data,goal)+start.level
    def h(self,start,goal):
            """ Calculates the number of different tiles between the given puzzles """
            temp = 0
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if start[i][j] != goal[i][j] and start[i][j] != '-':
                        temp += 1
            return temp

    def mh(self,start,goal):
            """ Calculates the manhatten distance between the given puzzles """
            temp = 0
            for i in range(0,self.n):
                for j in range(0,self.n):
                    dist=self.ds(start[i][j],i,j,goal)
                    temp=temp+dist
            return temp
        
    def ds(self,val,c1,c2,goal):
        dt=0
        for c3 in range(0, self.n):
            for c4 in range(0, self.n):
                if(val==goal[c3][c4]):
                    dt = abs(c3-c1)+abs(c4-c2)
                    return dt
    
    def process(self,typ):
            iterations=0
            start = Node(self.start,0,0,None,None)
            start.fval = self.f(start,self.goal,typ)
            """ Put the start node in the open list"""
            self.open.append(start)
            print("\n\n")
            while True:
                iterations+=1
                cur = self.open[0]


                
                """ If the difference between current and goal node is 0 we have reached the goal node"""
                if(self.h(cur.data,self.goal) == 0):
                    outputFile=open("output.txt","a+")
                    revNode=cur
                    moves=[]
                    moves1=[]
                    while (revNode.pre!=None):
                        moves.append(revNode.move)
                        revNode=revNode.pre
                    moves.reverse()
                    for val in moves:
                        moves1.append("("+val[0]+","+val[1]+")")
                    pt=", ".join(moves1)
                    outputFile.write(pt)
                    outputFile.write("\n")
                    print ("No of nodes discovered:"+str(iterations))
                    print ("Done")
                    break
                
                for i in cur.generate_child():
                    included=False
                    i.fval = self.f(i,self.goal,typ)
                    for close in self.closed:
                        if(close.data==i.data):
                            included=True
                            break
                    if(not(included)):
                        self.open.append(i)
                self.closed.append(cur)
                del self.open[0]
                """ sort the open list based on f value """
                self.open.sort(key = lambda x:x.fval,reverse=False)

print ("Enter the puzzle size")
length=input()
print ("Please enter the file names with extension seperated by tab")
input1=input().strip()
files=input1.split("\t")


initial=open(files[0], "r+")
goal1=open(files[1], "r+")

start=[]
goal=[]
for linei in initial:
    ln=linei.strip()
    start.append(ln.split("\t"))

for lineg in goal1:
    ln=lineg.strip()
    goal.append(ln.split("\t"))


print ("\nWhat is your heuristic function: (manhatten/misplaced tiles)")
typ=input()
puz = Puzzle(int(length),start,goal)
puz.process(typ)
