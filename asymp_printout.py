from math import sqrt, log2


def asymp_printout(size_count_list):
    print("n\tT\tT/log(n)\tT/sqrt(n)\tT/n\tT/(n*log(n))\tT/n**2")
    for size, count in size_count_list:
        T = count
        log_n = log2(size)
        sqrt_n = sqrt(size)
        T_over_n = T / size
        T_over_n_log_n = T / (size * log_n)
        T_over_n_squared = T / (size ** 2)
        print(
            f"{size}\t{T}\t{T_over_n_log_n:.2f}\t{T_over_n:.2f}\t{T_over_n:.2f}\t{T_over_n_log_n:.2f}\t{T_over_n_squared:.2f}")
