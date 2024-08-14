# Created by Татьяна at 14.08.2024
Feature: Open a cart


  Scenario: User can open an empty cart
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown