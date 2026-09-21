from aima.probability import *

T, F = True, False

burglary = BayesNet([
    ('Burglary', '', 0.001),                # Var: Burglary; Parents: None; Probability: 0.001
    ('Earthquake', '', 0.002),              # Var: Earthquake; Parents: None; Probability: 0.002
    ('Alarm', 'Burglary Earthquake',        # Var: Alarm; Parents: Burglary, Earthquake; P(Alarm=True | Burg, Earthq)
     
     {(T, T): 0.95,     # P(Alarm=True | Burglary=True, Earthquake=True)
      (T, F): 0.94,     # P(Alarm=True | Burglary=True, Earthquake=False)
      (F, T): 0.29,     # P(Alarm=True | Burglary=False, Earthquake=True)
      (F, F): 0.001}),  # P(Alarm=True | Burglary=False, Eathquake=False)

    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}), # Var: JohnCalls; Parents: Alarm; P(JohnnyCalls=True | Alarm)
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})  # Var: MaryCalls; Parents: Alarm; P(MaryCalls=True | Alarm)
])


'''
Enumeration_ask(X, evidence, network) calculates P(X | evidence)
'''

'''Prior Distribution: ('Burglary', '', 0.001)'''
print(enumeration_ask('Burglary', dict(), burglary).show_approx()) # with dict(), it asks P(Burglary)

'''P(Burglary | JohnCalls = True, MaryCalls = True)    BUT   only prints the distribution's name: P(Burglary)'''
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary))

'''P(Burglary = True | JohnCalls = True, MaryCalls = True)'''
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary)[T]) #[T] extracts "True" probability

'''P(Burglary = True)'''
print(burglary.variable_node('Burglary').p(T, {}))  # Retreives BayesNode for Burglary, then asss node for P(...)

'''Retrieves Alarm node and asks:  P(Alarm = True | Burglary = True, Earthquake = False)'''
print(burglary.variable_node('Alarm').p(T, {'Burglary': T, 'Earthquake': F}))

