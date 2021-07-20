a = [0, 1, 1, 2, 3, 3]

def fp(parent, x):
  if parent[x] != x:
    parent[x] = fp(parent, parent[x])
    print(x)
  print(x)
  return x

print(fp(a, 5))
print(a)


#a[5] =  fp(a,3) = 3

  #a[3] =  fp(a,2) = 2

    #a[2] =  fp(a,1) = 1

      #print(1)
      #return 1

    #print(2)
    #return 2

  #print(3)
  #return 3

#print(5)  
#return 5

print('\n\n\n\n\n\n')

a = [0, 1, 1, 2, 3, 3]

def fp(parent, x):
  if parent[x] != x:
    parent[x] = fp(parent, parent[x])
    print(x)
  print(x)
  return parent[x]

print(fp(a, 5))
print(a)


#a[5] =  fp(a,4) = 1

  #a[4] =  fp(a,3) = 1

    #a[3] =  fp(a,2) = 1

      #a[2] =  fp(a,1) = 1

        #print(1)
        #return parent[1]

      #print(2)
      #return parent[2]

    #print(3)
    #return parent[3]

  #print(4)
  #return parent[4]

#print(5)  
#return parent[5]