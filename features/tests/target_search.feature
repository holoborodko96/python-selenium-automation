# Created by Татьяна at 14.08.2024
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page
    When Search for 'coffe'
    Then Verify search results are shown