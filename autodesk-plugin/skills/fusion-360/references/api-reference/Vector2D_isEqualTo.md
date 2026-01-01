# Vector2D.isEqualTo Method

Parent Object: [Vector2D](Vector2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector2D.h>

## Description

Compare this vector with another to check for equality.

## Syntax

* [Python](#Python)
* [C++](#C++)

"vector2D\_var" is a variable referencing a [Vector2D](Vector2D.htm) object.```` ``` returnValue = vector2D_var.isEqualTo(vector) ``` ```` |

"vector2D\_var" is a variable referencing a [Vector2D](Vector2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the vectors are equal. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vector | [Vector2D](Vector2D.htm) | The vector to compare with for equality. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |