# Created by iryna at 2/9/2024
Feature: Target.com empty cart
  # Enter feature description here

  Scenario: "Your cart is empty" message is displayed
    Given Open Target.com
    When Click on cart icon
    Then Message Your cart is empty is shown


  Scenario: Logged out user can access Sign In
    Given Open Target.com
    When Click Sign In
    When Click from navigation menu on Sign In
    Then Verify Sign In form opened
