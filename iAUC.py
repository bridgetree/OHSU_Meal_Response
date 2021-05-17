#Sample a and b
#a = [0,1,2,3,4,5]
#b = [10,12,10,10,8,10]

def inc_auc(a,b):
    iAUC  = []
    for i in range(len(a)-1):
    
        if((b[i+1]-b[0] >= 0) & (b[i]-b[0] >= 0)):
            result = ((b[i]-b[0]+b[i+1]-b[0])/2)*(a[i+1]-a[i]) 
            iAUC.append(result)

        elif((b[i+1]-b[0] < 0) & (b[i]-b[0] >= 0)):
            result = (b[i]-b[0])*((b[i]-b[0])/(b[i]-b[i+1])*(a[i+1]-a[i])/2)
            iAUC.append(result)

        elif((b[i+1]-b[0] >= 0) & (b[i]-b[0] < 0)):
            result = (b[i+1]-b[0])*((b[i+1]-b[0])/(b[i+1]-b[i])*(a[i+1]-a[i])/2)
            iAUC.append(result)

        elif((b[i]-b[0] < 0) & (b[i+1]-b[0] < 0)):
            iAUC.append(0)
    return(sum(iAUC))
