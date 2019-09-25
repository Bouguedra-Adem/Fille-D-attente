
import math


# M/M/S
def get_P0(lam,mu,S):
    u = lam/mu
    ro = u/S
    sum = 0;
    for k in range(0,S):
        sum += math.pow(u,k)/math.factorial(k)
    sum += (1/math.factorial(S))* math.pow(u,S)*(S*mu/(S*mu-lam))
    return 1/sum


def get_Pk(lamb,mu,S,k):
    if k <= S and k >= 1:
        return math.pow(lamb,k)*get_P0(lamb,mu,S)/(math.factorial(k)*math.pow(mu,k))
    elif k >= S:
        return math.pow(lamb,k)*get_P0(lamb,mu,S)/(math.pow(S,k-S)*math.factorial(s)*math.pow(mu,k))



def nb_moy_client_f(lamb,mu,S):

    A = lamb/(mu*S)
    Ps = get_Pk(lamb,mu,S,S)

    return A*Ps/ math.pow((1-A),2)


def nb_moy_client_s(lamb,mu,S):
    return nb_moy_client_f(lamb,mu,S) + lamb/mu


def temps_sej_f(lamb,mu,S):
    return nb_moy_client_f(lamb,mu,S)/lamb

def temps_sej_s(lamb,mu,S):
    return temps_sej_f(lamb,mu,S) + 1/mu




# M/M/Infini


def get_P0_Inf(lamb,mu):
    return math.exp(-lamb/mu)

def get_Pk_Inf(lamb,mu,k):
    return get_P0_Inf(lamb,mu)*math.pow(lamb/mu,k)/math.factorial(k)

def ns(lamb,mu):
    return lamb/mu
def ts(lamb,mu):
    return 1/mu

def nf(lamb,mu):
    return 0
def tf (lamb,mu):
    return 0





#M/M/S/L


def get_P0_SL(lamb,mu,S,L):
    u = lamb/mu
    sum1 = 0
    for i in range(0,S):
        sum1 += math.pow(u,i)/math.factorial(i)
    sum2 = 0
    for j in range(0,L-S+1):
        sum2 += math.pow(u/S,j)
    sum2 = math.pow(u,S)/math.factorial(S)*sum2
    sum = sum1 + sum2

    return 1 / sum

def get_Pk_SL(lamb,mu,S,L,k):
    u = lamb/mu;
    if k >=1 and k <=S :
        return (get_P0_SL(lamb,mu,S,L)*math.pow(u,k)/math.factorial(k))
    elif k >=S and k <= L:
        return get_P0_SL(lamb,mu,S,L)*math.pow(u,k)/(math.factorial(S)*math.pow(S,k-S))


def nf_SL(lamb,mu,S,L):
    u = lamb/mu
    ro = u/S
    sum = 0
    for i in range(1,S-L+1):
        sum += i*math.pow(ro,i-1)
    return get_P0_SL(lamb,mu,S,L)*ro*math.pow(S*ro,S)/math.factorial(S)

def ns_SL(lamb,mu,S,L):

    return nf_SL(lamb,mu,S,L)*(1-get_Pk_SL(lamb,mu,S,L,L))*(lamb/mu)

def tf_SL(lamb,mu,S,L):
    return (nf_SL(lamb,mu,S,L)/(lamb*(1-get_Pk_SL(lamb,mu,S,L,L))))

def ts_SL(lamb,mu,S,L):
    return (tf_SL(lamb,mu,S,L)+1/mu)



# M/M/S/Infini/N

def comb(k,n):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def get_P0_Inf_N(lamb,mu,S,N):
    u = lamb/mu
    sum1 = 0
    for k in range(0,N+1):
        sum1 += comb(k,N)*math.pow(u,k)
    sum2 = 0
    for k in range(0,N+1):
        sum2 += comb(k,N)*math.pow(u,k)*(math.factorial(k)/(math.factorial(S)*math.pow(S,k-S)))
    return 1/(sum1+sum2)


def get_Pk_Inf_N(lamb,mu,S,N,k):
    u = lamb/mu
    if k >=1 and k <= S:
        return comb(k,N)*math.pow(u,k)*get_P0_Inf_N(lamb,mu,S,N)
    elif k >= S and k <= N:
        return comb(k,N)*math.pow(u,k)*get_P0_Inf_N(lamb,mu,S,N)*(math.factorial(k)/(math.factorial(S)*math.pow(S,k-S)))

def nf_Inf_N(lamb,mu,S,N):
    sum = 0
    for i in range(S,N+1):
        sum += (i-S)*get_Pk_Inf_N(lamb,mu,S,N,i)
    return sum

def ns_Inf_N(lamb,mu,S,N):
    print(get_Pk_Inf_N(lamb,mu,S,N,5))
    print(get_Pk_Inf_N(lamb,mu,S,N,5))
    print(get_Pk_Inf_N(lamb,mu,S,N,5))
    sum1 = 0
    sum2 = 0
    for i in range(1,S):
        sum1 += i * get_Pk_Inf_N(lamb,mu,S,N,i)
        sum2 += get_Pk_Inf_N(lamb,mu,S,N,i)
    return (sum1 + nf_Inf_N(lamb,mu,S,N) +(1-sum2))

print(get_Pk_Inf_N(8,9,5,3,2))
