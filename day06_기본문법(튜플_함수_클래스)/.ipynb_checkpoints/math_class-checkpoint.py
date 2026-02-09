class Math:
    ### 생성자 함수 정의하기
    def __init__(self, a, b) :
        ### 함수 정의시 사용한 a, b변수는 지역변수(함수 내에서만 접근 가능)라고 하며,
        # - self가 붙은 aa, bb변수는 전역변수(클래스 내부 및 외부에서 접근 가능)라고 칭함
        self.aa = a
        self.bb = b
        
    ### 일반 함수 정의하기
    def getPlus(self):
        return self.aa + self.bb
        