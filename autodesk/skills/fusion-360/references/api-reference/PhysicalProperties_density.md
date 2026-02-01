# PhysicalProperties.density Property

Parent Object: [PhysicalProperties](PhysicalProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/PhysicalProperties.h>

## Description

Gets the density in kilograms per cubic centimeter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. |

"physicalProperties\_var" is a variable referencing a PhysicalProperties object. ```` ``` #include <Fusion/Fusion/PhysicalProperties.h>  // Get the value of the property. double propertyValue = physicalProperties_var->density(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Get Physical Properties API Sample](GetPhysicalProperties_Sample.htm) | Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |