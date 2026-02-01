# TriangleMeshCalculator.setQuality Method

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

This is a simplified way to set the various settings that control the resulting mesh. When used it automatically adjusts all of the property values appropriately. It does this for the given geometry by computing its bounding box diameter. Then the surface tolerance is calculated as shown below where the meshLOD is the "Level of Detail" and is described in more detail below. The diameter is the bounding box diameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a [TriangleMeshCalculator](TriangleMeshCalculator.htm) object.```` ``` returnValue = triangleMeshCalculator_var.setQuality(triangleMeshQuality) ``` ```` |

"triangleMeshCalculator\_var" is a variable referencing a [TriangleMeshCalculator](TriangleMeshCalculator.htm) object.  ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  returnValue = triangleMeshCalculator_var->setQuality(triangleMeshQuality); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the quality was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| triangleMeshQuality | [TriangleMeshQualityOptions](TriangleMeshQualityOptions.htm) | The mesh quality is specified by using an item from the enum list where the following items result in a corresponding mesh LOD that's used in the equation above.   LowQualityTriangleMesh: 8 NormalQualityTriangleMesh: 11 HighQualityTriangleMesh: 13 VeryHighQualityTriangleMesh: 15 |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |