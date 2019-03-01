
Feature: Checking search

Scenario: Check some text in search results

  Given website "https://www.amazon.com/"
  Then search book "JAVA"
  Then get info from page
  Then check search value is in names
  Then exit
