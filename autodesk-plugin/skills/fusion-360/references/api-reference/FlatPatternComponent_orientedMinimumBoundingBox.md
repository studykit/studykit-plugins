# FlatPatternComponent.orientedMinimumBoundingBox Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns an oriented bounding box that is best oriented to tightly fit all B-Rep bodies in the component. All other geometry types are ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<OrientedBoundingBox3D> propertyValue = flatPatternComponent_var->orientedMinimumBoundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |