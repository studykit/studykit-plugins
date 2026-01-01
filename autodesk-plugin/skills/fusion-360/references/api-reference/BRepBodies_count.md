# BRepBodies.count Property

Parent Object: [BRepBodies](BRepBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodies.h>

## Description

Returns the number of bodies in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodies\_var" is a variable referencing a BRepBodies object. |

"bRepBodies\_var" is a variable referencing a BRepBodies object. ```` ``` #include <Fusion/BRep/BRepBodies.h>  // Get the value of the property. uinteger propertyValue = bRepBodies_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Empty Components](DeleteEmptyComponents_Sample.htm) | Deletes empty components from the active design. |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |