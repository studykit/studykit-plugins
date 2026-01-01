# Attribute.isValid Property

Parent Object: [Attribute](Attribute.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attribute\_var" is a variable referencing an Attribute object. |

"attribute\_var" is a variable referencing an Attribute object. ```` ``` #include <Core/Application/Attribute.h>  // Get the value of the property. boolean propertyValue = attribute_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |