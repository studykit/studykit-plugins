# BoundingBox3D.create Method

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Creates a transient bounding box object. This object is created statically using the BoundingBox3D.create method.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundingBox3D](BoundingBox3D.htm) | Returns the newly created bounding box or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| minPoint | [Point3D](Point3D.htm) | The point that defines the minimum corner of the bounding box. |
| maxPoint | [Point3D](Point3D.htm) | The point that defines the maximum corner of the bounding box. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |