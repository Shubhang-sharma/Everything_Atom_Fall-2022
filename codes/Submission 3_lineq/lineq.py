import my_lib as mb

#INUPT---------------
filename = 'input.txt'
with open(filename) as data:
    arr = mb.read_data(data)
mb.floater(arr) #floats the data which was read as strings before

# END OF INPUT----------------------------


#OUTPUT---------------------------#
res_file = open('lineq_output.txt','w')
Res = []
#----------------------------------

print('QUESTION 1')

# --------- GAUSS-JORDAN ELIMINATION
M,P = arr[0],arr[0]
N,Q = arr[1][0],arr[1][0]

for i in range(len(N)): #Condtruction of Augmented Matrix
    M[i].append(N[i])
print('Solution Using Gauss Elimination')
mb.print_array(mb.gauss(M))

#---------- LU Decomposition

print('Solution using LU',mb.ludecomp(P,Q),'\n')

# -------------------------------------------------------------------------------
# -----------------------------------------------------------------------------
print('QUESTION 2')

G,I = arr[2],arr[2]
H,J = arr[3][0],arr[3][0]
#--------- Gauss-Seidal
print('solution using Gauss-seidel',mb.seidel(I,J),'\n')

#---------- Cholesky
if mb.if_symmetric(G):
    print('solution using cholesky',mb.cholesky(G,H),'\n')

print('QUESTION 3')
X,V =  arr[4],arr[4]
Y,Z = arr[5][0],arr[5][0]
#LU -without rearranging
print('Solution using LU',mb.ludecomp(V,Z),'\n')

#Seidel - Passing the rearrange matrix
print('solution using Gauss-seidel',mb.seidel(mb.rearrange_diag_dom(X),Y),'\n')
#Jacobi- Passing the rearranged matrix
print('solution using Jacobi',mb.jacobi(X,Y),'\n') #note that X is already rearranged.
