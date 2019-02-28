
Feature: Checking search

Scenario: Сheck some text in search results

  Given website "https://www.amazon.com/"
  Then search book "Java"
  Then get info from page
  Then check search value is in names
  Then exit