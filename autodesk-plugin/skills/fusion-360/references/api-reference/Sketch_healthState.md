# Sketch.healthState Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the current health state of this sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. FeatureHealthStates propertyValue = sketch_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Point API Sample](SketchPointSample_Sample.htm) | Demonstrates creating a new sketch point. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |