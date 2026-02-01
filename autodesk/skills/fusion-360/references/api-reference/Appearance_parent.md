# Appearance.parent Property

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

Property that returns the Parent object of this Appearance (a MaterialLibrary, Design, or AppearanceFavorites collection).

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an Appearance object. |

"appearance\_var" is a variable referencing an Appearance object. ```` ``` #include <Core/Materials/Appearance.h>  // Get the value of the property. Ptr<Base> propertyValue = appearance_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |