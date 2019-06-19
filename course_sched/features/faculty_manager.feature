Feature: Faculty Manager

  Scenario: Add faculty to database
     Given we have a form to submit a new faculty member
      When form is submitted
      Then faculty is added to database
  
  Scenario: Delete faculty to database
      Given we have a button to delete faculty
      When we delete a faculty member
      Then the person is removed from database