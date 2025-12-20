# SimplifyDefinition Object

## Description

The SimplifyDefinition object represents all of the information that defines a part simplify feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../SimplifyDefinition/SimplifyDefinition_Copy.md) | Method that creates a copy of this SimplifyDefinition object. The new SimplifyDefinition is independent of any SimplifyFeature. It can be edited and used as input to edit an existing SimplifyFeature or to create a new SimplifyFeature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SimplifyDefinition/SimplifyDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [EnvelopeBoundingType](../SimplifyDefinition/SimplifyDefinition_EnvelopeBoundingType.md) | Read-write property that gets and sets envelope bounding type. This is applicable only when the EnvelopesReplaceStyle is not kNoneReplaceStyle. When the definition is just created this is default to kOrthogonalBoundingBox. |
| [EnvelopesReplaceBodies](../SimplifyDefinition/SimplifyDefinition_EnvelopesReplaceBodies.md) | Read-write property that gets and sets bodies that replaced by envelopes. This is applicable only when the EnvelopesReplaceStyle is set to kSelectedBodiesReplaceStyle. |
| [EnvelopesReplaceStyle](../SimplifyDefinition/SimplifyDefinition_EnvelopesReplaceStyle.md) | Read-write property that gets and sets envelopes replace style. When the definition is just created this is default to kNoneReplaceStyle. Valid values are kNoneReplaceStyle, kAllInOneEnvelopeReplaceStyle, kEachBodyReplaceStyle and kSelectedBodiesReplaceStyle. |
| [Parent](../SimplifyDefinition/SimplifyDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PreservedBodies](../SimplifyDefinition/SimplifyDefinition_PreservedBodies.md) | Read-write property that gets and sets the bodies to preserve from removing. |
| [PreservedFeatures](../SimplifyDefinition/SimplifyDefinition_PreservedFeatures.md) | Read-write property that gets and sets the features to preserve from removing. |
| [RemoveBodiesBySize](../SimplifyDefinition/SimplifyDefinition_RemoveBodiesBySize.md) | Read-write property that gets and sets whether remove bodies by size or not. This is applicable when the source document is a part document. This is applicable when the EnvelopesReplaceStyle is not kAllInOneEnvelopeReplaceStyle. |
| [RemoveBodiesSize](../SimplifyDefinition/SimplifyDefinition_RemoveBodiesSize.md) | Read-write property that gets and sets the bounding box diagonal length in centimeters of the bodies being removed. This is applicable when the RemoveBodiesBySize is set to True. |
| [RemoveChamfersMaxDistanceRange](../SimplifyDefinition/SimplifyDefinition_RemoveChamfersMaxDistanceRange.md) | Read-write property that gets and sets the max distance of chamfers in centimeters to remove for the simplify feature. The chamfers which distance is less than or equal to this value will be removed. This is only applicable when the RemoveChamfersStyle is set. |
| [RemoveChamfersStyle](../SimplifyDefinition/SimplifyDefinition_RemoveChamfersStyle.md) | Read-write property that gets and sets the style to remove chamfers for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [RemovedBodies](../SimplifyDefinition/SimplifyDefinition_RemovedBodies.md) | Read-write property that gets and sets the bodies being removed. This is applicable when the RemoveBodiesBySize is set to True. |
| [RemoveEmbossesStyle](../SimplifyDefinition/SimplifyDefinition_RemoveEmbossesStyle.md) | Read-write property that gets and sets the style to remove embosses for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [RemoveEmbossMaxHeightRange](../SimplifyDefinition/SimplifyDefinition_RemoveEmbossMaxHeightRange.md) | Read-write property that gets and sets the max height of embosses in centimeters to remove for the simplify feature. The embosses which height is less than or equal to this value will be removed. This is only applicable when the RemoveEmbossesStyle is set to k. |
| [RemoveFilletsMaxRadiusRange](../SimplifyDefinition/SimplifyDefinition_RemoveFilletsMaxRadiusRange.md) | Read-write property that gets and sets the max radius of fillets in centimeters to remove for the simplify feature. The fillets which radius is less than or equal to this value will be removed. This is only applicable when the RemoveFilletsStyle is set to kSim. |
| [RemoveFilletsStyle](../SimplifyDefinition/SimplifyDefinition_RemoveFilletsStyle.md) | Read-write property that gets and sets the style to remove fillets for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [RemoveHolesMaxDiameterRange](../SimplifyDefinition/SimplifyDefinition_RemoveHolesMaxDiameterRange.md) | Read-write property that gets and sets the max diameter of holes in centimeters to remove for the simplify feature. The holes which diameter is less than or equal to this value will be removed. This is only applicable when the RemoveHolesStyle is set to kSimpl. |
| [RemoveHolesStyle](../SimplifyDefinition/SimplifyDefinition_RemoveHolesStyle.md) | Read-write property that gets and sets the style to remove holes for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [RemoveInternalBodies](../SimplifyDefinition/SimplifyDefinition_RemoveInternalBodies.md) | Read-write property that gets and sets whether internal bodies will be removed or not. This is applicable when the EnvelopesReplaceStyle is not kAllInOneEnvelopeReplaceStyle. |
| [RemoveInternalVoids](../SimplifyDefinition/SimplifyDefinition_RemoveInternalVoids.md) | Read-write property that gets and sets whether remove all the internal voids or not. Set this to True will fill all the internal void shells in the simplified solid. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesRepla. |
| [RemovePocketsMaxDepthRange](../SimplifyDefinition/SimplifyDefinition_RemovePocketsMaxDepthRange.md) | Read-write property that gets and sets the max depth of pockets in centimeters to remove for the simplify feature. The pockets which max depth is less than or equal to this value will be removed. This is only applicable when the RemovePocketsStyle is set to kS. |
| [RemovePocketsStyle](../SimplifyDefinition/SimplifyDefinition_RemovePocketsStyle.md) | Read-write property that gets and sets the style to remove pockets for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [RemoveTunnelsStyle](../SimplifyDefinition/SimplifyDefinition_RemoveTunnelsStyle.md) | Read-write property that gets and sets the style to remove tunnels for the simplify feature. This is applicable when the EnvelopesReplaceStyle is kNoneReplaceStyle or kSelectedBodiesReplaceStyle. |
| [Type](../SimplifyDefinition/SimplifyDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[SimplifyDefinition.Copy](../SimplifyDefinition/SimplifyDefinition_Copy.md), [SimplifyFeature.Definition](../SimplifyFeature/SimplifyFeature_Definition.md), [SimplifyFeatureProxy.Definition](../SimplifyFeatureProxy/SimplifyFeatureProxy_Definition.md), [SimplifyFeatures.CreateDefinition](../SimplifyFeatures/SimplifyFeatures_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Part SimplifyFeature Sample](../../sample-programs/PartSimplifyFeatureSample_Sample.md) | This sample demonstrates how to create a simplify feature in part document. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |