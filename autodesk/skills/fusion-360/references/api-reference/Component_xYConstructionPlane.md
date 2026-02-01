# Component.xYConstructionPlane Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the XY origin construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<ConstructionPlane> propertyValue = component_var->xYConstructionPlane(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPlane](ConstructionPlane.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [mirrorFeatures.add](mirrorFeatures_add_Sample.htm) | Demonstrates the mirrorFeatures.add method by mirroring the selected body around the base X-Y construction plane. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [Sketches.add](Sketches_add_Sample.htm) | Demonstrates the Sketches.add method. |
| [Sketches.addToBaseOrFormFeature](Sketches_addToFormBaseOrFeature_Sample.htm) | Demonstrates the Sketches.addToBaseOrFormFeature method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |