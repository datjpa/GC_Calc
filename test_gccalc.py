from gccalc import calc_gc_content
#import pytest

def test_mid_gc():
	seq = "GCGCGCGCGCATATATATAT"
	exp = 50.0
	obs = calc_gc_content(seq)
	assert obs == exp

def test_high_gc():
        seq = "GCGCGCGCGCGCGCG"
        exp = 100.0
        obs = calc_gc_content(seq)
        assert obs == exp

def test_low_gc():
        seq = "ATATATATATATATATAT"
        exp = 0.0
        obs = calc_gc_content(seq)
        assert obs == exp

#def test_empty_seq():
 #       seq = ""
  #     obs = calc_gc_content(seq)
   #     assert obs == exp

test_mid_gc()
test_high_gc()
test_low_gc()

#@pytest.mark.skip(reason="Cleaning not yet implemented.")
#def test_invalid_characters():
#		seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
#		exp = 50.0
#		obs = calc_gc_content(seq)
#		assert obs == exp
		
#test_invalid_characters()








