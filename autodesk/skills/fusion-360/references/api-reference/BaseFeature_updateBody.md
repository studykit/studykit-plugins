# BaseFeature.updateBody Method

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

Update an existing source BRepBody created by this BaseFeature. The input BRepBody definition will be copied into the existing BRepBody.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a [BaseFeature](BaseFeature.htm) object.```` ``` returnValue = baseFeature_var.updateBody(sourceBody, newBody) ``` ```` |

"baseFeature\_var" is a variable referencing a [BaseFeature](BaseFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the body was updated, or false if the update failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceBody | [BRepBody](BRepBody.htm) | The source BRepBody to update. The source bodies of a BaseFeature are only available from the bodies collection of the BaseFeature when the BaseFeature is in edit mode. |
| newBody | [BRepBody](BRepBody.htm) | The BRepBody whose definition will be used to replace the existing source body's definition. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |