from groupper import FairGroupper

def main():
    names = ['김철수', '이명희', '천영희', '박석현', '홍길동', '장길산', '전지현', '김수현', '지현우', '휘성', '쥐디', '강백호', '서태웅']
    group_count = 4
    groupper = FairGroupper(names)
    groupper.random_group(group_count)

if __name__ == '__main__':
    main()
