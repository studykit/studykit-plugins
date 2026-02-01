# Sketch.copy Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Copies the specified sketch entities, applying the specified transform. Any geometric or dimension constraints associated with the entities will automatically be copied, if possible. For example, if there is a horizontal dimension and the transform defines a rotation then it will not be included in the result. This same behavior can be seen when performing a copy/paste operation in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.  ```` ``` #include <Fusion/Sketch/Sketch.h>  // Uses no optional arguments. returnValue = sketch_var->copy(sketchEntities, transform);  // Uses optional arguments. returnValue = sketch_var->copy(sketchEntities, transform, targetSketch); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the new sketch entities that were created as a result of the copy. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchEntities | [ObjectCollection](ObjectCollection.htm) | The collection of sketch entities to copy. They must all exist in this sketch. |
| transform | [Matrix3D](Matrix3D.htm) | The transform to apply to the copied entities. |
| targetSketch | [Sketch](Sketch.htm) | Optionally specifies the sketch to copy the entities to. If not provided the entities are copied to this sketch.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |