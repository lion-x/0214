birthday = input("请输入你的生日(格式: YYYYMMDD): ")
times = int(birthday) - 0x130B0DB
for i in range(times):
    print(i)
    print("I love you!")
print("数数一共说了多少遍 \"I love you\" ？想起什么电影了吗？请回复该电影名到公众号（五个字）。")
