from check import check
from input_data import input_data
from print_tab import print_tab as pt


def main(tab):
    counter = 0
    win = False
    while not win:
        pt(tab)
        if counter % 2 == 0:
            input_data("X", tab)
        else:
            input_data("O", tab)
        counter += 1
        if counter > 4:
            tmp = check(tab)
            if tmp:
                print(tmp, "- WIN!!!")
                win = True
        
                break
        if counter == 9:
            print("A draw")
            break
    print("What we have:")
    pt(tab)


tab = list(range(1, 20))

main(tab)
