# SpunProfileInput.flipResult Property

Parent Object: [SpunProfileInput](SpunProfileInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SpunProfileInput.h>

## Description

Gets and sets whether the profile will be created on the opposite side of the axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. |

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. ```` ``` #include <Fusion/Sketch/SpunProfileInput.h>  // Get the value of the property. boolean propertyValue = spunProfileInput_var->flipResult();  // Set the value of the property, where value_var is a boolean. bool returnValue = spunProfileInput_var->flipResult(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |