# RipFeatures.CreateRipDefinition Method

Parent Object: [RipFeatures](../RipFeatures/RipFeatures.md)

## Description

Method that creates a new RipDefinition object.

## Remarks

This object is not a rip feature but contains the information that defines a rip feature and can be used to create a new rip feature. The resulting RipDefinition will define a 'Face Extents' rip feature where the entire face defines the extents of the rip. To create a single point or point to point rip definition you can edit the RipDefinition feature.

## Syntax

RipFeatures.**CreateRipDefinition**( ***RipFace*** As [Face](../Face/Face.md) ) As [RipDefinition](../RipDefinition/RipDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RipFace | [Face](../Face/Face.md) | The face that the rip is defined along. This must be a face this is valid for defining a rip extent. For example a face along the edge of the part where the thickness of the part is represented is not valid as input. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |