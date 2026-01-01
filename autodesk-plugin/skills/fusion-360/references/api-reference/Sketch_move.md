# Sketch.move Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Moves the specified sketch entities using the specified transform. Transform respects any constraints that would normally prohibit the move.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.move(sketchEntities, transform) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the move was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchEntities | [ObjectCollection](ObjectCollection.htm) | A collection of sketch entities to transform. |
| transform | [Matrix3D](Matrix3D.htm) | The transform that defines the move, rotate or scale. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |