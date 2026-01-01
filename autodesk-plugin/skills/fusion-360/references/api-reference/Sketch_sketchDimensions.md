# Sketch.sketchDimensions Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the sketch dimensions collection associated with this sketch. This provides access to the existing sketch dimensions and supports the creation of new sketch dimensions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<SketchDimensions> propertyValue = sketch_var->sketchDimensions(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDimensions](SketchDimensions.htm).

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