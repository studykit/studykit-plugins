# Attributes.isValid Property

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an Attributes object. |

"attributes\_var" is a variable referencing an Attributes object. ```` ``` #include <Core/Application/Attributes.h>  // Get the value of the property. boolean propertyValue = attributes_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |