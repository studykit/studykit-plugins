# AreaProperties.getPrincipalMomentsOfInertia Method

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Method that returns the moments of inertia about the principal axes. Unit for returned values is kg\*cm^2.

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
| i1 | double | Output Double that specifies the first moment of inertia. |
| i2 | double | Output Double that specifies the second moment of inertia. |
| i3 | double | Output Double that specifies the third moment of inertia. |

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