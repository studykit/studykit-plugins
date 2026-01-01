# BRepBody.appearanceSourceType Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Read-write property that gets the source of the appearance for the body. If this returns OverrideAppearanceSource, an override exists on this body. The override can be removed by setting the Appearance property to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object.  ```` ``` # Get the value of the property. propertyValue = bRepBody_var.appearanceSourceType ``` ```` |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. AppearanceSourceTypes propertyValue = bRepBody_var->appearanceSourceType(); ``` ```` |

## Property Value

This is a read only property whose value is an [AppearanceSourceTypes](AppearanceSourceTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |