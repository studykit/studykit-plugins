# CornerFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The CornerSeamFeature object represents a sheet metal corner seam feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CornerFeature/CornerFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CornerFeature/CornerFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CornerFeature/CornerFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CornerFeature/CornerFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CornerFeature/CornerFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CornerFeature/CornerFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../CornerFeature/CornerFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CornerFeature/CornerFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CornerFeature/CornerFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CornerFeature/CornerFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CornerFeature/CornerFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CornerFeature/CornerFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../CornerFeature/CornerFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../CornerFeature/CornerFeature_Definition.md) | Property that gets and sets the CornerDefinition object associated with this corner feature. |
| [ExtendedName](../CornerFeature/CornerFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../CornerFeature/CornerFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CornerFeature/CornerFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../CornerFeature/CornerFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CornerFeature/CornerFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CornerFeature/CornerFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../CornerFeature/CornerFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CornerFeature/CornerFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CornerFeature/CornerFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CornerFeature/CornerFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../CornerFeature/CornerFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CornerFeature/CornerFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../CornerFeature/CornerFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CornerFeature/CornerFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CornerFeature/CornerFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CornerDefinition.Parent](../CornerDefinition/CornerDefinition_Parent.md), [CornerFeatures.Add](../CornerFeatures/CornerFeatures_Add.md), [CornerFeatures.Item](../CornerFeatures/CornerFeatures_Item.md)

## Derived Classes

[CornerFeatureProxy](../CornerFeatureProxy/CornerFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |

## Version

Introduced in version 5.3
