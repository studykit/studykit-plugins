# CircularPatternConstraint.createForAssemblyContext Method

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a [CircularPatternConstraint](CircularPatternConstraint.htm) object.```` ``` returnValue = circularPatternConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"circularPatternConstraint\_var" is a variable referencing a [CircularPatternConstraint](CircularPatternConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternConstraint](CircularPatternConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |