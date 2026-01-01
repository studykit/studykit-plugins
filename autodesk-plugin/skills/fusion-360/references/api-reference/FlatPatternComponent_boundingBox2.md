# FlatPatternComponent.boundingBox2 Method

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the bounding box of the specified entity types within the component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.```` ``` returnValue = flatPatternComponent_var.boundingBox2(entityTypes) ``` ```` |

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object. |

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