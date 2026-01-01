# Component.sketches Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the sketches collection associated with this component. This provides access to the existing sketches and supports the creation of new sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<Sketches> propertyValue = component_var->sketches(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketches](Sketches.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
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