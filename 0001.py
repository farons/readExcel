#  第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
import uuid
from itertools import dropwhile

def generateActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4())
        while code in codeList:
            code = str(uuid.uuid4())    # 避免生成重复的code
        codeList.append(code)
    
    for code in codeList:
        print(len(codeList))
        print(code)

if __name__== '__main__':

    generateActivationCode(200)