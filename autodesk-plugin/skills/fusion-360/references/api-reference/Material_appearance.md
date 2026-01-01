# Material.appearance Property

Parent Object: [Material](Material.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

Gets the Appearance of this material.

## Syntax

* [Python](#Python)
* [C++](#C++)

"material\_var" is a variable referencing a Material object. |

"material\_var" is a variable referencing a Material object. ```` ``` #include <Core/Materials/Material.h>  // Get the value of the property. Ptr<Appearance> propertyValue = material_var->appearance(); ``` ```` |

## Property Value

This is a read only property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |