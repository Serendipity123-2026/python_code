"""
           打印如下图形
        * * * * * * * * *
        * * * * * * * * *
        * * * * * * * * *
        * * * * * * * * *
"""
print("============ 矩形 ============")
for i in range(4):
    for j in range(9):
        print("*", end=" ")
    print()

"""
        * * * * * * * * * 
       * * * * * * * * * 
      * * * * * * * * * 
     * * * * * * * * * 
"""
print("============ 平行四边形 ============")
for i in range(4):
    for k in range(3 - i):          # 该循环控制空格
        print(" ", end="")
    for j in range(9):
        print("*", end=" ")
    print()

"""
            *
           ***
          *****
         *******
        *********
"""
print("============ 等腰三角形 ============")
for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range((2 * i) + 1):
        print("*", end="")
    print()
"""
        *
        **
        ***
        ****
        *****
"""
print("============ 直角三角形 ============")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

"""
            *
           ***
          *****
         *******
        *********
         *******
          *****
           ***
            *
"""
print("============ 菱形 ============")
for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range((2 * i) + 1):
        print("*", end="")
    print()
for i in range(4):
    for k in range(i + 1):
        print(" ", end="")
    for j in range(7 - (2 * i)):
        print("*", end="")
    print()

"""
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *
"""
print("============ 空心菱形 ============")
for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range((2 * i) + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")

    print()
for i in range(4):
    for k in range(i + 1):
        print(" ", end="")
    for j in range(7 - (2 * i)):
        if j == 0 or j == 6 - (2 * i):
            print("*", end="")
        else:
            print(" ", end="")
    print()




# for i in range(5):
#     for k in range(4 - i):
#         print("+", end="")
#     for j in range((2 * i) + 1):
#         if j == 0 or j == 2 * i:   # i=0 j=0   i=1 j=2
#             print("*", end="")
#         else:
#             print("+", end="")
#     print()