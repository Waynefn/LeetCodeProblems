void rotate(int** matrix, int matrixRowSize, int *matrixColSizes) {
   	int size = matrixRowSize - 1;
	while (size > 0) {
		for (int i = 0; i < size; i++) {
			int offset = (matrixRowSize - size) >>1;
			int t = matrix[offset][offset + i];
			matrix[offset][offset + i] = matrix[offset + size - i][offset];
			matrix[offset + size - i][offset] = matrix[offset + size][offset + size - i];
			matrix[offset + size][offset + size - i] = matrix[offset + i][offset + size];
			matrix[offset + i][offset + size] = t;
		}
		size -= 2;
	} 
}
