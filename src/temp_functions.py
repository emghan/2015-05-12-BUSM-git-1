def k_to_c(temp):
	return temp - 273.15

def f_to_k(temp):
	return ((temp-32)*(5/9.0))+273.15

def f_to_c(temp):
	return k_to_c(f_to_k(temp))
