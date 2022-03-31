class Calculator:
    # 여기에 코드를 작성해보세요!
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

    def sub(self,num):
        self.result -= num
        return self.result

    def mul(self,num):
        self.result *= num
        return self.result

    def div(self, num):
        if num !=0:
            self.result /= num
            return self.result
        else: 
            print("계산 안됩니다")
            return None

        

calculator1 = Calculator("이영서",21)
calculator1.add(2)
calculator1.div(0)
print(calculator1.result)

