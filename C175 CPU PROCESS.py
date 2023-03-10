import matplotlib.pyplot as plt
import psutil as p
app_name_list = []
app_name_list_percentage = []
Count = 0
for process in p.process_iter():
    Count = Count + 1
    if Count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print("name:",name, "cpu_usage:",cpu_usage)
        app_name_list.append(name)
        app_name_list_percentage.append(cpu_usage)
plt.figure(figsize = (15,7))
plt.xlabel("application")
plt.ylabel("usage")
plt.bar(app_name_list, app_name_list_percentage, width = 0.6, color = ("purple","red","blue","green","orange","pink"))
plt.show()