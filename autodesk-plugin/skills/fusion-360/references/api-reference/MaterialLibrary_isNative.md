# MaterialLibrary.isNative Property

Parent Object: [MaterialLibrary](MaterialLibrary.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibrary.h>

## Description

Gets if this is a native material library. Native libraries are those that are delivered with Fusion and are always available. And non-native libraries are user created. If This returns True then there are some limitations to what can be done with the library. For example, if this is a native material library it cannot be unloaded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. |

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. ```` ``` #include <Core/Materials/MaterialLibrary.h>  // Get the value of the property. boolean propertyValue = materialLibrary_var->isNative(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |