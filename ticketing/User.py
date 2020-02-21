#유저 데이터 저장 class
#필요도에 대해서 다시 생각해볼 필요가 있음. 일단은 작업 중지.
class User():
    def __init__(self,name,age,ID,psw): #유저 이름, 나이, id와 pass word
        self.name = name
        self.age = age
        self.ID = ID
        self.psw = psw
        self.have_ticket = None
        self.ticket_list = []

    def login(self, ID, psw):
        if self.ID != ID:
            print("존재하지 않는 ID입니다.")
        elif self.psw != psw:
            print("비밀번호가 옳지 않습니다.")
        else:
            print("로그인이 확인되었습니다.")
    
    def User_ticket_buy(self, ticket_name):
        ticket_num = 0
        ticket_num = input("티켓의 매수를 확인해주세요.")

        print("결제 확인")
        self.have_ticket += ticket_num
        self.ticket_list.append(ticket_name)

        