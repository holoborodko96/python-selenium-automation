# Created by Татьяна at 14.08.2024
Feature: Navigation to Sign In form

  Scenario: Logged out user can navigate to Sign In
    Given Open page target.com
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened