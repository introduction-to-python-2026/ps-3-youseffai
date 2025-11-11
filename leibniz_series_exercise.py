def approximate_pi(n_terms):
    t_terms = 0 
    for i in range(n_terms + 1):
      term = ((-1)**i) / (2 * i + 1) 
      t_terms += term
    pi = 4 * t_terms

    return pi
