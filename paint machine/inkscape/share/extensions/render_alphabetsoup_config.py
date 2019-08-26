#!/usr/bin/env python
# Syntax format: (raise your hand if you know lisp :-)
#
# 'state0':  ("file.svg", ( ( ('state1', dx, dy, T-B, L|R),),
#                           ( ('state2', ...), ('state3', ...),),
#                           ( ('state4', ...),),
#                           ) ),
# )
# 
# Translation of the above in CNF:
# state0 -> state1
# state0 -> state2 state3
# state0 -> state4
#
# Semantics at state0:
# Paste subtree image from state1 onto "file.svg".
# Subtree image is translated by (dx, dy) (measured in units, not pixels!). 
# Subtree image is flipped top to bottom if v==1.
# Subtree image is flipped left to right if h==1.
#
# Notes:
# Origin (0,0) is at *upper* left corner.
# For optional reflections, add both reflecting and non-reflecting rules
# For 180 degree rotations, set v = 1, h = 1.
# It helps to have an empty "epsilon" image.
#
# Jan. 16 2002
#    Removed zeros from the end of rules, changed the code to reflect this.
#    Remember to add trailing ',' at ends of lists, especially singletons.
#
# Jan. 20-26 2002
#    Added uppercase.

syntax = {
    'start': ("epsilon.svg", ((('lc', 0,0,0,0),),# start state
                              (('UC', 0,0,0,0),),
                              )),
    # lowercase
    'lc':    ("epsilon.svg", ((('barsym', 0,0,0,0),), #(2096714) (26) 
                              (('lc2', 0,0,0,0),),    #(830)    (19)
                              )),
    # uppercase
    'UC':    ("epsilon.svg", ((('UCb',  0,0,0,0),),   #(2160) (30)
                              (('UCu',  0,-5,0,0),),
                              )), 
    'UCb':   ("epsilon.svg", ((('Bar', 0,0,0,0),),    #(21)  Psi T I KK Phi
                              (('Bar', 0,0,0,1),),    #
                              (('D',   0,0,0,0),),    #(39)  D O Q C G
                              (('D',   0,0,0,1),),    #
                              (('E',   0,0,0,0),),    #(373) E B PL 3 3r 8 S Theta Eth/Dyet
                              (('E',   0,0,0,1),),    #
                              (('F',   0,0,0,0),),    #(84)  F P R
                              (('F',   0,0,0,1),),    #
                              (('H',   0,0,0,0),),    #(8)   H Hblock
                              (('H',   0,0,0,1),),    #
                              (('L',   0,0,0,0),),    #(12)  L J U
                              (('L',   0,0,0,1),),    #
                              (('V',   0,0,0,1),),    #(6)   A V M Delta Forall W
                              (('X',   0,0,0,0),),    #(172) X N M W Sigma NN
                              (('X',   0,0,0,0),),    #(172) X N M W Sigma NN
                              )),
    'UCu':   ("epsilon.svg", ((('UCb', 0,0,1,1),),)),
    # for statistical balancing
    'lc2':   ("epsilon.svg", ((('osym', 0,0,0,0),),   #(40)  o, c, e, ou 
                              (('vsym', 0,0,0,0),),   #(40)  v, w, ^, y
                              (('dsym', 0,0,0,1),),   #(96)  x, z, 7, 2, yogh
                              (('lc3',  0,0,0,0),),   #(928) (5)
                              )),
    'lc3':   ("epsilon.svg", ((('3sym', 0,0,0,0),),   #(40)  epsilon
                              (('ssym', 0,0,0,0),),   #(8)   s
                              (('asym', 0,0,0,0),),   #(880) a 6 9
                              )),
    # symmetry rules
    'barsym':("epsilon.svg", ((('bar', 0,0,0,0),),
                              (('bar', 0,0,0,1),),
                              (('bar', 0,0,1,0),),
                              (('bar', 0,0,1,1),),
                              )),
    '6sym':  ("epsilon.svg", ((('6', 0,0,0,0),),
                              (('6', 0,0,0,1),),
                              (('6', 0,0,1,0),),
                              (('6', 0,0,1,1),),
                              )),
    '3sym':  ("epsilon.svg", ((('3', 0,0,0,0),),
                              (('3', 0,0,0,1),),
                              (('3', 0,0,1,0),),
                              (('3', 0,0,1,1),),
                              )),
    'vsym':  ("epsilon.svg", ((('v', 0,0,0,0),),
                              (('v', 0,0,1,1),),
                              )),
    'osym':  ("epsilon.svg", ((('o', 0,0,0,0),),
                              (('o', 0,0,0,1),),
                              )),
    'ssym':  ("epsilon.svg", ((('s', 0,0,0,0),),
                              (('s', 0,0,0,1),),
                              )),
    'dsym':  ("epsilon.svg", ((('diag', 0,0,0,0), ('diag', 0,0,1,1),),
                              (('diag', 0,0,0,1), ('diag', 0,0,1,0),),
                              (('dstk', 0,0,0,0),),
                              )),
    'dstk':  ("epsilon.svg", ((('stik', 0,4,0,0), ('z',    0,0,1,1),),
                              (('stik', 0,4,0,0), ('x',    0,0,1,1),),
                              (('stik', 0,4,0,1), ('z',    0,0,1,0),),
                              (('stik', 0,4,0,1), ('x',    0,0,1,0),),
                              )),
    'asym':  ("epsilon.svg", ((('abase', 0,0,0,0),),
                              (('abase', 0,0,0,1),),
                              (('abase', 0,0,1,0),),
                              (('abase', 0,0,1,1),),
                              )),
    # epsilon rules
    'diag':  ("epsilon.svg", ((('x',    0,0,0,0),),
                              (('yogh', 0,0,1,1),),
                              (('z',    0,0,0,0),),
                              (('7',    0,0,0,0),),
                              (('2',    0,0,0,0),),
                              )),
    'bar':   ("bar.svg", ((('vert', 0,0,0,0), ('vert', 0,0,1,0),),                 # f l i t j glot.
                          (('k', 0,0,0,0), ('vert', 0,0,0,0), ('vert', 0,0,1,0),), # k
                          (('b', 0,0,0,0), ('vert', 0,0,1,0),),                    # h heng
                          (('n', 0,0,0,0), ('vert', 0,0,1,0),),                    # n m r eng u uu mu
                          (('b1', 0,0,0,0), ('b0', 0,0,1,0),),                     # thorn eject.
                          (('b1', 0,0,0,0), ('n0', 0,0,1,0),),                     # b p q d 
                          (('n1', 0,0,0,0), ('n0', 0,0,1,0),),                     # open-a 
                          )),
    'vert':  ("epsilon.svg", ((('xtnd', 0,0,0,0),),
                              (('srf',  0,0,1,0),),
                              #(('xtnd', 0,0,0,1),),
                              #(('srf',  0,0,1,1),),
                              )),
    'srf':   ("epsilon.svg", ((('lserif', 0,0,0,0),), 
                              (('lserif', 0,0,0,1),),
                              (('serif',  0,0,0,0),),
                              (('tserif', 0,0,0,0),),
                              (('tserif', 0,0,0,1),),
                              )),
    'xtnd':  ("epsilon.svg", ((('cross', 0,0,0,0),), # this needs to be L-R flippable
                              (('cross', 0,0,0,1),),
                              (('l',     0,0,0,0),),
                              (('?',     0,0,0,0),),
                              (('?',     0,0,0,1),),
                              (('idot',  0,0,0,0),),
                              )),
    'loop':  ("epsilon.svg", ((('o0',  5,0,0,1),),  # loop-around elts
                              (('30',  5,0,0,1),),
                              )),
    'elike': ("epsilon.svg", ((('e',   0,0,0,0), ('crv', 0,0,1,0),),
                              (('a',   0,0,0,0), ('crv', 0,0,1,0),),
                              (('crv', 0,0,0,0), ('crv', 0,0,1,0),),
                              )),
    'loop2': ("epsilon.svg", ((('elike', 0,0,0,0),),
                              (('loop', 0,0,0,0),),
                              )),
    'hlike': ("epsilon.svg", ((('h', 0,0,0,0),),    # h-like extensions
                              (('m', 0,0,0,0),),
                              (('crv', 0,0,0,0),),
                              )),
    'crv':   ("epsilon.svg", ((('r', 0,0,0,0),),    # curvy things
                              (('cserif', 0,0,1,0),),
                              )),
    # image rules
    'abase': ("abase.svg",   ((('n0', 0,0,1,0), ('loop2', 0,0,0,0),),
                              (('n0', 0,0,1,0), ('loop2', 0,0,1,0),),
                              (('b0', 0,0,1,0), ('loop2', 0,0,0,0),),
                              (('b0', 0,0,1,0), ('loop2', 0,0,1,0),),
                              )),
    'v':     ("v.svg", ((('vserl', 0,0,0,0), ('vserr', 0,0,0,0),),
                        (('vserl', 0,0,0,0), ('vserr', 0,0,0,0), ('y0', 0,0,0,0),),
                        (('vserl', 0,0,0,0), ('w', 6,0,0,0),),
                        (('vserl', 0,0,0,0), ('w', 6,0,0,0), ('y0', 0,0,0,0),),
                        )),
    'w':     ("v.svg", ((('vserr', 0,0,0,0),),
                        (('vserr', 0,0,0,0), ('y0', 0,0,0,0),),
                        )),
    'y0':    ("epsilon.svg", ((('y', 0,0,0,1),),
                              (('y', 0,0,0,0),),
                              (('gamma', 0,0,0,0),),
                              )),
    'l':     ("l.svg", ((('j',   0,0,0,0),),
                        (('j',   0,0,0,1),),
                        (('srf', 0,-4,1,0),),
                        )),
    'o':     ("o.svg", ((('loop2', 0,0,0,0),),
                        (('loop2', 0,0,1,0),),
                        )),
    'cross': ("cross.svg", ((('t', 0,0,0,0),),
                            (('f0', 0,0,0,0),),
                            )),
    'f':     ("f.svg", ((('j',   0, 0,0,0),),
                        (('j',   0, 0,0,1),),
                        (('srf', 0,-4,1,0),), 
                        )),
    'f0':    ("f.svg", ((('j',   0, 0,0,0),),
                        (('srf', 0,-4,1,0),), 
                        )),
    'idot':  ("idot.svg", ((('serif',  0,0,1,0),),
                           (('lserif', 0,0,1,0),),
                           (('lserif', 0,0,1,1),),
                           )),
    'stik':  ("f.svg", ((('srf',  0,-4,1,0),),
                        #(('srf',  0,-4,1,1),),
                        )),
    '3':     ("3.svg", ((('loop2',  0,0,0,0),),
                        )),
    # uppercase
    # Bar rules
    'X':       ("epsilon.svg", ((('Xtb', 0,0,0,0), ('Xtb', 0,-5,1,1),),
                                (('Xlr', 0,0,0,0), ('Xlr', 0,-5,1,1),),
                                (('Xtb', 0,0,0,0), ('Xtb2', 0,-5,1,1),),
                                (('Xlr', 0,0,0,0), ('Xlr2', 0,-5,1,1),),
                                (('Xtb2', 0,0,0,0), ('Xtb', 0,-5,1,1),),
                                (('Xlr2', 0,0,0,0), ('Xlr', 0,-5,1,1),),
                                )),

    'Xtb':     ("epsilon.svg", ((('Xnw', 0,0,0,0), ('Xne', 0,0,0,0),),
                                (('Xne', 0,0,0,0), ('Xh', 0,0,0,0), ('Lterm2', 0,0,0,0),),
                                (('Xnw', 0,0,0,0), ('Xh', 0,0,0,1), ('Lterm2', 0,0,0,1),),
                                (('Xne', 0,0,0,0), ('Xh', 0,0,0,0), ('Xnw', 0,0,0,0), ('Xh', 0,0,0,1),),
                                )),
    'Xlr':     ("epsilon.svg", ((('Xne', 0,-5,1,1), ('Xnw', 0,0,0,0),),
                                (('Xne', 0,-5,1,1), ('Xvt', 0,0,0,0), ('Xvb', 0,0,0,0),  ('ITSerif', 0.5,0,0,0),),
                                (('Xnw', 0, 0,0,0), ('Xvt', 0,0,0,0), ('Xvt', 0,-5,1,0), ('IBSerif', 0,0,0,0),),
                                (('Xne', 0,-5,1,1), ('Xnw', 0,0,0,0), ('Xvt', 0,0,0,0),  ('Xvb', 0,0,0,0),),
                                )),

    'Xtb2':    ("epsilon.svg", ((('Xne', 0,0,0,0),),
                                (('Xnw', 0,0,0,0),),
                                )),
    'Xlr2':    ("epsilon.svg", ((('Xnw', 0,0,0,0),),
                                (('Xne', 0,-5,1,1),),
                                )),

    'Xne':     ("Xne.svg",),
    'Xnw':     ("Xnw.svg",),
    'Xh':      ("Xh.svg",),
    'Xvt':     ("Xvt.svg",),
    'Xvb':     ("Xvb.svg",),
                

    'Bar':     ("barcap.svg", ((('Bartop', 0,0,0,0), ('Barbot', 0,0,0,0), ('Barmid', 0,0,0,0),),
                            (('Bartop2', 0,0,0,0), ('Barbot2', 0,0,0,0),),
                            )),
    'Bartop':  ("epsilon.svg", ((('ITSerif', 0.5,0,0,0),),
                                (('Tt',      0,  0,0,0),),
                                )),
    'Barbot':  ("epsilon.svg", ((('IBSerif', 0,0,0,0),),
                                (('Tb',      0,0,0,0),),
                                )),
    'Barbot2': ("epsilon.svg", ((('Barbot', 0,0,0,0),),
                                (('Psi',    0,0,0,0),),
                                )),
    'Bartop2': ("epsilon.svg", ((('Bartop', 0, 0,0,0),),
                                (('Psi',    0,-5,1,0),),
                                )),    
    'Barmid':  ("epsilon.svg", ((('Hm', 0,0,0,0), ('Eserif', 0,0,0,0), ('Hm', -7.5,0,0,1), ('Eserif', -7.5,0,0,1),),
                                (('P',  -2.5,3,0,0), ('P', -5, 3,0,1),),
                                (('P',    -5,3,0,1),), #points left
                                )),
    'Psi':     ("epsilon.svg", ((('IBSerif', 0,0,0,0), ('R', -2.5,0,0,0,), ('R', -5,0,0,1,),),
                                )),
    # D / E / F / H / L rules
    'D':     ("epsilon.svg", ((('Dterm', 0,0,0,0), ('Dterm',  0,0,0,1),),
                              (('Dterm', 0,0,0,0), ('Dterm2',  0,0,0,1),),
                              )),
    'E':     ("epsilon.svg", ((('Eterm', 0,0,0,0), ('Eterm',  0,0,0,1),),
                              (('Eterm',  0,0,0,0), ('Eterm2',  0,0,0,1),),
                              (('Eterm2', 0,0,0,1), ('Eterm2',  0,-5,1,0),), # for S
                              )),
    'F':     ("epsilon.svg", ((('Fterm', 0,0,0,0), ('Fterm',  0,0,0,1),),
                              (('Fterm', 0,0,0,0), ('Fterm2',  0,0,0,1),),
                              )),
    'H':     ("epsilon.svg", ((('Hterm', 0,0,0,0), ('Hterm',  0,0,0,1),),
                              (('Hterm', 0,0,0,0), ('Hterm2', 0,0,0,1),),
                              )),
    'L':     ("epsilon.svg", ((('Lterm', 0,0,0,0), ('Lterm',  0,0,0,1),),
                              (('Lterm', 0,0,0,0), ('Lterm2', 0,0,0,1),),
                              )),
    'Dterm': ("epsilon.svg", ((('Barterm', 0,0,0,0), ('Et',      0,0,0,0), ('Eb', 0,0,0,0),),
                              (('O',       0,0,0,0),),
                              )),
    'Dterm2':("epsilon.svg", ((('C',       0,0,0,1),),
                              (('Ltserif', 0,0,0,1), ('Lbserif', 0,0,0,1),),
                              )),
    'Eterm': ("epsilon.svg", ((('Barterm', 0,0,0,0), ('Et', 0,0,0,0), ('Hm', 0,0,0,0), ('Eb', 0,0,0,0),),
                              (('B', 0,0,0,1),),
                              (('O',      0,0,0,0), ('Ocross',  0,0,0,0),),
                              (('Dterm',  0,0,0,0), ('Eserif',  0,0,0,1),),
                              (('Dterm2', 0,0,0,0), ('Eserif',  0,0,0,1),),
                              )),
    'Eterm2':("epsilon.svg", ((('P',     0,0,0,1), ('Lterm2', 0,-5,1,0),),
                              )),
    'Fterm': ("epsilon.svg", ((('Barterm', 0,0,0,0), ('Et', 0,0,0,0), ('Hm', 0,0,0,0), ('IBSerif', 0,0,0,0),),
                              (('Lterm',   0,0,0,0), ('Eserif', 0,0,0,1),),
                              (('P',       0,0,0,1), ('R', 0,0,0,1),), 
                              (('Ltserif', 0,0,0,1), ('R', 0,0,0,1),), 
                              (('Ltserif', 0,0,0,1), ('Rblock', 0,0,0,1),),
                              (('Uterm',   0,0,0,0), ('Ocross', 0,0,0,0),),
                              )),
    'Fterm2':("epsilon.svg", ((('P', 0,0,0,1),),
                              (('Lterm2',  0,0,0,0), ('Eserif', 0,0,0,1),),
                              )),
    'Hterm': ("epsilon.svg", ((('Barterm', 0,0,0,0), ('Hm', 0,0,0,0), ('ITSerif', 0.5,0,0,0), ('IBSerif', 0,0,0,0),),
                              (('R',     0,0,0,1),  ('R',     0,-5,1,1),),
                              )),
    'Hterm2':("epsilon.svg", ((('R',     0,0,0,1),),
                              (('Rblock',0,0,0,1),),
                              )),
    'Lterm': ("epsilon.svg", ((('Barterm', 0,0,0,0), ('Et', 0,0,0,0), ('IBSerif', 0,0,0,0),),
                              (('Uterm',   0,0,0,0),),
                              )),
    'Lterm2':("epsilon.svg", ((('Ltserif', 0,0,0,1),),
                              (('Cserif', 0,-5,1,1),),
                              )),
    'B':     ("epsilon.svg", ((('P', 0,0,0,0), ('P', 0,6,0,0),),)),
    'C':     ("epsilon.svg", ((('Cserif', 0,0,0,0), ('Cserif', 0,-5,1,0),),)),
    'Cserif':("epsilon.svg", (#(('Ctail', 0,0,0,0),), # I just hate the way these look...
                              (('Cblob', 0,0,0,0),),
                              (('Chook', 0,-5,1,0),),
                              (('G',    0,0,0,0),),
                              ),),
    'O':     ("epsilon.svg", ((('Oterm', 0,0,0,0),),
                              (('Q',     0,0,0,1),),
                              (('Qu',    0,0,0,1),),
                              )),
    'Qu':    ("epsilon.svg", ((('Q', 0,-5,1,0),),)),
    'Barterm':("barcap.svg",),
    'Ctail': ("Ctail.svg",),
    'Chook': ("Chook.svg",),
    'Cblob': ("Cblob.svg",),
    'G':     ("G.svg",),
    'Ltserif':("Lt.svg",),
    'Lbserif':("Lb.svg",),
    'Et':    ("Et.svg",),
    'Eb':    ("Eb.svg",),
    'Hm':    ("hcap.svg",),
    'P':     ("P.svg",),
    'Tb':    ("Tb.svg",),
    'Tt':    ("Tt.svg",),
    'Ocross':("Ocross.svg",),
    'Oterm': ("ocap.svg",),
    'Q':     ("Q.svg",),
    'R':     ("rcap.svg",      ((('IBSerif', -0.5,0,0,1),),)),
    'Rblock':("Rblock.svg", ((('IBSerif', -0.5,0,0,1),),)),
    'Uterm': ("U.svg",      ((('IBSerif', -0.5,0,0,0),),)),
    'IBSerif':("IBSerif.svg",),
    'ITSerif':("ITSerif.svg",),    
    'Eserif':("Eserif.svg",),
    # V rules
    'V':     ("vcap.svg",       ((('V2', 0,0,0,0),),
                              (('V2', 0,0,0,0), ('Across', 0,0,0,0)),
                              )),
    'V2':    ("epsilon.svg", ((('M', 0,0,0,0),),
                              (('Delta', 0,0,0,0),),
                              (('Vser',  0,0,0,0),),
                              )),
    'M':     ("mcap.svg", ((('IBSerif', -1.5,0,0,0), ('IBSerif', 1.5,0,0,1),),)),
    'Delta': ("Delta.svg",),
    'Vser':  ("Vser.svg",),
    'Across':("acap.svg",),
    # single daughter rules
    'b':     ("b.svg", ((('hlike', 0,0,0,0), ('f', 0,0,0,0),),
                        #(('hlike', 0,0,0,0), ('f', 0,0,0,1),),
                        )),
    'b1':    ("b.svg", ((('loop', 0,0,0,0), ('f', 0,0,0,0),),
                        #(('loop', 0,0,0,0), ('f', 0,0,0,1),),
                       )),
    'b0':    ("b.svg", ((('f', 0,0,0,0),),
                        #(('f', 0,0,0,1),),
                        )),
    'h':     ("h.svg", ((('vert', 5,0,1,0),),)),
    'm':     ("m.svg", ((('h',   5,0,0,0), ('vert', 5,0,1,0),),)),# change later to allow 3 humped m
    'n':     ("n.svg", ((('hlike', 0,0,0,0),),)),
    'n1':    ("n.svg", ((('loop', 0,0,0,0),),)),
    's':     ("s.svg", ((('crv',   0,0,0,0), ('crv',   5,0,1,1),),)),
    'j':     ("j.svg", ((('crv',   0,-5,0,0),),)), 
    '?':     ("question.svg", ((('crv', -2.5,-5,0,0),),)),
    'yogh':  ("yogh.svg",((('crv', -2.5,4,1,0),),)),
    #terminal rules
    '2':     ("2.svg",),
    '30':    ("3.svg",),
    '7':     ("7.svg",),    
    'a':     ("a.svg",),
    'cserif':("cserif.svg",), 
    'e':     ("e.svg",),
    'k':     ("k.svg",),
    'n0':    ("n.svg",),
    'o0':    ("o.svg",),
    'r':     ("r.svg",),
    'serif': ("serif.svg",),
    'tserif':("tserif.svg",),
    'lserif':("lserif.svg",),
    't':     ("t.svg",),
    'x':     ("x.svg",),
    'z':     ("z.svg",),
    'vserl': ("vserl.svg",),
    'vserr': ("vserr.svg",),
    'y':     ("y.svg",),
    'gamma': ("gamma.svg",)
    }

