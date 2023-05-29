import easygui



class maze_cell:
	def __init__(self, pos, direction = (True, True, True, True)):
		self.pos = pos
		self.direction = direction

	def dir_convert(direction):
		match direction:
			case "front":
				return 0
			case "right":
				return 1
			case "back":
				return 2
			case "left":
				return 3
			case _:
				return -1

	def isvalid_dir(self, direction):
		if self.dir_convert(direction) == -1: raise ValueError("Invalid direction")
		return self.direction[self.dir_convert(direction)]
	
# easygui.integerbox("test","Title",0,upperbound=10**10**10)s

while True:
	username = easygui.enterbox("請輸入使用者名稱：", "使用者名稱")
	if username == None:
		break

	if username == "Programmer":
		mazeprop = ["檔案名稱","長度","寬度"]
		result = []

		while True:
			if result == None:
				break
			errmsg = "\n"
			result = easygui.multenterbox(f"請輸入迷宮資訊：{errmsg}", "建立迷宮", mazeprop, result)
			for i in range(len(result)):
				if result[i].strip() == "":
					errmsg = errmsg + (f'"{mazeprop[i]}" 是必要資訊。')
			if errmsg == "\n":
				break

		mazename = result[0]
		mazeheight = int(result[1])
		mazelength = int(result[2])

		#寫入迷宮
		with open(f'maze/{mazename}.maz', 'w') as f:
			maze = [""]
			pointer = maze
			for i in range(mazeheight-1):
				maze.extend([""])

			err1 = mazeheight
			err2 = 0
			while True:
				maze = easygui.multenterbox(f"請輸入迷宮地形：\n仍然有 {err1} 行未填寫、 {err2} 行填寫有誤", "建立迷宮", pointer, maze)
				err1 = 0
				err2 = 0

				if maze == None:
					break
				
				for i in range(len(maze)):
					if (maze[i].strip() == ""):
						pointer[i] = ">"
						err1 += 1
					if (len(maze[i]) != mazelength):
						pointer[i] = ">"
						err2 += 1
						continue
					for j in range(len(maze[i])):
						if (int(maze[i][j]) // 4 != 0):
							pointer[i] = ">"
							err2 += 1
							break
				
				if err1 == 0 and err2 == 0:
					f.write(f"{mazeheight}\n{mazelength}\n")
					for i in maze:
						f.write(f"{i}\n")

					easygui.msgbox("創建成功！","訊息")
					break

			
	elif username == "John Cena":
		easygui.msgbox("I can't see you!", "He's name is John Cena")
	else:
		pass