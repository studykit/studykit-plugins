# SketchDimensions.addOffsetDimension Method

Parent Object: [SketchDimensions](SketchDimensions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensions.h>

## Description

Creates a new linear dimension constraint between the two input entities. The first input entity must be a sketch line. The second entity can be a point or a line that is parallel to the first. The dimension controls the distance as measured perpendicular to the first input line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.  ```` ``` #include <Fusion/Sketch/SketchDimensions.h>  // Uses no optional arguments. returnValue = sketchDimensions_var->addOffsetDimension(line, entityTwo, textPoint);  // Uses optional arguments. returnValue = sketchDimensions_var->addOffsetDimension(line, entityTwo, textPoint, isDriving); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchOffsetDimension](SketchOffsetDimension.htm) | Returns the newly created dimension or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The SketchLine to dimension to. |
| entityTwo | [SketchEntity](SketchEntity.htm) | The parallel SketchLine or SketchPoint to dimension to. If a SketchLine is used it must be parallel to the first line. |
| textPoint | [Point3D](Point3D.htm) | A Point3D object that defines the position of the dimension text. |
| isDriving | boolean | Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchDimensions.addOffsetDimension](SketchDimension_addOffsetDimension_Sample.htm) | Demonstrates the SketchDimension.addOffsetDimension method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |