#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy 
def rnp(sigma,a,T,S0,dt):
    T = int(T)
    # 하향평균회귀 및 상향평균회귀 기준노드
    j_max = int( numpy.ceil( 0.184/(a*dt) ) )
    j_min = - j_max

    # 각 기간마다 j값을 정해준다.
    num_j = numpy.zeros(T)
    for i in range(T):
        num_j[i] = min(j_max*2+1, 2*i+1)

    # 조정 전 단기선도이자율 트리 생성
    no_adj = numpy.zeros([int(j_max*2+1),T])

    for i in range(len(num_j)):  # i = 0,1,2
        jj = int( (num_j[i]-1)/2 ) # jj = 0,1,2
        jj = [ii for ii in range(-jj,jj+1)][::-1]   # jj = [0], [1,0,-1], [2,1,0,-1,-2]
        temp = 0
        for j in jj:          # j = [0], [1,0,-1], [2,1,0,-1,-2]
            no_adj[temp,i] = sigma*numpy.sqrt(3*dt)*j
            temp = temp + 1

    # 상태변화확률(RNP)를 결정한다.
    rnp = [[1]]
    for i in range(T-1):
        p = [] #zeros(int(num_j[i]*3))

        if int(num_j[i+1]) == (i+1)*2 + 1 : ## normal 상태만 유지된다.
            jj = int( (num_j[i]-1)/2 )
            jj = [ii for ii in range(-jj,jj+1)][::-1]
            for j in jj:
                pu = 1/6 + 1/2*(a**2 * j**2 * dt**2 - a*j*dt) 
                p.append(pu)
                pm = 2/3 - a**2 * j**2 * dt**2
                p.append(pm)
                pd = 1/6 + 1/2*(a**2 * j**2 * dt**2 + a*j*dt)
                p.append(pd)
        else :                         ## downward / normal / upward 상태가 유지된다.
            jj = int( (num_j[i]-1)/2 )
            jj = [ii for ii in range(-jj,jj+1)][::-1]
            j = jj[0]                    ## downward mean reversion
            pu = 7/6 + 1/2*(a**2 * j**2 * dt**2 - 3*a*j*dt) 
            pm = -1/3 - a**2 * j**2 * dt**2 + 2*a*j*dt
            pd = 1/6 + 1/2*(a**2 * j**2 * dt**2 - a*j*dt)
            p.append(pu)
            p.append(pm)
            p.append(pd)

            for j in jj[1:-1]:           ## normal
                pu = 1/6 + 1/2*(a**2 * j**2 * dt**2 - a*j*dt) 
                pm = 2/3 - a**2 * j**2 * dt**2
                pd = 1/6 + 1/2*(a**2 * j**2 * dt**2 + a*j*dt)
                p.append(pu)
                p.append(pm)
                p.append(pd)

            j = jj[-1]                    ## upward mean reversion
            pu = 1/6 + 1/2*(a**2 * j**2 * dt**2 + a*j*dt) 
            pm = -1/3 - a**2 * j**2 * dt**2 - 2*a*j*dt
            pd = 7/6 + 1/2*(a**2 * j**2 * dt**2 + 3*a*j*dt)
            p.append(pu)
            p.append(pm)
            p.append(pd)

        rnp.append(p)
    return rnp

