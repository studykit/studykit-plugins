# Occurrence.orientedMinimumBoundingBox Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns an oriented bounding box that is best oriented to tightly fit all B-Rep bodies in the occurrence. All other geometry types are ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<OrientedBoundingBox3D> propertyValue = occurrence_var->orientedMinimumBoundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |