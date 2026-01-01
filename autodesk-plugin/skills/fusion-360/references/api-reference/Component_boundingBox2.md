# Component.boundingBox2 Method

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the bounding box of the specified entity types within the component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a [Component](Component.htm) object.```` ``` returnValue = component_var.boundingBox2(entityTypes) ``` ```` |

"component\_var" is a variable referencing a [Component](Component.htm) object. |

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