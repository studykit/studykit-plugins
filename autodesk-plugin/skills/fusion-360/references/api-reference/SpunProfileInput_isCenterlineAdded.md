# SpunProfileInput.isCenterlineAdded Property

Parent Object: [SpunProfileInput](SpunProfileInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SpunProfileInput.h>

## Description

Gets and sets whether a resulting spun profile that would be open, will be closed along the axis of rotation. This closes the sketch so it is ready for further design operations, like revolving the sketch for example. Defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. |

"spunProfileInput\_var" is a variable referencing a SpunProfileInput object. ```` ``` #include <Fusion/Sketch/SpunProfileInput.h>  // Get the value of the property. boolean propertyValue = spunProfileInput_var->isCenterlineAdded();  // Set the value of the property, where value_var is a boolean. bool returnValue = spunProfileInput_var->isCenterlineAdded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |