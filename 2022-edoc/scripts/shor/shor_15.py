# Adapted from https://bitbucket.csiro.au/projects/QC/repos/qcem/browse

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, BasicAer, execute
from numpy import gcd, log2, pi
from random import randint
from sympy.ntheory.continued_fraction import continued_fraction_periodic

N = 15
z = 1
while z == 1 or z == N:
    a = randint(2, N - 2)
    print("a = %s" % a)
    z = gcd(a, N)
    print("z = %s" % z)
    if z == 1:
        print("Start Quantum Part")
        qr = QuantumRegister(7)
        cr = ClassicalRegister(3)
        qc = QuantumCircuit(qr, cr)

        # make lower register equal to 1
        qc.x(qr[6])

        # prepare uniform superposition on upper register
        qc.h(qr[0])
        qc.h(qr[1])
        qc.h(qr[2])

        # oracle for a = 2
        if a == 2:
            # add 1 for x = 1
            qc.ccx(qr[2], qr[6], qr[5])
            qc.cx(qr[2], qr[6])
            # multiply by 2^2 = 4(mod15) for x=2
            qc.cx(qr[3], qr[5])
            qc.ccx(qr[1], qr[5], qr[3])
            qc.cx(qr[3], qr[5])
            qc.cswap(qr[1], qr[6], qr[4])

        # oracle for a = 4
        if a == 4:
            # add 3 for x = 1
            qc.cx(qr[2], qr[5])
            qc.cx(qr[2], qr[6])

        # oracle for a = 7
        if a == 7:
            # add 6 for x = 1
            qc.cx(qr[2], qr[4])
            qc.cx(qr[2], qr[5])
            # multiply by 7^2 = 4(mod15) for x=2
            qc.cx(qr[3], qr[5])
            qc.ccx(qr[1], qr[5], qr[3])
            qc.cx(qr[3], qr[5])
            qc.cswap(qr[1], qr[6], qr[4])

        # oracle for a = 8
        if a == 8:
            # add 7 for x = 1
            qc.ccx(qr[2], qr[6], qr[3])
            qc.cx(qr[2], qr[6])
            # multiply by 8^2 = 4(mod15) for x=2
            qc.cx(qr[3], qr[5])
            qc.ccx(qr[1], qr[5], qr[3])
            qc.cx(qr[3], qr[5])
            qc.cswap(qr[1], qr[6], qr[4])

        # oracle for a = 11
        if a == 11:
            # add 10 for x = 1
            qc.cx(qr[2], qr[3])
            qc.cx(qr[2], qr[5])

        # oracle for a = 13
        if a == 13:
            # add 12 for x = 1
            qc.cx(qr[2], qr[3])
            qc.cx(qr[2], qr[4])
            # multiply by 13^2 = 4(mod15) for x = 2
            qc.cx(qr[3], qr[5])
            qc.ccx(qr[1], qr[5], qr[3])
            qc.cx(qr[3], qr[5])
            qc.cswap(qr[1], qr[6], qr[4])

        # inverse fourier transform
        qc.h(qr[2])
        qc.cp(pi / 2, qr[2], qr[1])
        qc.h(qr[1])
        qc.cp(pi / 4, qr[2], qr[0])
        qc.cp(pi / 2, qr[1], qr[0])
        qc.h(qr[0])
        qc.swap(qr[2], qr[0])

        qc.measure(qr[0], cr[2])
        qc.measure(qr[1], cr[1])
        qc.measure(qr[2], cr[0])

        # Simulate
        backend = BasicAer.get_backend('qasm_simulator')
        result = execute(qc, backend, shots=20).result()

        # print quantum measurement
        x = result.get_counts()



        # perform classical post processing (runs in polynomial time)
        # outputs the prime factors of N from the period
        print("Start classical post-processing")

        # performs the continued fractions algorithm on the quantum measurement value
        # output should be the continued fraction sequence for x/2^n.
        n = int(log2(N)) + 1
        d = int(max(x, key=x.get), 2)
        print('Measurement: d = {}'.format(d))
        cont_list = continued_fraction_periodic(d, 2 ** n)
        print('cont fraction sequence: %s' % cont_list)

        # find the period based on the continued fractions sequence
        # output should be the period.
        r = 0
        q_list = [1]
        i = 1
        while i < len(cont_list):
            if i == 1:
                q = cont_list[i]
            else:
                q = int(cont_list[i] * q_list[i - 1] + q_list[i - 2])
            q_list.append(q)
            if a ** q % N == 1:
                r = q
                break
            i += 1

        print('Period: r = {}'.format(r))

        if r % 2 == 0 and not r == 0 and r < N-1:
            print('Period is even')
            z = gcd(a ** (r / 2) - 1, N)
            print("z = int(gcd(int(a ** (r / 2) - 1), N)) = %s" % z)
            if z == 1 or z == N:
                print('z=%s' % z)
                z = gcd(a**(r/2) + 1, N)
                print("z = int(gcd(int(a ** (r / 2) + 1), N)) = %s" % z)
                if z == 1 or z == N:
                    print('z=%s; try again')
        else:
            print('Period is uneven; try again')
