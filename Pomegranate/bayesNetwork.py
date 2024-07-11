from pomegranate import *
from pomegranate.base import Node
from pomegranate import BayesianNetwork
# Define the distributions
rain = Node(DiscreteDistribution({
    "noRain": 0.7,
    "lightRain": 0.2,
    "heavyRain": 0.1  # Corrected this to ensure the sum is 1
}), name='rain')

# Define the Conditional Probability Table for trackMaintenance
trackMaintenance = Node(ConditionalProbabilityTable([
    ['noRain', "maintenance", 0.4],
    ['noRain', "noMaintenance", 0.6],
    ['lightRain', "maintenance", 0.5],
    ['lightRain', "noMaintenance", 0.5],
    ['heavyRain', "maintenance", 0.3],
    ['heavyRain', "noMaintenance", 0.7]
], [rain.distribution]), name="trackMaintenance")

# Define the Conditional Probability Table for train
train = Node(ConditionalProbabilityTable([
    ['noRain', 'maintenance', 'on time', 0.8],
    ['noRain', 'maintenance', 'delayed', 0.2],
    ['noRain', 'noMaintenance', 'on time', 0.7],
    ['noRain', 'noMaintenance', 'delayed', 0.3],
    ["lightRain", "maintenance", "on time", 0.6],
    ["lightRain", "maintenance", "delayed", 0.4],
    ["lightRain", "noMaintenance", "on time", 0.7],
    ["lightRain", "noMaintenance", "delayed", 0.3],
    ["heavyRain", "maintenance", "on time", 0.4],
    ["heavyRain", "maintenance", "delayed", 0.6],
    ["heavyRain", "noMaintenance", "on time", 0.5],
    ["heavyRain", "noMaintenance", "delayed", 0.5]
], [rain.distribution, trackMaintenance.distribution]), name="train")

# Define the Conditional Probability Table for appointment
appointment = Node(ConditionalProbabilityTable([
    ['on time', 'attend', 0.9],
    ['on time', 'miss', 0.1],
    ['delayed', 'attend', 0.5],
    ['delayed', 'miss', 0.5]
], [train.distribution]), name='appointment')

# Create the Bayesian Network and add states
model = BayesianNetwork()
model.add_states(rain, trackMaintenance, train, appointment)

# Add edges to the model
model.add_edge(rain, trackMaintenance)
model.add_edge(rain, train)
model.add_edge(trackMaintenance, train)
model.add_edge(train, appointment)

# Finalize the model
model.bake()

probability = model.probability([["noRain", "noMaintenance", "on time", "miss"]])
print(f"Probability Of::[noRain, noMaintenance, on time, miss]\n:_{probability}")

predictions = model.predict_proba({
    'train':'delayed'
})

for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f'{node.name}: {prediction}')
    else:
        print(f'{node.name}')
        for val, prob in prediction.parameters[0].items():
            print(f"  ./{val}: {prob:.4f}")
            


