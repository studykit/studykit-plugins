# MassProperties.XYZMomentsOfInertia Method

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Method that gets the moments of inertia about the reference axis with the center of gravity as origin.

## Syntax

MassProperties.**XYZMomentsOfInertia**( ***Ixx*** As Double, ***Iyy*** As Double, ***Izz*** As Double, ***Ixy*** As Double, ***Iyz*** As Double, ***Ixz*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Ixx | Double | Output Double that returns the XX partial moment. |
| Iyy | Double | Output Double that returns the YY partial moment. |
| Izz | Double | Output Double that returns the ZZ partial moment. |
| Ixy | Double | Output Double that returns the XY partial moment. |
| Iyz | Double | Output Double that returns the YZ partial moment. |
| Ixz | Double | Output Double that returns the XZ partial moment. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mass Properties from Part](../../sample-programs/MassProperties_Sample.md) | This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid. |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |