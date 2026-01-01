# Component.constructionPlanes Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the construction planes collection associated with this component. This provides access to the existing construction planes and supports the creation of new construction planes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<ConstructionPlanes> propertyValue = component_var->constructionPlanes(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPlanes](ConstructionPlanes.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |