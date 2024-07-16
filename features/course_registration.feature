# This is your feature file, put all your scenarios in here
Feature: Registration for the Alten BDD Workshop
	In order NOT to miss exciting new classes
	As an external user
	I want to be able to register for a course


Scenario: first registration
	Given there is a course with 0 registrations
	  And I enter John Doe
	 When I register
	 Then the course has 1 registration

