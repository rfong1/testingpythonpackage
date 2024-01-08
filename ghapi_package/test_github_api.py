import pytest
import github_api

def test_top_gitrepo():
  '''
  This script will test the output of the github_api function.

  Since the output of github_api is a list of a number (defined 
  by a user) of github repos sorted by highest fork count to lowest,
  the tester will need to edit the values for 'inputs' and 'expected_output'
  parameters. This editing is necessary because the outputted list of
  github repositories from github_api is dynamic and always updating
  as more users fork more repositories; therefore, the value obtained
  from the github_api will change from minute to minute.
  
  This test will then determine if the length of the 'actual_output'
  and the 'expected_output' lists are the same.
  

  Parameters
  ----------
  inputs : this is the value entered by the function user.
      Default will be 5.
      Tester can edit this.
  expected_outputs : this is the resulting list from github_api.
      When tester runs the github_api function, edit this parameter
      to equal the values in the outputted list from the function.


  Result
  ------
  actual_outputs : this is the resulting list from the test.

  Example
  -------

  import github_api
  github_api.top_gitrepo(5)

  Result:
  ['rdpeng/ProgrammingAssignment2',
  'octocat/Spoon-Knife',
  'tensorflow/tensorflow',
  'github/gitignore',
  'twbs/bootstrap']


  import test_github_api.test_github_api()
    inputs = 5
    expected_output = 
  ['rdpeng/ProgrammingAssignment2',
  'octocat/Spoon-Knife',
  'tensorflow/tensorflow',
  'github/gitignore',
  'twbs/bootstrap']

  Result:
  actual_output is a list
  actual_output == expected_output
  '''

  #Parameters
  inputs = 5  # ensure this value is the same as entered in github_api
  expected_output = ['jtleek/datasharing',
 'octocat/Spoon-Knife',
 'SmartThingsCommunity/SmartThingsPublic',
 'tensorflow/tensorflow',
 'github/gitignore']
    # ensure that this expected list is the same as the github_api output.
    # copy/paste github_api outputted list.

  actual_output = []
  actual_output = github_api.top_gitrepo(inputs)
  assert len(actual_output) ==len(expected_output)

