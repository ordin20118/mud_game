
def print_info_msg(msg):
    print_line()
    print("  ###   %s  ###   " % msg)
    print_line()

def print_warning_msg(msg):
    print("      !!! %s !!!       " % msg)


def print_title(title):
    side_len = int((50 - len(title) - 2)/2)
    print(side_len)
    print("="*side_len + " " + title + " " +  "="*side_len)

def print_line():
    print("="*60)

def print_confirm_msg(msg):
    input("[%s] - Enter" % msg)