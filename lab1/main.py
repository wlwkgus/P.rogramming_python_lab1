# TODO : Implement class 'WaitingList'
from waiting_list import WaitingList

def main():
    max_try = 99999
    is_end = False
    waiting_list = WaitingList()
    for i in range(max_try):
        if is_end:
            break
        print("===옵션===")
        print("1) 웨이팅 리스트 추가")
        print("2) 현재 웨이팅 리스트 조회")
        print("3) 손님 들어갑니다")
        print("4) 종료")
        a = input(">>> 옵션을 입력해주세요")
        if a == '':
            a = 0
        else:
            a = int(a)
        if a == 1:
            print()
            name = input(">>> 이름을 입력해주세요")
            waiting_list.add_customer(name)
            print()
        elif a == 2:
            print()
            waiting_list.print_current_list()
            print()
        elif a == 3:
            name = waiting_list.pop_customer()
            print()
            print(">>> {}님 들어오세요".format(name))
            print()
        elif a == 4:
            is_end = True
        else:
            print()
            print(">>> 알 수 없는 옵션입니다.")
            print()
    exit(0)


if __name__ == '__main__':
    main()
