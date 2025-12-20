# MassProperties.RadiusOfGyration Method

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Property that gets the radius of gyration about the principal axis.

## Syntax

MassProperties.**RadiusOfGyration**( ***Kx*** As Double, ***Ky*** As Double, ***Kz*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Kx | Double | Output Double that returns the X partial radius of gyration. |
| Ky | Double | Output Double that returns the Y partial radius of gyration. |
| Kz | Double | Output Double that returns the Z partial radius of gyration. |

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