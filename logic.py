# @nissmogt asked: "What is the logic basis of argumentation?"
# Copilot said: "The logic basis of argumentation is the
#                       principle of non-contradiction and the principle of excluded middle."
# ChatGPT said: Some of the key principles and
#                       rules of logic
#                       that form the basis of argumentation
#               include the following:
#
# The principle of non-contradiction: This principle states that a statement cannot be both true and false at the
# same time and in the same way. In other words, if a statement is true, it cannot be false, and vice versa. This
# principle is often used to evaluate the consistency and coherence of arguments. Define a function based on
# non-contradiction
def non_contradiction(statement1, statement2):
    if statement1 == statement2:
        return True
    else:
        return False


#
# The principle of excluded middle: This principle states that every statement is either true or false,
# and that there is no middle ground or third option. In other words, every statement must be either true or false,
# and it cannot be both true and false at the same time and in the same way. This principle is often used to evaluate
# the completeness and exhaustiveness of arguments. Define a function based on excluded middle
def excluded_middle(statement):
    if statement:
        return True
    else:
        return False
#
# The principle of validity: This principle states that an argument is valid if and only if the conclusion follows
# logically from the premises. In other words, if the premises of an argument are true, then the conclusion must also
# be true. This principle is often used to evaluate the logical strength and soundness of arguments.


# Define a function based on validity
def validity(premise1, premise2, conclusion):
    if premise1 and premise2:
        return conclusion
    else:
        return False
