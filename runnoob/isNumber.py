def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass

    return False

# test cases
print(is_number('foo'))      # False
print(is_number('1'))        # True 
print(is_number('1.5'))      # True
print(is_number('-1.5'))     # True
print(is_number('1e10'))     # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False