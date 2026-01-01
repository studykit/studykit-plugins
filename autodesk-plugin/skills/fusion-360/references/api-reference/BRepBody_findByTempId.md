# BRepBody.findByTempId Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns all of the faces, edges, or vertices that match the input ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.findByTempId(tempId) ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm)[] | Returns an array of entities that have the specified ID. This returns an array because it's possible that a body created by converting a body can have multiple entities with the same ID in the case where a curve or face was split. Returns an empty array in the case where no match is found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tempId | integer | The ID of the B-Rep entity to find. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |