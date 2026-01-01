# IntegerProperty.hasLimits Property

Parent Object: [IntegerProperty](IntegerProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IntegerProperty.h>

## Description

Gets the boolean flag that indicates if the value of this property has any limits it must be within to be valid. If True, use the GetLimits method to get the limit values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerProperty\_var" is a variable referencing an IntegerProperty object.  ```` ``` # Get the value of the property. propertyValue = integerProperty_var.hasLimits ``` ```` |

"integerProperty\_var" is a variable referencing an IntegerProperty object. ```` ``` #include <Core/Application/IntegerProperty.h>  // Get the value of the property. boolean propertyValue = integerProperty_var->hasLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |