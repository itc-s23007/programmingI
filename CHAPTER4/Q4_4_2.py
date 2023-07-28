vote_num = 0

def vote(vote_n):
    print("投票します")
    vote_n += 1
    return vote_n

def reset_box(vote_n):
    print("箱を空にします")
    vote_n = 0
    return vote_n

def check_box(vote_n):
    print("票の数は{}です".format(vote_n))
    return

def vote(vote_n):
    print("投票します")
    vote_n += 1
    return vote_n

def reset_box(vote_n):
    print("箱を空にします")
    vote_n = 0
    return vote_n

def check_box(vote_n):
    print("票の数は{}です".format(vote_n))
    return vote_n

vote_num = 0

# 初期状態の箱
vote_num = check_box(vote_num)  # 票の数は0です

# 投票
vote_num = vote(vote_num)
vote_num = vote(vote_num)
vote_num = vote(vote_num)

# 現在の箱の状態
vote_num = check_box(vote_num)  # 票の数は3です

# 箱をリセット
vote_num = reset_box(vote_num)
vote_num = check_box(vote_num)  # 票の数は0です

