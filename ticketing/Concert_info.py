#콘서트 정보
#일단은 전석 스탠딩으로 생각하고 구현하기
class Concert_info():
    def __init__(self,Concert_name, Concert_date, Concert_size, Concert_standing_size):
        self.Concert_name = Concert_name #콘서트 이름
        self.Concert_date = Concert_date #콘서트 날짜
        self.Concert_size = Concert_size #콘서트 규모
        self.Ticket_stock = Concert_size #남은 티켓 수
        self.Concert_standing_size = Concert_standing_size #스탠딩석 규모

    #티켓 예매와 취소시 남는 티켓 수의 변동
    def Ticket_buy(self, Ticket_num):
        self.Ticket_stock -= Ticket_num
    def Ticket_cancle(self, Ticket_num):
        self.Ticket_stock += Ticket_num

    #공연정보 열람
    def show_concert(self):
        print("공연명 : %s\n공연날짜 : %s" % self.Concert_name,self.Concert_date)

    #