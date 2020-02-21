import ticketing.Concert_info
#ticket 표현
class Concert_ticket():
    def __init__(self, Concert_info_struct, Reserv_name, Ticket_type, Ticket_num, Ticket_Rev_stock):
        self._Concert_info = Concert_info_struct #Concert_info의 콘서트가 그대로 들어감.
        self._Reservation_name = Reserv_name #예약자명
        self.Ticket_type = Ticket_type #스탠딩/좌석
        self.Ticket_num = Ticket_num #스탠딩/좌석 번호
        self.Ticket_Rev_stock = Ticket_Rev_stock #한 예약자의 보유 티켓 개수
    
    #티켓 정보 열람
    def show_ticket(self):
        print(self._Concert_info, self._Reservation_name, self.Ticket_type, self.Ticket_num, self.Ticket_Rev_stock)

    #