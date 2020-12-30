def height(ro):

	if not ro:
		return 0

	return max(height(ro.l), height(ro.r)) + 1