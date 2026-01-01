# BRepFace.appearance Property

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Read-write property that gets and sets the current appearance of the face. Setting this property will result in applying an override appearance to the face and the AppearanceSourceType property will return OverrideAppearanceSource. Setting this property to null will remove any override.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a BRepFace object. |

"bRepFace\_var" is a variable referencing a BRepFace object. ```` ``` #include <Fusion/BRep/BRepFace.h>  // Get the value of the property. Ptr<Appearance> propertyValue = bRepFace_var->appearance();  // Set the value of the property, where value_var is an Appearance. bool returnValue = bRepFace_var->appearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |