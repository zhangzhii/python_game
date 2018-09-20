print("MAD LIB GAME")
print("Enter answers to the following prompts\n")

guy = input("姓名： ")
food = input("请输入最近一次就餐的餐厅： ")
job = input("请输入您的职业： ")

story = "\nGUY是一个快乐的JOB，今天他结束了一天的工作蹦蹦跳跳地来到FOOD吃饭，结果把脚趾踢残了！"

story = story.replace("GUY", guy)
story = story.replace("FOOD", food)
story = story.replace("JOB", job)

print(story)