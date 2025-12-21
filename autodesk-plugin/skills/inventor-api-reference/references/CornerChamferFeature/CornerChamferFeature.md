# CornerChamferFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The CornerChamferFeature object represents a sheet metal corner chamfer feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CornerChamferFeature/CornerChamferFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CornerChamferFeature/CornerChamferFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CornerChamferFeature/CornerChamferFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CornerChamferFeature/CornerChamferFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CornerChamferFeature/CornerChamferFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CornerChamferFeature/CornerChamferFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../CornerChamferFeature/CornerChamferFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CornerChamferFeature/CornerChamferFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CornerChamferFeature/CornerChamferFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CornerChamferFeature/CornerChamferFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CornerChamferFeature/CornerChamferFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CornerChamferFeature/CornerChamferFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../CornerChamferFeature/CornerChamferFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../CornerChamferFeature/CornerChamferFeature_Definition.md) | Property that gets the CornerChamferDefinition object associated with this fold feature. |
| [ExtendedName](../CornerChamferFeature/CornerChamferFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../CornerChamferFeature/CornerChamferFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CornerChamferFeature/CornerChamferFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../CornerChamferFeature/CornerChamferFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CornerChamferFeature/CornerChamferFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CornerChamferFeature/CornerChamferFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../CornerChamferFeature/CornerChamferFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CornerChamferFeature/CornerChamferFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CornerChamferFeature/CornerChamferFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CornerChamferFeature/CornerChamferFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../CornerChamferFeature/CornerChamferFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CornerChamferFeature/CornerChamferFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../CornerChamferFeature/CornerChamferFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CornerChamferFeature/CornerChamferFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CornerChamferFeature/CornerChamferFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CornerChamferDefinition.Parent](../CornerChamferDefinition/CornerChamferDefinition_Parent.md), [CornerChamferFeatures.Add](../CornerChamferFeatures/CornerChamferFeatures_Add.md), [CornerChamferFeatures.Item](../CornerChamferFeatures/CornerChamferFeatures_Item.md)

## Derived Classes

[CornerChamferFeatureProxy](../CornerChamferFeatureProxy/CornerChamferFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |