# Component.bRepBodies Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the B-Rep bodies collection associated with this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = component_var->bRepBodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |