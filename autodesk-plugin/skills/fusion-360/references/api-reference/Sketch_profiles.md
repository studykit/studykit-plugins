# Sketch.profiles Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the profiles currently computed for the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<Profiles> propertyValue = sketch_var->profiles(); ``` ```` |

## Property Value

This is a read only property whose value is a [Profiles](Profiles.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |