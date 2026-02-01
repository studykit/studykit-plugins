# SketchDimensions.addAngularDimension Method

Parent Object: [SketchDimensions](SketchDimensions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensions.h>

## Description

Creates a new angular dimension constraint between the two input lines. The position of the text controls which of the four quadrants will be dimensioned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchDimensions\_var" is a variable referencing a [SketchDimensions](SketchDimensions.htm) object.  ```` ``` #include <Fusion/Sketch/SketchDimensions.h>  // Uses no optional arguments. returnValue = sketchDimensions_var->addAngularDimension(lineOne, lineTwo, textPoint);  // Uses optional arguments. returnValue = sketchDimensions_var->addAngularDimension(lineOne, lineTwo, textPoint, isDriving); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchAngularDimension](SketchAngularDimension.htm) | Returns the newly created dimension or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lineOne | [SketchLine](SketchLine.htm) | The first SketchLine to dimension to. |
| lineTwo | [SketchLine](SketchLine.htm) | The second SketchLine to dimension to. |
| textPoint | [Point3D](Point3D.htm) | A Point3D object that defines the position of the dimension text. The position of the text also defines which quadrant will be dimensioned. |
| isDriving | boolean | Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchDimensions.addAngularDimension](SketchDimension_addAngularDimension_Sample.htm) | Demonstrates the SketchDimension.addAngularDimension method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |