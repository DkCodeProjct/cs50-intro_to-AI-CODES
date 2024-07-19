#
#   find the probability of a 
#   patient having a disease 
#   given their test results.
#    
#  P(Disease|Test Result) = P(Test Result|Disease)P(Disease)
#                           -------------------------------                                
#                                   P(Test Result)
#
  # #

priorDisease = 0.01 # P(Disease)
liklyHoodPostiv = 0.9 # P(Test Positive|Disease)
liklyHoodNegtiv = 0.1 # P(Test Negative|Disease)
proirNotDisease = 1 - priorDisease


# Marginal likelihood P(Test Positive)
margianlPostiv = (liklyHoodPostiv * priorDisease) + (liklyHoodNegtiv * proirNotDisease)


def bayeseanInference(testResult, proirDisease, liklyhdNegtv, liklyhdPostiv):
    if testResult == 'positive':
        prob  = (liklyhdPostiv * proirDisease) / margianlPostiv
        return prob
    
    else:
        prob = (liklyhdNegtv * proirDisease) / (1 - margianlPostiv)
        return 1 - prob
    

testResult = 'positive'
prob  = bayeseanInference(testResult,priorDisease ,liklyHoodPostiv, liklyHoodPostiv)
print(f"Probability of disease given a {testResult} test result: {prob:.2f}")

