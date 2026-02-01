# SpunProfileInput.isAxisProjected Property

Parent Object: [SpunProfileInput](SpunProfileInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SpunProfileInput.h>

## Description

Specifies if the axis will be projected to the sketch plane before making the spun profile. Otherwise, the spun profile will be generated around the axis in space. Defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. |

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. ```` ``` #include <Fusion/Sketch/SpunProfileInput.h>  // Get the value of the property. boolean propertyValue = spunProfileInput_var->isAxisProjected();  // Set the value of the property, where value_var is a boolean. bool returnValue = spunProfileInput_var->isAxisProjected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |