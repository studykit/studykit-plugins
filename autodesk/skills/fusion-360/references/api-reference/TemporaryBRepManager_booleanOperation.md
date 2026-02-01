# TemporaryBRepManager.booleanOperation Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Performs the specified Boolean operation between the two input bodies. The input bodies need not be solid but can be faces that are combined or trimmed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.booleanOperation(targetBody, toolBody, booleanType) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. If successful, the target body is modified as a result of the Boolean operation. Because of this the targetBody must always be a temporary BRepBody. The toolbody is not modified. This is analogous to a machining operation where you have the target that is being machined and the tool that removes material. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetBody | [BRepBody](BRepBody.htm) | The target body that will be modified as a result of the Boolean operation. |
| toolBody | [BRepBody](BRepBody.htm) | The tool body that will be used to operate on the target body. |
| booleanType | [BooleanTypes](BooleanTypes.htm) | The type of Boolean operation to perform. |

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