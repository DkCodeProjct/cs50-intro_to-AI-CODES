from pomegranate import *
from pomegranate.base import Node
from pomegranate import BayesianNetwork

motherGene = Node(DiscreteDistribution({
    '0': 0.4,
    '1': 0.3,
    '2': 0.3,
}), name='mother')

fatherGene = Node(DiscreteDistribution({
    '0': 0.4,
    '1': 0.3,
    '2': 0.3,
}), name='fatherGene')

motherTrait = Node(ConditionalProbabilityTable([
    ['0','yes', 0.5],
    ['0', 'no', 0.5 ],
    ['1','yes', 0.5],
    ['1', 'no', 0.5 ],
    ['2','yes', 0.5],
    ['2', 'no', 0.5 ],
], [motherGene.distribution]), name='motherTrait')

fatherTrait = Node(ConditionalProbabilityTable([
    ['0','yes', 0.5],
    ['0', 'no', 0.5 ],
    ['1','yes', 0.5],
    ['1', 'no', 0.5 ],
    ['2','yes', 0.5],
    ['2', 'no', 0.5 ],
], [fatherGene.distribution]), name='fatherTrait')
childGene = Node(ConditionalProbabilityTable([
    ['0', '0', '0', 0.8],
    ['0', '0', '1', 0.1],
    ['0', '0', '2', 0.1],
    ['0', '1', '0', 0.3],
    ['0', '1', '1', 0.4],
    ['0', '1', '2', 0.3],
    ['0', '2', '0', 0.2],
    ['0', '2', '1', 0.3],
    ['0', '2', '2', 0.5],
    ['1', '0', '0', 0.3],
    ['1', '0', '1', 0.4],
    ['1', '0', '2', 0.3],
    ['1', '1', '0', 0.2],
    ['1', '1', '1', 0.5],
    ['1', '1', '2', 0.3],
    ['1', '2', '0', 0.2],
    ['1', '2', '1', 0.3],
    ['1', '2', '2', 0.5],
    ['2', '0', '0', 0.2],
    ['2', '0', '1', 0.3],
    ['2', '0', '2', 0.5],
    ['2', '1', '0', 0.2],
    ['2', '1', '1', 0.3],
    ['2', '1', '2', 0.5],
    ['2', '2', '0', 0.2],
    ['2', '2', '1', 0.3],
    ['2', '2', '2', 0.5],

], [motherGene.distribution, fatherGene.distribution]), name='childGene')

childTrait = Node(ConditionalProbabilityTable([
    ['0', 'yes', 0.3 ],
    ['0', 'no', 0.7],
    ['1', 'yes', 0.6],
    ['1', 'no', 0.4],
    ['2', 'yes', 0.8],
    ['2', 'no', 0.2]
], [childGene.distribution]), name='childTrait')

model = BayesianNetwork()

model.add_states(motherGene, fatherGene, motherTrait, fatherTrait, childGene, childTrait)

model.add_edge(motherGene, motherTrait)
model.add_edge(fatherGene, fatherTrait)
model.add_edge(motherGene, childGene)
model.add_edge(fatherGene, childGene)

model.add_edge(childGene, childTrait)

model.bake()
sample0 = [['0', '0', 'yes', 'yes', '0', 'yes']]
sample1 = [['1', '1', 'yes', 'yes', '2', 'yes']] 
probability0 = model.probability(sample0)
probability1 = model.probability(sample1)
print(f'Probability_0:, {probability0:.2f}')
print(f'Probability_1:, {probability1:.2f}')
