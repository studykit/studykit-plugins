# FloatProperty.hasMultipleValues Property

Parent Object: [FloatProperty](FloatProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

Gets the boolean flag that indicates if this property has multiple values or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatProperty\_var" is a variable referencing a FloatProperty object.  ```` ``` # Get the value of the property. propertyValue = floatProperty_var.hasMultipleValues ``` ```` |

"floatProperty\_var" is a variable referencing a FloatProperty object. ```` ``` #include <Core/Application/FloatProperty.h>  // Get the value of the property. boolean propertyValue = floatProperty_var->hasMultipleValues(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |