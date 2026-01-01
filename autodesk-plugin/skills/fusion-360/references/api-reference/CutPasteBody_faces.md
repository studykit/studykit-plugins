# CutPasteBody.faces Property

Parent Object: [CutPasteBody](CutPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBody.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBody\_var" is a variable referencing a CutPasteBody object.  ```` ``` # Get the value of the property. propertyValue = cutPasteBody_var.faces ``` ```` |

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. ```` ``` #include <Fusion/Features/CutPasteBody.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = cutPasteBody_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |