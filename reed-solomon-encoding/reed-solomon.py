class ReedSolomon:
    def __init__(self, field, gen, msglen, ecclen):
        self.f = field  # 有限域
        self.generator = gen  # 生成元
        self.message_len = msglen
        self.ecc_len = ecclen
        self.codeword_len = msglen + ecclen

    def encode(self, message):
        if len(message) != self.message_len:
            raise ValueError("Invalid message length")
        genpoly = self._make_generator_polynomial()
        # 多項式除法計算校正碼...
        eccpoly = [self.f.zero()] * self.ecc_len
        for msgval in reversed(message):
            factor = self.f.add(msgval, eccpoly[-1])
            del eccpoly[-1]
            eccpoly.insert(0, self.f.zero())
            for j in range(self.ecc_len):
                eccpoly[j] = self.f.subtract(eccpoly[j], self.f.multiply(genpoly[j], factor))
        return [self.f.negate(val) for val in eccpoly] + message
    
    def _make_generator_polynomial(self):
        genpoly = [self.f.one()] + [self.f.zero()] * self.ecc_len
        for i in range(1, self.ecc_len):
            genpoly[i] = self.f.multiply(genpoly[i], self.generator)
        return genpoly
    
    
if __name__ == "__main__":
    # 設定有限域與生成元
    field = 2
    gen = 3
    msglen = 20
    ecclen = 10
    encoder = ReedSolomon(field, gen, msglen, ecclen)
    
    encoder.encode("hi, I am Xiang990293")
