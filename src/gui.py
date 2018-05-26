import tkinter as tk 
import random
# import runSim


def buttonClick(gravityEntry, window):
    g = gravityEntry.get()
    window.quit
    # print(eval(g))
    # print(isinstance(list(g), list))
    if isinstance(list(g), list):
    	window.quit

    # result.delete(0, tk.END)
    # result.insert(0, sentence)

def gui():
	window = tk.Tk()

	# varList = ['gravity', 'ballNum']
	# for var in varList:
	# 	labelName = var + "Label"
	# 	label = eval(labelName)
	# 	label = tk.Label(window, text=labelName)

	gravityLabel = tk.Label(window, text="重力加速度[x y]:")
	ballNumLabel = tk.Label(window, text="小球个数:")
	radiusLabel = tk.Label(window, text="小球半径:")
	locationLabel = tk.Label(window, text="小球初始位置:")

	
	# nameLabel.grid(row=0)
	gravityEntry = tk.Entry(window)
	ballNumEntry = tk.Entry(window)
	radiusEntry = tk.Entry(window)
	locationEntry = tk.Entry(window)
	gravityEntry.insert(10, '[0, 5000]')
	ballNumEntry.insert(10, '2')
	radiusEntry.insert(10,'60, 80')
	locationEntry.insert(10,'[600, 800], [1300, 500]')
	# ballNumEntry.grid(row=1,column=1)
	
	# button = tk.Button(window, text="确定", command=buttonClick(gravityEntry, window))
	button = tk.Button(window, text="确定", command=window.quit)
	
	# result = tk.Entry(window)
	gravityLabel.pack()
	gravityEntry.pack()

	ballNumLabel.pack()
	ballNumEntry.pack()
	
	radiusLabel.pack()
	radiusEntry.pack()

	locationLabel.pack()
	locationEntry.pack()
	
	button.pack()
	
	window.mainloop()
	g = gravityEntry.get()

	ballNum = ballNumEntry.get()
	# print(ballNum)
	ballNum = int(ballNum)
	radius = radiusEntry.get()
	location = locationEntry.get()

	try:
		# gx, gy = g.strip('[]').split(' ')
		# gx = float(gx)
		# gy = float(gy)
		g = eval(g)
		# radius = radius.split(' ')
		radius = eval(radius)
		# for val in radius:
		# val = float(val)
		location = list(eval(location))

		# location= location.strip('[]').split(' ')
		# for i in len(ballNum):
		# 	locationList.append([location[2*i], location[2*i+1]])
	except Exception:
		raise Exception ('Wrong input format')




	return g, ballNum, radius, location

if __name__ == '__main__':
	g, ballNum, radius, location = gui()
	print(location,type(location))
	# runSim.run_game(g)