# OffsetStartDefinition.create Method

Parent Object: [OffsetStartDefinition](OffsetStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetStartDefinition.h>

## Description

Statically creates a new OffsetStartDefinition object. This is used as input when create a new feature and defining the starting condition.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetStartDefinition](OffsetStartDefinition.htm) | Returns the newly created OffsetStartDefinition object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| offset | [ValueInput](ValueInput.htm) | An input ValueInput objects that defines the offset distance. The offset can be positive or negative. A positive value indicates an offset in the same direction as the z axis of the profile plane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extrudeFeatures.add using setSymmetricExtent](extrudeFeaturesSymmetricExtent_add_Sample.htm) | Demonstrates the extrudeFeatures.add method using the setSymmetricExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |