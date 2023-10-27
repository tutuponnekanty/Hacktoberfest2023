def initialize_matrix(dim):
    """
    Initialize a square matrix of dimension 'dim' with all elements set to 0.

    Args:
    dim (int): The dimension of the square matrix.

    Returns:
    list: A 2D list representing the initialized matrix.
    """
    M=[]
    for i in range(dim):
        M.append([])
    for i in range(dim):
        for j in range(dim):
            M[i].append(0)
    return M
 
def dot_product(a,b):
    """
    Calculate the dot product of two vectors 'a' and 'b'.

    Args:
    a (list): The first vector.
    b (list): The second vector.

    Returns:
    int: The dot product of the two vectors.
    """
    dim=len(a)
    dop=0
    for i in range(dim):
        dop+=(a[i]*b[i])
    return dop

def req_row(M,i):
    """
    Retrieve the 'i-th' row from the matrix 'M'.

    Args:
    M (list): The input matrix.
    i (int): The index of the row to retrieve.

    Returns:
    list: The 'i-th' row of the matrix.
    """
    reqr=[]
    dim=len(M)
    for k in range(dim):
        reqr.append(M[i][k])
    return reqr

def req_col(M,j):
    """
    Retrieve the 'j-th' column from the matrix 'M'.

    Args:
    M (list): The input matrix.
    j (int): The index of the column to retrieve.

    Returns:
    list: The 'j-th' column of the matrix.
    """
    reqc=[]
    dim=len(M)
    for k in range(dim):
        reqc.append(M[k][j])
    return reqc

def mat_multip(A,B):
    """
    Perform matrix multiplication between matrices 'A' and 'B'.

    Args:
    A (list): The first matrix.
    B (list): The second matrix.

    Returns:
    list: The resulting matrix after multiplication.
    """
    dim=len(A)
    C=initialize_matrix(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j]=dot_product(req_row(A,i),req_col(B, j))
    return C

# Prompt user for matrix dimension
dim=int(input("Enter the matrix dimension: "))

# Initialize matrices A and B
A = initialize_matrix(dim)
B = initialize_matrix(dim)

# Prompt user to enter elements of A
print(f"Enter elements for matrix A ({dim}x{dim}):")
for i in range(dim):
    for j in range(dim):
        A[i][j] = int(input(f"A[{i}][{j}]: "))

# Prompt user to enter elements of B
print(f"Enter elements for matrix B ({dim}x{dim}):")
for i in range(dim):
    for j in range(dim):
        B[i][j] = int(input(f"B[{i}][{j}]: "))

# Perform matrix multiplication
result = mat_multip(A, B)

# Print the result
print(f"The result of matrix multiplication is:")
for row in result:
    print(row)
