def validate_cpf(cpf: str) -> bool:
    return True


def validate_cnpj(cnpj: str) -> bool:
    return True


def is_area_smaller_than_areable_and_vegetation(total_area: float, arable_area: float, vegetation_area: float) -> bool:
    return total_area < arable_area + vegetation_area
