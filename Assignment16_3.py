def Count():
    FileName="Data.txt"
    fobj=open(FileName,"r")

    lines=fobj.readlines()
    line_cnt=len(lines)
    word_cnt=0
    char_cnt=0

    for i in lines:
        word=i.split()
        word_cnt=word_cnt + len(word)
        char_cnt=char_cnt + len(i)

    print("Lines in files are :",line_cnt)
    print("Words in lines are :",word_cnt)
    print("Characters in line are :",char_cnt)

def main():
    Count()

if __name__=="__main__":
    main()