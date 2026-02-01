# GroupCommandInput.isVisible Property

Parent Object: [GroupCommandInput](GroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/GroupCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object.  ```` ``` # Get the value of the property. propertyValue = groupCommandInput_var.isVisible  # Set the value of the property. groupCommandInput_var.isVisible = propertyValue ``` ```` |

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object. ```` ``` #include <Core/UserInterface/GroupCommandInput.h>  // Get the value of the property. boolean propertyValue = groupCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = groupCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |