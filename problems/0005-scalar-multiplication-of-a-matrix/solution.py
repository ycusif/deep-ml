def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	if not matrix or not matrix[0]:
		return []

	return [[item * scalar for item in row] for row in matrix]