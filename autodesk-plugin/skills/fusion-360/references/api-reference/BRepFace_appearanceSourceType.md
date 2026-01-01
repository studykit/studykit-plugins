# BRepFace.appearanceSourceType Property

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Read-write property that gets the source of the appearance for the face. If this returns OverrideAppearanceSource, an override exists on this face. The override can be removed by setting the Appearance property to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a BRepFace object. |

"bRepFace\_var" is a variable referencing a BRepFace object. ```` ``` #include <Fusion/BRep/BRepFace.h>  // Get the value of the property. AppearanceSourceTypes propertyValue = bRepFace_var->appearanceSourceType(); ``` ```` |

## Property Value

This is a read only property whose value is an [AppearanceSourceTypes](AppearanceSourceTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |