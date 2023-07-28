vote_num = 0

def vote():
    global vote_num
    print("投票します")
    vote_num += 1

def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0

def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))

