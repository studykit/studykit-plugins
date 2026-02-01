# Sketch.createSpunProfileInput Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Creates a new SpunProfileInput object that is used to specify the input needed to create a spun profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.createSpunProfileInput(entities, axis) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SpunProfileInput](SpunProfileInput.htm) | Returns the newly created SpunProfileInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entities | Base[] | An array containing the entities (BRepBody or BRepFace) to create a spun profile. |
| axis | [Base](Base.htm) | The axis can be a sketch line, construction axis, or linear edge. The axis must not be perpendicular to the sketch plane. |

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |