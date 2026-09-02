def maxi (*args):
    #return (max(args))
    max = args[0]
    for val in args:
        if val > max:
            max = val
    return max
if __name__ == '__main__':
    print(f"maximum =  ") maxi (10,53,...)