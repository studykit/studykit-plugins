# Material.description Property

Parent Object: [Material](Material.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

Gets and sets the description associated with this material. Setting the description is only valid for materials in a document or the favorites list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"material\_var" is a variable referencing a Material object. |

"material\_var" is a variable referencing a Material object. ```` ``` #include <Core/Materials/Material.h>  // Get the value of the property. string propertyValue = material_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = material_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |