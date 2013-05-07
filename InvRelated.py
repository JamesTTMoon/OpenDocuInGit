
# create the root window



class HtIndvBase : # MonoBehaviour {
    # 객체에 할당되는 스크립트의 부모 클래스
    
    mName = ""; mState = "상태 이름"
    
    def SetState (string_pStt): # (int pValue, bool pIsTotal): // 10 , 5 , ...
        # 상태 세팅.
        mState = string_pStt
        

class HtFriendIdv (HtIndvBase): 
    # 프렌드 폴리곤에 할당되는 스크립트
    
    def MdFormatter() : #(int pForm, int pLatt, Godirum pGod):
        # 12 + 34 같은 경우를 정의하는 함수. 
        
        pass
        
        

    

"""  Schedule

1.  Coding ..
1.1     3   자릿수 넘어가는 부분
1.2     3   곱셈
1.3     1   이펙트


2.  Design
        이펙트

"""