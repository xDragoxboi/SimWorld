# Agent Conventions and Guidelines

This file outlines the conventions and guidelines for agents working on this project.

## Code Style

* All code should be written in Python 3.
* All code should be formatted using the Black code formatter.
* All code should be documented using Google-style docstrings.

## Project Structure

The project is organized into the following directories:

* `blueprints`: This directory contains the XML files that define the life forms, items, and other objects in the game.
* `docs`: This directory contains the documentation for the project.
* `logs`: This directory contains the log files for the game.
* `src`: This directory contains the source code for the game.
* `tests`: This directory contains the tests for the game.

## Workflow

1. **Create a new branch:** Before you start working on a new feature, create a new branch for your work.
2. **Write your code:** Write your code in the `src` directory.
3. **Write tests:** Write tests for your code in the `tests` directory.
4. **Run the tests:** Run the tests to make sure that your code is working correctly.
5. **Submit a pull request:** When you are finished with your work, submit a pull request to the `main` branch.

## Blueprint System

The game uses a blueprint system that is based on XML files. This allows you to easily create new life forms, items, and other objects without having to write any code.

To create a new blueprint, you will need to create a new XML file in the `blueprints` directory. The XML file should have the following format:

```xml
<blueprint>
  <type>lifeform</type>
  <name>Human</name>
  <attributes>
    <health>100</health>
    <energy>100</energy>
    <size>70</size>
  </attributes>
</blueprint>
```

## Modding

The game is designed to be highly moddable. You can create new life forms, items, and other objects by creating new XML files in the `blueprints` directory. You can also modify the game's code to add new features and functionality.
