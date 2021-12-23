import factorial.factorial
import exp_root.exponentiation
import exp_root.root
import logarithm.logarithm
def main():
    print('Welcome to project "Practice_17_KM_11_Krakovych_Boryslav"!')
    a=True
    while a:
        a=True
        while a:
            function=input('Select and enter one of these functions: fact, exp2, exp3, root2, root3, log, ln, lg:')
            if function == 'fact':
                ok=False
                while not ok:
                    try:
                        n=int (input('Enter n to calculate the factorial of n:'))
                        ok=True
                        print ('Result:',factorial.factorial.fact(n))
                        break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'exp2':
                ok=False
                while not ok:
                    try:
                        n=int (input('Enter n to calculate the second power of n:'))
                        ok=True
                        print ('Result:',exp_root.exponentiation.exp2(n))
                        break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'exp3':
                ok=False
                while not ok:
                    try:
                        n=int (input('Enter n to calculate the third power of n:'))
                        ok=True
                        print ('Result:',exp_root.exponentiation.exp3(n))
                        break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'root2':
                ok=False
                while not ok:
                    try:
                        n=int (input('Enter n to calculate the root of the second power from n:'))
                        if n >= 0:
                            ok=True
                            print ('Result:',exp_root.root.root2(n))
                            break
                        else:
                            print('Error. You input a negative value. Try again, please.')
                            continue
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'root3':
                ok=False
                while not ok:
                    try:
                        n=int (input('Enter n to calculate the root of the third power from n:'))
                        ok=True
                        print ('Result:',exp_root.root.root3(n))
                        break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'log':
                ok=False
                while not ok:
                    try:
                        a=int (input('Enter a to calculate the logarithm b to the base a:'))
                        if a < 0:
                            print('Error. You input a negative value. Try again, please.')
                            continue
                        elif a == 1 or a == 0:
                            print('Error. You input an incorrect value. Try again, please.')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                ok=False
                while not ok:
                    try:
                        b=int (input('Enter b to calculate the logarithm b to the base a:'))
                        if b < 0:
                            print('Error. You input a negative value. Try again, please.')
                            continue
                        elif b == 0:
                            print('Error. You input an incorrect value. Try again, please.')
                            continue
                        else:
                            ok=True
                            print ('Result:',logarithm.logarithm.log(b,a))
                            break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'ln':
                ok=False
                while not ok:
                    try:
                        b=int (input('Enter b to calculate the natural logarithm b:'))
                        if b < 0:
                            print('Error. You input a negative value. Try again, please.')
                            continue
                        elif b == 0:
                            print('Error. You input an incorrect value. Try again, please.')
                            continue
                        else:
                            ok=True
                            print ('Result:',logarithm.logarithm.ln(b))
                            break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            elif function == 'lg':
                ok=False
                while not ok:
                    try:
                        b=int (input('Enter b to calculate the decimal logarithm b:'))
                        if b < 0:
                            print('Error. You input a negative value. Try again, please.')
                            continue
                        elif b == 0:
                            print('Error. You input an incorrect value. Try again, please.')
                            continue
                        else:
                            ok=True
                            print ('Result:',logarithm.logarithm.lg(b))
                            break
                    except ValueError:
                        print('Error. You input an incorrect value. Try again, please.')
                        continue
                break
            else:
                print ('You entered incorrect function. Try again, please.')
                continue
        exit=input('Do you want to continue working in this project? Enter yes or no:')
        if exit=='yes':
            continue
        elif exit=='no':
            print('Shutting down the project.')
            break
if __name__ == '__main__':
    main()