def calc_gc_content(seq):
	gc_content = ((seq.count("C") + seq.count("G")) / 
			len(seq) * 100)
	return gc_content
