# BooleanProperty.isValid Property

Parent Object: [BooleanProperty](BooleanProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/BooleanProperty.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanProperty\_var" is a variable referencing a BooleanProperty object. |

"booleanProperty\_var" is a variable referencing a BooleanProperty object. ```` ``` #include <Core/Application/BooleanProperty.h>  // Get the value of the property. boolean propertyValue = booleanProperty_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |