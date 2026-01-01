# AreaProperties.getCentroidMomentsOfInertia Method

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Method that returns the moments of inertia about the centroid. Unit for returned values is kg\*cm^2.

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
| ixx | double | Output Double that returns the XX partial moment. |
| iyy | double | Output Double that returns the YY partial moment. |
| izz | double | Output Double that returns the ZZ partial moment. |
| ixy | double | Output Double that returns the XY partial moment. |
| iyz | double | Output Double that returns the YZ partial moment. |
| ixz | double | Output Double that returns the XZ partial moment. |

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