from pomegranate import * 


condition = DiscreteDistribution({
    "sun" : 0.5,
    "rain" : 0.5
})

transition = ConditionalProbabilityTable([
    ['sun', 'sun', 0.8],
    ['sun', 'rain', 0.2],
    ['rain', 'rain', 0.7],
    ['rain', 'sun', 0.3],
], [condition])

mode = MarkovChain([condition, transition])
print(mode.sample(20))