Feature: Course Form

  Scenario: Submit new course to database
     Given we have a form to submit a new course
      When form is submitted
      Then course is added to database
  