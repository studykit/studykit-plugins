# MassProperties Object

## Description

The MassProperties object provides access to properties that provide read and write access to various mass property information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AchievedAccuracy](../MassProperties/MassProperties_AchievedAccuracy.md) | Property that gets the actual accuracy achieved while computing the mass property calculations. |
| [PrincipalMomentsOfInertia](../MassProperties/MassProperties_PrincipalMomentsOfInertia.md) | Property that gets the moments of inertia about the principal axis. |
| [RadiusOfGyration](../MassProperties/MassProperties_RadiusOfGyration.md) | Property that gets the radius of gyration about the principal axis. |
| [RotationToPrincipal](../MassProperties/MassProperties_RotationToPrincipal.md) | Gets the rotation from the active edit coordinate system of the target to the principal coordinate system. |
| [XYZMomentsOfInertia](../MassProperties/MassProperties_XYZMomentsOfInertia.md) | Method that gets the moments of inertia about the reference axis with the center of gravity as origin. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Accuracy](../MassProperties/MassProperties_Accuracy.md) | Read-write property that gets/sets the desired level of computational accuracy of the mass property calculations. |
| [Area](../MassProperties/MassProperties_Area.md) | Property that returns the area of the entity. |
| [AvailableAccuracy](../MassProperties/MassProperties_AvailableAccuracy.md) | Indicates the computational accuracy of mass properties calculations. |
| [CacheResultsOnCompute](../MassProperties/MassProperties_CacheResultsOnCompute.md) | Property that deterimines whether mass property calculations are cached with the component. |
| [CenterOfMass](../MassProperties/MassProperties_CenterOfMass.md) | Property that gets the center of mass. |
| [IncludeCosmeticWelds](../MassProperties/MassProperties_IncludeCosmeticWelds.md) | Gets and sets whether cosmetic welds should be included for mass property calculations. |
| [IncludeQuantityOverrides](../MassProperties/MassProperties_IncludeQuantityOverrides.md) | Gets and sets whether BOM quantity overrides should be used for assembly components to perform mass property calculations. |
| [Mass](../MassProperties/MassProperties_Mass.md) | Gets and sets the mass of the model in database units. |
| [MassOverridden](../MassProperties/MassProperties_MassOverridden.md) | Gets and sets whether the mass value is overridden. |
| [Type](../MassProperties/MassProperties_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Volume](../MassProperties/MassProperties_Volume.md) | Gets and sets the volume of the model in database units. |
| [VolumeOverridden](../MassProperties/MassProperties_VolumeOverridden.md) | Gets and sets whether the volume value is overridden. |

## Accessed From

[AssemblyComponentDefinition.MassProperties](../AssemblyComponentDefinition/AssemblyComponentDefinition_MassProperties.md), [ComponentOccurrence.MassProperties](../ComponentOccurrence/ComponentOccurrence_MassProperties.md), [ComponentOccurrenceProxy.MassProperties](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_MassProperties.md), [FlatPattern.MassProperties](../FlatPattern/FlatPattern_MassProperties.md), [PartComponentDefinition.MassProperties](../PartComponentDefinition/PartComponentDefinition_MassProperties.md), [SheetMetalComponentDefinition.MassProperties](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_MassProperties.md), [WeldmentComponentDefinition.MassProperties](../WeldmentComponentDefinition/WeldmentComponentDefinition_MassProperties.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Mass Properties from Part](../../sample-programs/MassProperties_Sample.md) | This sample demonstrates getting mass properties from a part. This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. To run the sample you must have a part document open that contains a solid. |
| [Computing mass properties without dirtying document](../../sample-programs/MassProperties_CacheResultsOnCompute_Sample.md) | This sample demonstrates getting mass properties from a part without dirtying the document (i.e. without caching the computed results in the document). This sample is specific to a part document, but the MassProperties object can also be obtained from an Assembly document and from component occurrences. |

## Version

Introduced in version 5
