# AreaProperties.getPrincipalAxes Method

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Method that returns the principal axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"areaProperties\_var" is a variable referencing an [AreaProperties](AreaProperties.htm) object. |

```` ```  #include <Fusion/Fusion/AreaProperties.h ``` ```` |

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

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample for AreaProperties](AreaPropertiesSample_Sample.htm) | Demonstrates how to use AreaProperties |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |