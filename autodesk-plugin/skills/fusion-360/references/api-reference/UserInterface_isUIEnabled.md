# UserInterface.isUIEnabled Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets and sets if the Fusion user interface is enabled or not. By default it is enabled allowing the user to interact with Fusion. When set to false, the UI is disabled which blocks all interaction, including running commands, manipulating the view and interacting with the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. boolean propertyValue = userInterface_var->isUIEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = userInterface_var->isUIEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |