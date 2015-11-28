Feature: Load Wikipedia home

Scenario: Load it
	Given I am not logged in
	When I am on the homepage
	Then I should see the English option
