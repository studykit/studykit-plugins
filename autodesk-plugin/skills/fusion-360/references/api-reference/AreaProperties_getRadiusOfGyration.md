# AreaProperties.getRadiusOfGyration Method

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Method that returns the radius of gyration about the principal axes. Unit for returned values is cm.

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
| kxx | double | Output Double that returns the X partial radius of gyration. |
| kyy | double | Output Double that returns the Y partial radius of gyration. |
| kzz | double | Output Double that returns the Z partial radius of gyration. |

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