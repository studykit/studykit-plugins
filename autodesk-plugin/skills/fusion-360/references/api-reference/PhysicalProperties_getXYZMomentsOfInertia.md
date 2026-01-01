# PhysicalProperties.getXYZMomentsOfInertia Method

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

Method that gets the moment of inertia about the world coordinate system. Unit for returned values is kg\*cm^2.

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
| xx | double | Output Double that returns the XX partial moment. |
| yy | double | Output Double that returns the YY partial moment. |
| zz | double | Output Double that returns the ZZ partial moment. |
| xy | double | Output Double that returns the XY partial moment. |
| yz | double | Output Double that returns the YZ partial moment. |
| xz | double | Output Double that returns the XZ partial moment. |

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