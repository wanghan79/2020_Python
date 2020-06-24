from collections.abc import Iterable

class IsError():
    '''
    判断参数是否属于某种类型的错误
    '''

    def __init__(self, errortype, *args):
        self.errortype = errortype    #请求判断的错误类型
        self.args = args              #判断错误条件
        self.error_set = {
            "Iter": self.IsUniterable, "Type": self.IsTypeUninclude, "Range": self.IsRangeError
        }                             #错误类型及对应处理函数键值对

    def ErrorSelection(self):
        '''
        判断是否包括需要判断的错误类型，如果包括，返回判断结果；如果不包括，输出类型错误
        '''
        if self.errortype in self.error_set.keys():
            result = self.error_set.get(self.errortype)#result 赋值为对应的错误处理函数
            return result()
        else:
            print('Errortype is wrong')

    def IsUniterable(self):
        '''
        判断是否可以迭代
        '''
        var = self.args[0]
        if isinstance(var, Iterable) == False:
            return True
        else:
            return False

    def IsTypeUninclude(self):
        '''
        判断变量是否在给定的范围中
        '''
        var = self.args[0]
        range = self.args[1]
        if isinstance(range, Iterable) == True and var in range:
            return False
        elif var == range:
            return False
        else:
            return True

    def IsRangeError(self):
        '''
        判断给定数值范围是否错误
        '''
        range = self.args[0]
        if range[0]>range[1]:
            return True
        else:
            return False


