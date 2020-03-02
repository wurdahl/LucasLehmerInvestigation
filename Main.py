#This function will return true if the Merseinne number M(p) is prime using the Lucas-Lehmer method
def LucLehIsPrime(p):
    Mp = 2**(p)-1

    s = 4

    for i in range(p-2):
        s = (s**2 - 2)%Mp

    return(s==0)

primeList = []

outputFile = open("output.txt","w")

if __name__ == "__main__":

    for i in range(5000):
        if LucLehIsPrime(i):
            primeList.append(2**i - 1)

    outputFile.write(str(primeList));
    outputFile.write("\n")
    outputFile.write(str(len(str(primeList[-1])))+" Digits Long")
