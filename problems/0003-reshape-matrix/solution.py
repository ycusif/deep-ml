import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	if not a or not a[0]:
		return []
	flat= [item for row in a for item in row]
	new_rows, new_cols = new_shape
	if len(flat) != new_rows * new_cols:
		return []

	reshaped=[]
	for i in range(new_rows):
		start= i * new_cols
		end= start + new_cols
		reshaped.append(flat[start:end])

	return reshaped