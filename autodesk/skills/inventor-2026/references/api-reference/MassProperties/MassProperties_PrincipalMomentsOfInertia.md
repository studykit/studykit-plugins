# MassProperties.PrincipalMomentsOfInertia Method

Parent Object: [MassProperties](../MassProperties/MassProperties.md)

## Description

Property that gets the moments of inertia about the principal axis.

## Syntax

MassProperties.**PrincipalMomentsOfInertia**( ***I1*** As Double, ***I2*** As Double, ***I3*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| I1 | Double | Output Double that specifies the first moment of inertia. |
| I2 | Double | Output Double that specifies the second moment of inertia. |
| I3 | Double | Output Double that specifies the third moment of inertia. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mass Properties from Part](../../sample-programs/MassProperties_Sample.md) | This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid. |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |

## Version

Introduced in version 5
