# Sketches.addToBaseOrFormFeature Method

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Creates a parametric sketch that is associated with a base feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.```` ``` returnValue = sketches_var.addToBaseOrFormFeature(planarEntity, targetBaseOrFormFeature, includeFaceEdges) ``` ```` |

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.  ```` ``` #include <Fusion/Sketch/Sketches.h>  returnValue = sketches_var->addToBaseOrFormFeature(planarEntity, targetBaseOrFormFeature, includeFaceEdges); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Sketch](Sketch.htm) | Returns the newly created Sketch or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | A construction plane or planar face that defines the sketch plane. |
| targetBaseOrFormFeature | [Base](Base.htm) | The existing base feature that you want to associate this sketch with. |
| includeFaceEdges | boolean | When a BrepFace is used as the planarEntity argument, this defines if the edges of the face should be included in the sketch. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BaseFeature Sample](BaseFeatureSample_Sample.htm) | Creates a new base feature. |
| [Sketches.addToBaseOrFormFeature](Sketches_addToFormBaseOrFeature_Sample.htm) | Demonstrates the Sketches.addToBaseOrFormFeature method. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |