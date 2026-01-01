# RipFeatureInput.setByFace Method

Parent Object: [RipFeatureInput](RipFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureInput.h>

## Description

Specifies the rip feature will be defined by a face..

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object.```` ``` returnValue = ripFeatureInput_var.setByFace(face) ``` ```` |

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the defining the rip is successful. |

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