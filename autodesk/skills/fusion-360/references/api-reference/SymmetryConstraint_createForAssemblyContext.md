# SymmetryConstraint.createForAssemblyContext Method

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a [SymmetryConstraint](SymmetryConstraint.htm) object.```` ``` returnValue = symmetryConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"symmetryConstraint\_var" is a variable referencing a [SymmetryConstraint](SymmetryConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SymmetryConstraint](SymmetryConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |