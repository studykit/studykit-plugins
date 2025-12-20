# MarkFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

MarkFeature Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MarkFeature/MarkFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../MarkFeature/MarkFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../MarkFeature/MarkFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../MarkFeature/MarkFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [ResultEdges](../MarkFeature/MarkFeature_ResultEdges.md) | Method that gets the result edges created by this mark feature. |
| [SetAffectedBodies](../MarkFeature/MarkFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../MarkFeature/MarkFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../MarkFeature/MarkFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../MarkFeature/MarkFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../MarkFeature/MarkFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../MarkFeature/MarkFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../MarkFeature/MarkFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MarkFeature/MarkFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../MarkFeature/MarkFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../MarkFeature/MarkFeature_Definition.md) | Property that gets and sets the MarkDefinition object associated with this feature. |
| [ExtendedName](../MarkFeature/MarkFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../MarkFeature/MarkFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../MarkFeature/MarkFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../MarkFeature/MarkFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../MarkFeature/MarkFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../MarkFeature/MarkFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../MarkFeature/MarkFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../MarkFeature/MarkFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../MarkFeature/MarkFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../MarkFeature/MarkFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../MarkFeature/MarkFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../MarkFeature/MarkFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../MarkFeature/MarkFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../MarkFeature/MarkFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../MarkFeature/MarkFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MarkDefinition.Parent](../MarkDefinition/MarkDefinition_Parent.md), [MarkFeatureProxy.NativeObject](../MarkFeatureProxy/MarkFeatureProxy_NativeObject.md), [MarkFeatures.Add](../MarkFeatures/MarkFeatures_Add.md), [MarkFeatures.Item](../MarkFeatures/MarkFeatures_Item.md)

## Derived Classes

[MarkFeatureProxy](../MarkFeatureProxy/MarkFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mark feature creation sample](../../sample-programs/MarkFeatureCreationSample_Sample.md) | This sample demonstrates how to create a mark feature in part document. |

## Version

Introduced in version 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |