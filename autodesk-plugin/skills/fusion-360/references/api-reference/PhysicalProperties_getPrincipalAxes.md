# PhysicalProperties.getPrincipalAxes Method

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

Method that returns the principal axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"physicalProperties\_var" is a variable referencing a [PhysicalProperties](PhysicalProperties.htm) object. |

```` ```  #include <Fusion/Fusion/PhysicalProperties.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| xAxis | [Vector3D](Vector3D.htm) | The output Vector3D object that indicates the direction of the x axis. |
| yAxis | [Vector3D](Vector3D.htm) | The output Vector3D object that indicates the direction of the y axis. |
| zAxis | [Vector3D](Vector3D.htm) | The output Vector3D object that indicates the direction of the z axis. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Physical Properties API Sample](GetPhysicalProperties_Sample.htm) | Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |