# ShellFeature.faces Property

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a ShellFeature object.  ```` ``` # Get the value of the property. propertyValue = shellFeature_var.faces ``` ```` |

"shellFeature\_var" is a variable referencing a ShellFeature object. ```` ``` #include <Fusion/Features/ShellFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = shellFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |