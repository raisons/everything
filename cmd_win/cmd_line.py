from eprogress import LineProgress

def CreateProgress(title,max_l):
    line_progress = LineProgress(title='qweqweqew',total=100,symbol='#')
    for i in range(101):
        line_progress.update(i*2)
        time.sleep(0.05)


