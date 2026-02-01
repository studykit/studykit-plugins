# BRepBodyDefinition.createBody Method

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

Attempts to create a temporary BRepBody object using the definition provided by this BRepBodyDefinition object. Properties on this BRepBodyDefinition are used to define some of the criteria that control how the body is created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a [BRepBodyDefinition](BRepBodyDefinition.htm) object.```` ``` returnValue = bRepBodyDefinition_var.createBody() ``` ```` |

"bRepBodyDefinition\_var" is a variable referencing a [BRepBodyDefinition](BRepBodyDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the newly created BRepBody object if successful, otherwise null is returned. Information about the body creation can be obtained by using the outcomeInfo property. The outcom info is especially useful when initially writing and debugging your code to understand why the creation of the body is failing. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |