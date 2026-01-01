# AngleValueCommandInput.isVisible Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = angleValueCommandInput_var.isVisible  # Set the value of the property. angleValueCommandInput_var.isVisible = propertyValue ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. boolean propertyValue = angleValueCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = angleValueCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |