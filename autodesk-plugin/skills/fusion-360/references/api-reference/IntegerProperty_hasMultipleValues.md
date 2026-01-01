# IntegerProperty.hasMultipleValues Property

Parent Object: [IntegerProperty](IntegerProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IntegerProperty.h>

## Description

Gets the boolean flag that indicates if this property has multiple values or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerProperty\_var" is a variable referencing an IntegerProperty object.  ```` ``` # Get the value of the property. propertyValue = integerProperty_var.hasMultipleValues ``` ```` |

"integerProperty\_var" is a variable referencing an IntegerProperty object. ```` ``` #include <Core/Application/IntegerProperty.h>  // Get the value of the property. boolean propertyValue = integerProperty_var->hasMultipleValues(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |