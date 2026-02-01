# ImageCommandInput.isVisible Property

Parent Object: [ImageCommandInput](ImageCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ImageCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object.  ```` ``` # Get the value of the property. propertyValue = imageCommandInput_var.isVisible  # Set the value of the property. imageCommandInput_var.isVisible = propertyValue ``` ```` |

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. ```` ``` #include <Core/UserInterface/ImageCommandInput.h>  // Get the value of the property. boolean propertyValue = imageCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = imageCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |