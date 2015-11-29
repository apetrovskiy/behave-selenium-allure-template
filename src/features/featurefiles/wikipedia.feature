Feature: Load Wikipedia home

Scenario: Load it
	Given I am not logged in
	When I am on the homepage
	Then I should see the English option

Scenario: Search Cats
	Given I am on the homepage
	When I search cats
	Then I should go to the cats page