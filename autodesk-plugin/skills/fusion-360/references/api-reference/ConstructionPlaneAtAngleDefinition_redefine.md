# ConstructionPlaneAtAngleDefinition.redefine Method

Parent Object: [ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a [ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm) object.```` ``` returnValue = constructionPlaneAtAngleDefinition_var.redefine(angle, linearEntity, planarEntity) ``` ```` |

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a [ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angle | [ValueInput](ValueInput.htm) | A ValueInput object that defines the angle at which to create the construction plane |
| linearEntity | [Base](Base.htm) | The linear edge, construction line, or sketch line that defines the axis of rotation to measure the angle about |
| planarEntity | [Base](Base.htm) | A plane, planar face or construction plane the angle of the construction plane is measured from |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |