from ipaddress import *

count = 0
net = ip_network('172.16.168.0/255.255.248.0')
for ip in net:
    bin_ip = bin(int(ip))[2:].zfill(32)
    print(bin_ip)
    if bin_ip.count('1') % 5 != 0:
        count += 1
print(count)


# net = list(ip_network('145.92.137.88/255.255.240.0', 0))
# print(net)

#Определение адреса сети
# dict1 = {0: 'А', 145: 'B', 255: 'C', 137 : 'D', 128 : 'E', 240 : 'F', 88 : 'G', 92 : 'H'}
# mylist = [145 & 255, 92 & 255, 137 & 240, 88 & 0]
# for i in mylist:
#     if i in dict1: # если элемент из списка встречается в словаре, то выводим элемент словаря
#         print(dict1[i])


#Определение маски
# from ipaddress import *
# ip = ip_address('111.81.208.27')
# net = ip_address('111.81.192.0')
# for mask in range(33):
#     network = ip_network(f'{ip}/{mask}', 0)
#     if net == network.network_address:
#         mask = network.netmask
#         byte3 = str(mask).split('.')[2]
#         print(byte3)


#2231
# from ipaddress import *
# net4 = list(ip_network('162.198.0.157/255.255.255.224',0))
# a=0
# print (net4)
# for x in net4:
#     a+=1
#     print (f"{bin(int(x))[2:]},{x},{a}")
#
#     #╨║╨╛╨╗-╨▓╨╛ 1,0
#     s=bin(int(x))[2:]
#     print (s,s.count('1'),s.count('0'))
#
#
#
#
# #╨в╨╕╨┐ 13 11308
# # 203.155.196.98
#
# for i in range(23,24):
#     subnet1=ip_network(f"203.155.196.98/{i}", 0)
#     # for x in subnet1:
#     #     print (x)
#     print(subnet1)
#
#
#
# #17330
#
# for i in range(32,0,-1):
#     subnet1=ip_network(f"98.162.71.150/{i}",0)
#
#
#     subnet2=ip_network(f"98.162.71.140/{i}",0)
#     if subnet1==subnet2:
#         print(i,subnet1,subnet2)
#         break
# for x in subnet1:
#     print (x)
# for x in ip_network(f"98.162.71.150/28",0):
#     print (ip_network(f"98.162.71.150/28",0),x)