"""
Copyright Mykola Rabchevskiy 2021

"""
import random

'''
Available actions:
'''
C = 'C'  # :cautious option
R = 'R'  # :risky    option

print()
print( "Test for naive version of probability based decision making"          )
print()
print( " Decision making: if estimated probability of unwanted consequence"  )
print( " less than THRESHOLD then use risky action else use cautious action:" )
print()

THRESHOLD = 0.1  # :if estimated probability > THESHOLD then decide C else decide R

print( " Threshold: %.3f" % THRESHOLD )
print()

N =  600         # :number of tests
L =  500         # :steps per test

print( " Nuber of tests: %4d" % N )
print( " Steps per test: %4d" % L )

'''
True probability of unwanted consequence:
'''
P = { C:0.01, R: 0.2 }

'''
Estimated probability ranges: 
'''
Pmin = { C:1.0, R:1.0 }
Pmax = { C:0.0, R:0.0 }

random.seed()

def test( n ):
  '''
  Statistics:
  '''
  total    = { C:0, R:0 }
  unwanted = { C:0, R:0 }   

  def probabilityEstimation():
    P = {}
    for action in [ C, R ]: P[action] = unwanted[action]/total[action] if total[action] > 0 else None
    return P
    
  def decision():
    Pe = probabilityEstimation()
    if Pe[R] is None: # Random choice:
      return R if random.random() > 0.5 else C
    else:
      return R if Pe[R] < THRESHOLD else C

  def consequence( action ): 
    total[action] += 1
    # Random consequence based on real probability:
    if random.random() < P[action]: unwanted[action] += 1

  step = 1
  while step <= L:
    action = decision()
    consequence( action ) 
    Pi = probabilityEstimation()
    step += 1

  '''
  # optional print results of n`th test:
  print( 
    " %4d  %s  C: %4d/%-4d %8.6f  R: %4d/%-4d %8.6f" 
    % ( n, action, unwanted[C], total[C], Pi[C], unwanted[R], total[R], Pi[R] ) 
  )
  '''

  '''
  Update ranges of estimated probabilities:
  '''
  Pe = probabilityEstimation()
  for action in [ C, R ]:
    Pmin[ action ] = min( Pmin[ action ], Pe[ action ] )
    Pmax[ action ] = max( Pmax[ action ], Pe[ action ] )

attempt = 1
while attempt <= N: 
 test( attempt )
 attempt += 1
 
print()
for action in [ C, R ]:
  name = { C:'Cautious', R:'Risky' }
  print( 
    " %8s action: True probability of the unwanted consequences %5.3f; Range of probability estimation: %5.3f .. %5.3f ."
    % ( name[ action ], P[ action ], Pmin[ action ], Pmax[ action ] ) 
  )
print()


