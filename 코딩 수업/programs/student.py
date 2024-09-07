class score:
    def __init__(self):
        self.studentpoints={}

    # 학생들이 점수를 추가하는 함수
    def add_student(self,name,point):
        self.studentpoints[name]=point
    
    # 평균점수를 계산하는 기능
    def averagepoints(self):
        total=sum(self.studentpoints.values())
        return total/len(self.studentpoints)
    # 최고점수 찾는 기능
    def maxpoints(self):
        name=max(self.studentpoints,key=self.studentpoints.get)
        return name,self.studentpoints[name]

def main():
    points=score()
    while True:
        print("\n점수관리 프로그램 입니다")
        print("옵션을 선택하세요")
        print("1.새로운 학생 추가")
        print("2.모든 점수 출력")
        print("3.최고점수 찾기")
        print("4.평균점수 계산")
        choice=int(input("숫자를 선택하세요: "))
        if choice==1:
            name=input("학생 일름을 입력하세요: ")
            point=int(input("학생 점수를 입력하세요: "))
            points.add_student(name,point)
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            avg=points.averagepoints()
            print(f"평균점수: {avg}")
        else:
            pass
main()