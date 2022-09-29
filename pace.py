#!/usr/bin/env python3
def PrintFormer():## 打印提示语句前的修饰符
	print(">>>>",end='')
def TimeMinToSplit(time):## 将以分钟为单位的时间转换为以:分割的时间列表
	ret = list()
	if(int(time)>=60):
		ret.append(int(time)//60)
	ret.append(int(time)%60)
	ret.append(int((time-int(time))*60))
	return ":".join([str(item) for item in ret]) 

def TimeSplitToMin(time):## 将格式为:分割的时间处理为以分钟为单位的时间
	if(time.count(':') == 1):
		time = time.split(":")
		time = int(time[0]) + float(time[1])/60
	elif (time.count(':') == 2):
		time = time.split(':')
		time = int(time[0])*60 + int(time[1]) + float(time[2])/60
	elif (time.count(':')==0):
		time = float(time) 
	return time

def PaceCal():## 计算配速并以min:second min/km 格式输出
	PrintFormer()
	time = input("请输入时间(min)：")
	PrintFormer()
	length = float(input("请输入距离(km)："))
	time = TimeSplitToMin(time)
	pace = time/length ## 得到以min为单位的配速
	print("pace={}min/km".format(TimeMinToSplit(pace)))
	
def TimeFore():## 计算所用时间，并以min:second min 格式输出
	PrintFormer()
	pace = input("请输入配速(min/km)：")
	PrintFormer()
	length = float(input("请输入距离(km)："))
	pace = TimeSplitToMin(pace)
	time = length * pace
	print("time = {} min".format(TimeMinToSplit(time)))

def display():## 显示主界面函数
	print("==============")
	print("1 配速计算")
	print("2 时间预测")
	cho = input("请输入选择:")
	if(cho=="1"): 
		PaceCal()
	elif (cho == '2'):
		TimeFore()
	elif (cho == 'q'):## 若为q则退出该程序
		return 0;
	return 1;
		
if __name__ == "__main__":
	while(display()):
		print("~~~~~~~~~~~")
