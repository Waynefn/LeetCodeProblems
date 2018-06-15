unsigned __int32 reverseBits(unsigned __int32 n) {
	unsigned __int32 res = 0;
	for (int i = 31; i >= 0; i--) {
		if (2 * i - 31 > 0)
			res += (n&(1 << i)) >> 2 * i - 31;
		else
			res += (n&(1 << i)) << 31 - 2 * i;
	}
	return res;
}
