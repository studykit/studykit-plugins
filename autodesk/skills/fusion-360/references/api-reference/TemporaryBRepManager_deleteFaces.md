# TemporaryBRepManager.deleteFaces Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Deletes one or more faces from a temporary BRepBody. The body that will be modified is determined by getting the parent body of the input faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.deleteFaces(faces, deleteSpecifiedFaces) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| faces | BRepFace[] | An array of BRepFace objects to delete. If more than one face is provided, all of the faces must exist within the same body. |
| deleteSpecifiedFaces | boolean | This allows you to either delete the faces that were input or to keep those faces and delete all the other faces in the body. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |