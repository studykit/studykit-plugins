# RipFeature.setByFace Method

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

This input method is for creating a rip from a face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object.```` ``` returnValue = ripFeature_var.setByFace(face) ``` ```` |

"ripFeature\_var" is a variable referencing a [RipFeature](RipFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the rip definition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [BRepFace](BRepFace.htm) | The sheet metal face that defines the rip. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |