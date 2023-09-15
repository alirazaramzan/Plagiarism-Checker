#creating a plagiarism checker

def plagiarism_checker(text1, text2):
  """
  This function checks for plagiarism between two texts.

  Args:
    text1: The first text.
    text2: The second text.

  Returns:
    The percentage of plagiarism between the two texts.
  """

  # Create a set of all the words in the first text.
  words1 = set(text1.split())

  # Create a set of all the words in the second text.
  words2 = set(text2.split())

  # Find the intersection of the two sets.
  intersection = words1 & words2

  # Calculate the percentage of plagiarism.
  plagiarism_percentage = len(intersection) / len(words1) * 100

  return plagiarism_percentage


if __name__ == "__main__":
  # Get the two texts to be checked.
  text1 = input("Enter the text 1: ")
  text2 = input("Enter the text2: ")

  # Check for plagiarism.
  plagiarism_percentage = plagiarism_checker(text1, text2)

  # Print the percentage of plagiarism.
  print("The percentage of plagiarism is:", plagiarism_percentage, "%")
