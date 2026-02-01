# Occurrence.boundingBox2 Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the bounding box of the specified entity types within the occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.boundingBox2(entityTypes) ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundingBox3D](BoundingBox3D.htm) | Returns a BoundingBox3D object if the calculation was successful and null in the case where there is no valid geometry and the bounding box is empty. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entityTypes | [BoundingBoxEntityTypes](BoundingBoxEntityTypes.htm) | Bitwise value that specifies the types of entities to include in the calculation of the bounding box. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |