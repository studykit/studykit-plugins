# Material.name Property

Parent Object: [Material](Material.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

Returns the name of this Material. This is the name of the material as seen in the user interface. The name can only be edited if the material is in a Design or the favorites list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"material\_var" is a variable referencing a Material object. |

"material\_var" is a variable referencing a Material object. ```` ``` #include <Core/Materials/Material.h>  // Get the value of the property. string propertyValue = material_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = material_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |