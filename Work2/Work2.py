#�������� ����������� ������� sum(a, b), 
#������������ ����� ���� ����� ��������������� �����. 
#�� ���� �������������� �������� ����������� ������ +1 � -1. 
#����� ������������ ������

#�������/�����:
#<function_name>(0,0) -> 0
#<function_name>(0,2) -> 2
#<function_name>(3,0) -> 3

def num (x,y):
    if x == 0:
        return y       
    else:
        return num(x-1,y+1)

print (num(0,2))