password = 'a123456'
times = 3
while True:
    pwd = input('please input your password:')
    if pwd == password:
        print('log in sucessfully.')
        break 
    else:
        times = times - 1
        print('Password is wrong! You can try', times,'times')
        if times == 0:
            break
