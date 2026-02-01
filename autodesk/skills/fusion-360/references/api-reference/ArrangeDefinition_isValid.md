# ArrangeDefinition.isValid Property

Parent Object: [ArrangeDefinition](ArrangeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeDefinition.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeDefinition\_var" is a variable referencing an ArrangeDefinition object. |

"arrangeDefinition\_var" is a variable referencing an ArrangeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeDefinition.h>  // Get the value of the property. boolean propertyValue = arrangeDefinition_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |