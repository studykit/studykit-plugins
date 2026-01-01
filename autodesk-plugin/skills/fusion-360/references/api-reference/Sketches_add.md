# Sketches.add Method

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Creates a new sketch on the specified planar entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.  ```` ``` #include <Fusion/Sketch/Sketches.h>  // Uses no optional arguments. returnValue = sketches_var->add(planarEntity);  // Uses optional arguments. returnValue = sketches_var->add(planarEntity, occurrenceForCreation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Sketch](Sketch.htm) | Returns the newly created Sketch or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | A construction plane or planar face that defines the sketch plane |
| occurrenceForCreation | [Occurrence](Occurrence.htm) | A creation occurrence is needed if the planarEntity is in another component AND the sketch is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [Sketches.add](Sketches_add_Sample.htm) | Demonstrates the Sketches.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |