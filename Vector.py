class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs[::-1]  # Inverse the coefficients list for correct indexing (highest degree first)

    def __str__(self):
        degree = len(self.coeffs) - 1
        poly_str = ""
        for i, coeff in enumerate(self.coeffs):
            if coeff != 0:
                if degree - i == 0:
                    poly_str += f"{coeff}"
                elif degree - i == 1:
                    poly_str += f"{coeff}x + "
                else:
                    poly_str += f"{coeff}x^{degree - i} + "
        return poly_str.strip(" + ")

    def __add__(self, other):
        len_self = len(self.coeffs)
        len_other = len(other.coeffs)
        if len_self >= len_other:
            result_coeffs = [self.coeffs[i] + other.coeffs[i] if i < len_other else self.coeffs[i] for i in range(len_self)]
        else:
            result_coeffs = [self.coeffs[i] + other.coeffs[i] if i < len_self else other.coeffs[i] for i in range(len_other)]
        return Polynomial(result_coeffs[::-1])  # Inverse back the coefficients list

    def __mul__(self, other):
        len_self = len(self.coeffs)
        len_other = len(other.coeffs)
        result_coeffs = [0] * (len_self + len_other - 1)
        for i in range(len_self):
            for j in range(len_other):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result_coeffs[::-1])  # Inverse back the coefficients list

# Hàm chuyển đổi chuỗi thành list các số nguyên
def parse_polynomial(poly_str):
    coeffs = [int(coeff.strip()) for coeff in poly_str.split()]
    return coeffs

# Hàm nhập đa thức từ người dùng
def input_polynomial():
    poly_str = input("Nhập đa thức (các hệ số cách nhau bằng dấu cách từ hệ số cao nhất): ")
    coeffs = parse_polynomial(poly_str)
    return Polynomial(coeffs)

# Kiểm tra các phép toán trên đa thức
if __name__ == "__main__":
    print("Nhập đa thức thứ nhất:")
    poly1 = input_polynomial()

    print("\nNhập đa thức thứ hai:")
    poly2 = input_polynomial()

    print("\nĐa thức thứ nhất:", poly1)
    print("Đa thức thứ hai:", poly2)

    sum_poly = poly1 + poly2
    print("\nTổng hai đa thức:", sum_poly)

    product_poly = poly1 * poly2
    print("Tích hai đa thức:", product_poly)
