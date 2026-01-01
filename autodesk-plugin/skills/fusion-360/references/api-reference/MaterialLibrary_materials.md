# MaterialLibrary.materials Property

Parent Object: [MaterialLibrary](MaterialLibrary.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibrary.h>

## Description

Returns the materials defined within this library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. |

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. ```` ``` #include <Core/Materials/MaterialLibrary.h>  // Get the value of the property. Ptr<Materials> propertyValue = materialLibrary_var->materials(); ``` ```` |

## Property Value

This is a read only property whose value is a [Materials](Materials.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |