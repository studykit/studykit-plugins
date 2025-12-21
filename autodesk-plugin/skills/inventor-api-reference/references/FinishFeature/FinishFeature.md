# FinishFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

FinishFeature Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FinishFeature/FinishFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../FinishFeature/FinishFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../FinishFeature/FinishFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../FinishFeature/FinishFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../FinishFeature/FinishFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../FinishFeature/FinishFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../FinishFeature/FinishFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../FinishFeature/FinishFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../FinishFeature/FinishFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../FinishFeature/FinishFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../FinishFeature/FinishFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FinishFeature/FinishFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../FinishFeature/FinishFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../FinishFeature/FinishFeature_Definition.md) | The FinishFeature object represents an existing finish feature in an Inventor document. |
| [ExtendedName](../FinishFeature/FinishFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../FinishFeature/FinishFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../FinishFeature/FinishFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../FinishFeature/FinishFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../FinishFeature/FinishFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../FinishFeature/FinishFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../FinishFeature/FinishFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../FinishFeature/FinishFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../FinishFeature/FinishFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../FinishFeature/FinishFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../FinishFeature/FinishFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../FinishFeature/FinishFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../FinishFeature/FinishFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../FinishFeature/FinishFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../FinishFeature/FinishFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FinishDefinition.Parent](../FinishDefinition/FinishDefinition_Parent.md), [FinishFeatureProxy.NativeObject](../FinishFeatureProxy/FinishFeatureProxy_NativeObject.md), [FinishFeatures.Add](../FinishFeatures/FinishFeatures_Add.md), [FinishFeatures.Item](../FinishFeatures/FinishFeatures_Item.md)

## Derived Classes

[FinishFeatureProxy](../FinishFeatureProxy/FinishFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finish Feature Creation](../../sample-programs/FinishFeatureCreation_Sample.md) | This sample demonstrates how to create a finish feature. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |