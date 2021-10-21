
https://www.youtube.com/watch?v=lC0jzd8sGIA
https://www.youtube.com/watch?v=nrggIRWK6qo
https://www.youtube.com/watch?v=Ktrm2rmttm0
https://www.youtube.com/watch?v=3F8nHBKTKdc
https://www.youtube.com/watch?v=igk3H2DWz7k



BDD = describes overall behaviors of the system, customer focused
ATDD = acceptance test driven development
defines tests which act as requirements for the system, development focused

Gherkin = plain language way of describing a test case
* non-technical
* human readable
* helps enforce firm, unambiguous requirements

Gherkin keywords
* Given = precondition
 * And = precondition
* When = action
 * And = action
 * And = action
* Then result
 * And = action
 * And = action

* each test should always end with a Then

Cucumber?

Open source tool for test automation
Tests are written in gherkin
uses regex to match gherkin to cucumber setup
cucumber step is what wraps the automation code

Feature file

* contains multiple scenarios
* each scenarios contain multiple steps

Example...

``
Given I am on the home pag
when I login as "gherkin_test"
And I navigate to the "My Account" page
And I click on the "My Lists" element on the "My Account" Page
Then I should be on the "My Lists" Page
``

Gherkin: Backgrounds
