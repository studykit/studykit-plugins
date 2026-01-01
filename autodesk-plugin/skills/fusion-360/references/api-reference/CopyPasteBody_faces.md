# CopyPasteBody.faces Property

Parent Object: [CopyPasteBody](CopyPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBody.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object.  ```` ``` # Get the value of the property. propertyValue = copyPasteBody_var.faces ``` ```` |

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. ```` ``` #include <Fusion/Features/CopyPasteBody.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = copyPasteBody_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |