class Check:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.par_list={'}':'{',')':'(',']':'['}

    def paren(self,exp):
        for val in exp:
            if val in self.par_list.values():
                self.stack.append(val)
                self.top+=1
            elif val in self.par_list.keys():
                if self.top==-1: 
                    self.top=None
                    break
                elif self.stack[-1] == self.par_list[val]:
                    self.stack.pop()
                    self.top-=1
        
        if self.top ==-1:
            return "Balanced"
        else: return "UnBalanced"


if __name__ == "__main__":
    obj=Check()
    exp="[()]{()}{[()()]()}"
    print("The experience is :: ",obj.paren(exp))