alphabet = {
    # Uppercase fix Y make 2)
    '1':     ("start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Bartop.[.ITSerif.].].Barbot2.[.Barbot.[.IBSerif.].].].].].]",),
    '33':    ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.[.C.|.].Eserif.|.].Eterm.[.O.Ocross.].|.].].].]",),
    '3':     ("start.[.UC.[.UCb.[.E.[.Eterm.[.B.[.P.P.].|.].Eterm.[.Dterm2.[.C.|.].Eserif.|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.[.C.|.].Eserif.|.].Eterm.[.O.Ocross.].|.].].].]",),
    '4':     ("start.[.UC.[.UCu.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm2.[.Rblock.[.IBSerif.|.].|.].|.].].-.|.].].]",),
    '5':     ("start.[.UC.[.UCu.[.UCb.[.E.[.Eterm.[.Dterm2.[.Ltserif.|.Lbserif.|.].Eserif.|.].Eterm2.[.P.|.Lterm2.[.Ltserif.|.].-.].|.].|.].-.|.].].]",),
    '6':     ("start.[.UC.[.UCu.[.UCb.[.E.[.Eterm.[.Dterm.[.O.].Eserif.|.].Eterm2.[.P.|.Lterm2.-.].|.].|.].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.E.[.Eterm.[.O.Ocross.].Eterm2.[.P.|.Lterm2.-.].|.].|.].-.|.].].]",),
    '7':     ("start.[.UC.[.UCb.[.X.[.Xtb.[.Xne.Xh.Lterm2.[.Ltserif.|.].].Xtb2.[.Xne.].-.|.].].].]",),
    '8':     ("start.[.UC.[.UCb.[.E.[.Eterm.[.B.[.P.P.].|.].Eterm.[.B.[.P.P.].|.].|.].].].]",),
    '9':     ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm.[.O.].Eserif.|.].Eterm2.[.P.|.Lterm2.-.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.O.Ocross.].Eterm2.[.P.|.Lterm2.-.].|.].|.].].]",),
    '0':     ("start.[.UC.[.UCb.[.D.[.Dterm.[.O.].Dterm.[.O.].|.].].].]",),
    'A':     ("start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Barterm.Et.Hm.IBSerif.].|.].].].]", # no flip needed 
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].|.].].].]", 
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].|.].|.].].]", 
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Uterm.[.IBSerif.].Ocross.].|.].].].]",       
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Uterm.[.IBSerif.].Ocross.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].Fterm.[.Uterm.[.IBSerif.].Ocross.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm.[.Uterm.[.IBSerif.].Ocross.].|.].].].]",
              "start.[.UC.[.UCu.[.UCb.[.V.[.V2.[.Vser.].Across.].|.].-.|.].].]",),
    'B':     ("start.[.UC.[.UCb.[.E.[.Eterm.[.B.[.P.P.].|.].Eterm.|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm.Eserif.|.].Eterm.[.B.[.P.P.].|.].|.].].].]",),
    'Be':    ("start.[.UC.[.UCu.[.UCb.[.E.[.Eterm.[.Barterm.Et.Hm.Eb.].Eterm2.[.P.|.Lterm2.-.].|.].|.].-.|.].].]", #cyrillic
              "start.[.UC.[.UCu.[.UCb.[.E.[.Eterm.[.Dterm.[.Barterm.Et.Eb.].Eserif.|.].Eterm2.[.P.|.Lterm2.-.].|.].|.].-.|.].].]",),
    'C':     ("start.[.UC.[.UCb.[.D.[.Dterm.[.O.[.Oterm.].].Dterm2.[.C.|.].|.].].].]",),
    'D':     ("start.[.UC.[.UCb.[.D.[.Dterm.Dterm.[.O.[.Oterm.].].|.].].].]",
              "start.[.UC.[.UCb.[.D.[.Dterm.[.O.[.Oterm.].].Dterm2.[.Ltserif.|.Lbserif.|.].|.].|.].].].",
              "start.[.UC.[.UCb.[.D.[.Dterm.[.Barterm.Et.Eb.].Dterm.[.Barterm.Et.Eb.].|.].].].]",),
    'Delta': ("start.[.UC.[.UCu.[.UCb.[.V.[.V2.[.Delta.].].|.].-.|.].].]",), #Delta
    'De':    ("start.[.UC.[.UCu.[.UCb.[.D.[.Dterm.[.Barterm.Et.Eb.].Dterm.[.Barterm.Et.Eb.].|.].].-.|.].].]",), #Cyrillic
    'E':     ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.Eserif.|.].Eterm.[.Dterm.[.Barterm.Et.Eb.].Eserif.|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.Eserif.|.].Eterm.[.Dterm.[.O.].Eserif.|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.Eserif.|.].Eterm.[.B.[.P.P.].|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.Eserif.|.].Eterm.[.Barterm.Et.Hm.Eb.].|.].|.].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.O.Ocross.].Eterm.[.Dterm2.Eserif.|.].|.].].].]",),
    'Eth':   ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm.[.O.].Eserif.|.].Eterm.[.Barterm.Et.Hm.Eb.].|.].|.].].]",),
    'F':     ("start.[.UC.[.UCb.[.F.[.Fterm.Fterm2.[.Lterm2.Eserif.|.].|.].].].]",),
    'G':     ("start.[.UC.[.UCb.[.D.[.Dterm.[.O.].Dterm2.[.C.[.Cserif.[.G.].Cserif.-.].|.].|.].].].]",),
    'Gamma': ("start.[.UC.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm2.|.].].].]",), #Gamma
    'H':     ("start.[.UC.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm.[.Barterm.Hm.ITSerif.IBSerif.].|.].].].]",
              "start.[.UC.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm2.[.R.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm2.[.Rblock.[.IBSerif.|.].|.].|.].].].]",),
    'Che':   ("start.[.UC.[.UCu.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm2.[.Rblock.[.IBSerif.|.].|.].|.].].-.|.].].]", #Cyrillic
              "start.[.UC.[.UCu.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm2.[.R.[.IBSerif.|.].|.].|.].].-.|.].].]",),
    'Heng':  ("start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Ltserif.|.R.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm.[.Ltserif.|.Rblock.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm.[.Ltserif.|.R.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm.[.Ltserif.|.Rblock.[.IBSerif.|.].|.].|.].].].]",),
    'I':     ("start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Bartop.[.ITSerif.].].Barbot2.[.Barbot.[.IBSerif.].].].].].]",
              "start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Bartop.[.Tt.].].Barbot2.[.Barbot.[.Tb.].].].].].]",),
    'J':     ("start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Uterm.[.IBSerif.].].Lterm2.|.].].-.|.].].]",),
    'K':     ("start.[.UC.[.UCu.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xnw.].Xlr.[.Xne.-.|.Xvt.Xvb.ITSerif.].-.|.].].-.|.].].]",
              "start.[.UC.[.UCb.[.H.[.Hterm.[.Barterm.Hm.ITSerif.IBSerif.].Hterm.[.R.[.IBSerif.|.].|.R.[.IBSerif.|.].-.|.].|.].].].]",),
    'Zhe':   ("start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Psi.[.IBSerif.R.[.IBSerif.|.].R.[.IBSerif.|.].|.].-.].Barbot2.[.Psi.[.IBSerif.R.[.IBSerif.|.].R.[.IBSerif.|.].|.].].].].].]",), # Cyrillic
    'L':     ("start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm2.|.].|.].-.|.].].]",),
    'Lambda':("start.[.UC.[.UCu.[.UCb.[.V.[.V2.[.Vser.].].|.].-.|.].].]",),# Lambda
    'M':     ("start.[.UC.[.UCu.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xvt.Xvb.ITSerif.].Xlr.[.Xnw.Xvt.Xvt.-.IBSerif.].-.|.].].-.|.].].]",
              "start.[.UC.[.UCb.[.V.[.V2.[.M.[.IBSerif.IBSerif.|.].].].|.].].]",),
    'N':     ("start.[.UC.[.UCu.[.UCb.[.X.[.Xlr.[.Xnw.Xvt.Xvt.-.IBSerif.].Xlr.[.Xnw.Xvt.Xvt.-.IBSerif.].-.|.].].-.|.].].]",
              "start.[.UC.[.UCb.[.L.[.Lterm.[.Uterm.[.IBSerif.].].Lterm.[.Barterm.Et.IBSerif.].|.].|.].].]",),
    'NN':    ("start.[.UC.[.UCu.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xvt.Xvb.ITSerif.].Xlr.[.Xne.-.|.Xvt.Xvb.ITSerif.].-.|.].].-.|.].].]",), # Cyrillic I
    'O':     ("start.[.UC.[.UCb.[.D.[.Dterm.[.O.].Dterm.[.O.].|.].].].]",),
    'P':     ("start.[.UC.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm2.[.P.|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Ltserif.|.R.[.IBSerif.|.].|.].Fterm2.[.P.|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Ltserif.|.Rblock.[.IBSerif.|.].|.].Fterm2.[.P.|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm2.[.P.|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].Fterm2.[.P.|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm2.[.P.|.].|.].].].]",),
    'PL':    ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm.[.Barterm.Et.Eb.].Eserif.|.].Eterm2.[.P.|.Lterm2.-.].|.].].].]",
              "start.[.UC.[.UCb.[.E.[.Eterm.[.Barterm.Et.Hm.Eb.].Eterm2.[.P.|.Lterm2.[.Cserif.-.|.].-.].|.].].].]",),
    'Phi':   ("start.[.UC.[.UCb.[.Bar.[.Bartop.[.ITSerif.].Barbot.[.IBSerif.].Barmid.[.P.P.|.].].].].]",),
    'Pi':    ("start.[.UC.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm.[.Barterm.Et.IBSerif.].|.].].].]",),
    'Psi':   ("start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Psi.[.IBSerif.R.[.IBSerif.|.].R.[.IBSerif.|.].|.].-.].Barbot2.[.Barbot.[.IBSerif.].].].].].]",),
    'Soft':  ("start.[.UC.[.UCu.[.UCb.[.F.[.Fterm.[.Barterm.Et.Hm.IBSerif.].Fterm2.[.P.|.].|.].|.].-.|.].].]",# Cyrillic Yeru/Soft/Hard
              "start.[.UC.[.UCu.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm2.[.P.|.].|.].|.].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.F.[.Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].Fterm2.[.P.|.].|.].|.].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.F.[.Fterm.[.Ltserif.|.Rblock.[.IBSerif.|.].|.].Fterm2.[.P.|.].|.].|.].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm2.[.P.|.].|.].|.].-.|.].].]",),
    'Q':     ("start.[.UC.[.UCb.[.D.[.Dterm.[.O.[.Oterm.].].Dterm.[.O.[.Q.|.].].|.].].].]",),
    'R':     ("start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.P.|.R.[.IBSerif.|.].|.].Fterm.[.Barterm.Et.Hm.IBSerif.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].].].]",),
    'Ya':    ("start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Barterm.Et.IBSerif.].Eserif.|.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Lterm.[.Uterm.[.IBSerif.].].Eserif.|.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].|.].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.P.|.R.[.IBSerif.|.].|.].Fterm.[.Barterm.Et.Hm.IBSerif.].|.].].].]",
              "start.[.UC.[.UCb.[.F.[.Fterm.[.Uterm.[.IBSerif.].Ocross.].Fterm.[.P.|.R.[.IBSerif.|.].|.].|.].|.].].]",),
    'S':     ("start.[.UC.[.UCb.[.E.[.Eterm2.[.P.|.Lterm2.-.].|.Eterm2.[.P.|.Lterm2.-.].-.].|.].].]",),    
    'Sigma': ("start.[.UC.[.UCb.[.X.[.Xtb.[.Xnw.Xh.|.Lterm2.|.].Xtb.[.Xne.Xh.Lterm2.].-.|.].].].]",),
    'T':     ("start.[.UC.[.UCb.[.Bar.[.Bartop2.[.Bartop.[.Tt.].].Barbot2.[.Barbot.[.IBSerif.].].].].].]",
              "start.[.UC.[.UCb.[.Bar.[.Bartop.[.ITSerif.].Barbot.[.IBSerif.].Barmid.[.Hm.Eserif.Hm.|.Eserif.|.].].].].]",),
    'Theta': ("start.[.UC.[.UCb.[.E.[.Eterm.[.O.Ocross.].Eterm.[.O.Ocross.].|.].].].]",),
    'Thorn': ("start.[.UC.[.UCu.[.UCb.[.Bar.[.Bartop.[.ITSerif.].Barbot.[.IBSerif.].Barmid.[.P.|.].].].-.|.].].]",),
    'U':     ("start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm.[.Barterm.Et.IBSerif.].|.].|.].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm.[.Uterm.[.IBSerif.].].|.].].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Uterm.[.IBSerif.].].Lterm.[.Uterm.[.IBSerif.].].|.].].-.|.].].]",
              "start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm.[.Barterm.Et.IBSerif.].|.].].-.|.].].]",),
    'Tse':   ("start.[.UC.[.UCu.[.UCb.[.L.[.Lterm.[.Barterm.Et.IBSerif.].Lterm.[.Barterm.Et.IBSerif.].|.].].-.|.].].]",),# Cyrillic
    'V':     ("start.[.UC.[.UCb.[.V.[.V2.[.Vser.].].|.].].]",),
    'W':     ("start.[.UC.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xvt.Xvb.ITSerif.].Xlr.[.Xnw.Xvt.Xvt.-.IBSerif.].-.|.].].].]",
              "start.[.UC.[.UCu.[.UCb.[.V.[.V2.[.M.[.IBSerif.IBSerif.|.].].].|.].-.|.].].]",),
    'X':     ("start.[.UC.[.UCu.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xnw.].Xlr.[.Xne.-.|.Xnw.].-.|.].].-.|.].].]", 
              "start.[.UC.[.UCb.[.H.[.Hterm.[.R.|.R.-.|.].Hterm.[.R.|.R.-.|.].|.].].].]",),
    'Xi':    ("start.[.UC.[.UCb.[.E.[.Eterm.[.Dterm2.[.Ltserif.|.Lbserif.|.].Eserif.|.].Eterm.[.Dterm2.[.Ltserif.|.Lbserif.|.].Eserif.|.].|.].|.].].]",),
    'Y':     ("start.[.UC.[.UCb.[.X.[.Xlr.[.Xne.-.|.Xnw.].Xlr2.[.Xne.-.|.].-.|.].].].]",),
    'Z':     ("start.[.UC.[.UCb.[.X.[.Xtb.[.Xne.Xh.Lterm2.].Xtb.[.Xne.Xh.Lterm2.].-.|.].].].]",),
    # Lowercase
    'a':    ("start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.n0.-.loop2.[.elike.[.a.crv.-.].].-.].|.].].].].]",
             "start.[.lc.[.barsym.[.bar.[.n1.[.loop.].n0.-.].-.|.].].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.n0.-.loop2.[.loop.].].|.].].].].]",),
    'carat':("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.vserr.].-.|.].].].]",),
    'b':    ("start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.].n0.-.].].].]", 
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.].-.loop2.[.loop.].].-.].].].].]",
             "start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.|.].n0.-.].].].]", 
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.|.].-.loop2.[.loop.].].-.].].].].]",),
    'c':    ("start.[.lc.[.lc2.[.osym.[.o.[.loop2.[.elike.[.crv.-.|.crv.|.].|.].].].].].]",),
    'd':    ("start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.].n0.-.].].|.].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.].-.loop2.[.loop.].].-.].|.].].].]",
             "start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.|.].n0.-.].].|.].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.|.].-.loop2.[.loop.].].-.].|.].].].]",),
    'e':    ("start.[.lc.[.lc2.[.osym.[.o.[.loop2.[.elike.[.e.crv.-.].].].].].].]",
             "start.[.lc.[.lc2.[.lc3.[.3sym.[.3.[.loop2.[.elike.[.crv.crv.-.].].].].].].].]",),
    'epsi': ("start.[.lc.[.lc2.[.lc3.[.3sym.[.3.[.loop2.[.elike.[.crv.crv.-.].].].].].].].]",),
    'f':    ("start.[.lc.[.barsym.[.bar.[.vert.[.xtnd.[.cross.[.f0.[.j.].].].].vert.-.].].].]",),
    'g':    ("start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.[.j.[.crv.].].].n0.-.].-.|.].].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.[.j.].].-.loop2.[.loop.].].-.].-.|.].].].]",),
    'gamma':("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.vserr.y0.[.gamma.].].].].].]",),
    'h':    ("start.[.lc.[.barsym.[.bar.[.b.[.hlike.[.h.].f.].vert.-.].].].]",
             "start.[.lc.[.barsym.[.bar.[.b.[.hlike.[.h.].f.|.].vert.-.].].].]",),
    'heng': ("start.[.lc.[.barsym.[.bar.[.b.[.hlike.[.h.[.vert.[.xtnd.[.l.[.j.[.crv.].].].|.].-.].].f.[.j.[.crv.].].].vert.[.srf.-.|.].-.].].].]",),
    'i':    ("start.[.lc.[.barsym.[.bar.[.vert.vert.[.xtnd.[.idot.].-.].].-.|.].].]",
             "start.[.lc.[.barsym.[.bar.[.vert.vert.[.xtnd.[.idot.].-.].|.].-.|.].].]",),
    'j':    ("start.[.lc.[.barsym.[.bar.[.vert.[.xtnd.[.idot.].-.].vert.[.xtnd.[.l.[.j.].].].|.].-.].].]",),
    'k':    ("start.[.lc.[.barsym.[.bar.[.k.vert.vert.-.].].].]",),
    'l':    ("start.[.lc.[.barsym.[.bar.[.vert.vert.[.xtnd.[.l.].-.].|.].-.|.].].]",
             "start.[.lc.[.barsym.[.bar.[.vert.vert.[.xtnd.[.l.|.].-.].|.].-.|.].].]",),
    'lambda':("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.vserr.y0.].-.|.].].].]",),
    'm':    ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.m.[.h.[.vert.-.].vert.-.].].].vert.-.].].].]",),
    'mu':   ("start.[.lc.[.barsym.[.bar.[.b.[.hlike.[.h.[.vert.-.].].f.].vert.-.].-.|.].].]",),
    'muu':  ("start.[.lc.[.barsym.[.bar.[.b.[.hlike.[.m.[.h.[.vert.-.].vert.-.].].f.].vert.-.|.].-.|.].].]",),
    'n':    ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.h.[.vert.-.].].].vert.-.].].].]",),
    'ng':   ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.h.[.vert.[.xtnd.[.l.[.j.].].|.].-.].].].vert.-.].].].]",),
    'o':    ("start.[.lc.[.lc2.[.osym.[.o.[.loop2.[.loop.[.o0.|.].].].].].].]",),
    'p':    ("start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.].n0.-.].].-.].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.].-.loop2.[.loop.].].-.].-.].].].]",
             "start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.|.].n0.-.].].-.].]",
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.|.].-.loop2.[.loop.].].-.].-.].].].]",),
    'q':    ("start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.].n0.-.].].-.|.].]", 
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.].-.loop2.[.loop.].].-.].-.|.].].].]",
             "start.[.lc.[.barsym.[.bar.[.b1.[.loop.f.|.].n0.-.].].-.|.].]", 
             "start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.|.].-.loop2.[.loop.].].-.].-.|.].].].]",),
    'r':    ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.crv.].].vert.-.].].].]",),
    's':    ("start.[.lc.[.lc2.[.lc3.[.ssym.[.s.[.crv.crv.-.|.].].].].].]",),
    't':    ("start.[.lc.[.barsym.[.bar.[.vert.[.xtnd.[.cross.[.f0.].].].vert.-.].].].]",),
    'u':    ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.h.[.vert.-.].].].vert.-.].-.|.].].]",),
    'uu':   ("start.[.lc.[.barsym.[.bar.[.n.[.hlike.[.m.[.h.[.vert.-.].vert.-.].].].vert.-.].-.|.].].]",),
    'v':    ("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.vserr.].].].].]",),
    'w':    ("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.w.[.vserr.].].].].].]",),
    'x':    ("start.[.lc.[.lc2.[.dsym.[.diag.[.x.].-.diag.[.x.].|.].-.].].]",),
    'y':    ("start.[.lc.[.lc2.[.vsym.[.v.[.vserl.vserr.y0.].].].].]",),
    'yogh': ("start.[.lc.[.lc2.[.dsym.[.diag.[.z.].|.diag.[.yogh.[.crv.-.].-.|.].-.].].].]",),
    'z':    ("start.[.lc.[.lc2.[.dsym.[.diag.[.z.].diag.[.z.].-.|.].|.].].]",),
    'glot': ("start.[.lc.[.barsym.[.bar.[.vert.[.xtnd.[.?.|.].].vert.-.].].].]",),
    '1l':    ("start.[.lc.[.barsym.[.bar.[.vert.[.srf.[.lserif.].].vert.[.srf.[.serif.].-.].|.].].-.].]",),
    '2l':    ("start.[.lc.[.lc2.[.dsym.[.diag.[.2.].diag.[.z.].-.|.].|.].].]",),
    '3l':    ("start.[.lc.[.lc2.[.dsym.[.diag.[.z.].|.diag.[.yogh.[.crv.-.].-.|.].-.].].].]",),
    '6l':    ("start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.[.j.].].-.loop2.[.loop.].-.].-.].].].].]",),
    '7l':    ("start.[.lc.[.lc2.[.dsym.[.diag.[.z.].diag.[.7.].-.|.].|.].].]",),
    '8l':    ("start.[.lc.[.lc2.[.lc3.[.3sym.[.3.[.loop2.[.loop.[.30.|.].].].].].].].]",),
    '9l':    ("start.[.lc.[.lc2.[.lc3.[.asym.[.abase.[.b0.[.f.[.j.].].-.loop2.[.loop.].-.].|.].].].].]",),
    '0l':    ("start.[.lc.[.lc2.[.osym.[.o.[.loop2.[.loop.[.o0.|.].].].].].].]",)
    }

space = 4                                         # number of unit boxes to make a " " space in string
units = 36                                        # pixels per unit box in font
font = "alphabet_soup/"                           # location of font images
    

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 fileencoding=utf-8 textwidth=99
