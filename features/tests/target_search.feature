# Created by iryna at 2/28/2024
Feature: Target.com search tests
  # Enter feature description here

  Scenario: User can search for charger on target
    Given Open Target.com
    When Search for charger
    Then Search results for charger are shown


    Scenario: User can search for headphones
      Given Open Target.com
      When Search for headphones
      Then Search results for headphones are shown