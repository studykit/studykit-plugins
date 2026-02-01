# PropertyGroup.parent Property

Parent Object: [PropertyGroup](PropertyGroup.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Returns the parent of this group. Typically this will be a Component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroup\_var" is a variable referencing a PropertyGroup object. |

"propertyGroup\_var" is a variable referencing a PropertyGroup object. ```` ``` #include <Core/Application/PropertyGroup.h>  // Get the value of the property. Ptr<Base> propertyValue = propertyGroup_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |