# Component.orientedMinimumBoundingBox Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns an oriented bounding box that is best oriented to tightly fit all B-Rep bodies in the component. All other geometry types are ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<OrientedBoundingBox3D> propertyValue = component_var->orientedMinimumBoundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |