def approximate_pi(n_terms):
  tt=0
  for i in range (n_terms):
    t1=((-1)**i)
    t2=(2*i+1)
    t=t1/t2
    tt+=t

  pi=4*(tt)
  return pi
