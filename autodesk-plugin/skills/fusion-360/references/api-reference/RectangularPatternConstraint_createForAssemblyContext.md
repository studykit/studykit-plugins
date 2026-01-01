# RectangularPatternConstraint.createForAssemblyContext Method

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a [RectangularPatternConstraint](RectangularPatternConstraint.htm) object.```` ``` returnValue = rectangularPatternConstraint_var.createForAssemblyContext(occurrence) ``` ```` |

"rectangularPatternConstraint\_var" is a variable referencing a [RectangularPatternConstraint](RectangularPatternConstraint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RectangularPatternConstraint](RectangularPatternConstraint.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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