from height import height

def is_balanced_bst(ro):

	if not ro:
		return True

	hl = height(ro.l)
	hr = height(ro.r)

	if (
		abs(hl - hr) <= 1
		and
		is_balanced_bst(ro.l)
		and
		is_balanced_bst(ro.r)
	):
		return True

	return False
