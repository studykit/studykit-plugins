# DirectEditFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

Part DirectEdit Feature Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DirectEditFeature/DirectEditFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../DirectEditFeature/DirectEditFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../DirectEditFeature/DirectEditFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../DirectEditFeature/DirectEditFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../DirectEditFeature/DirectEditFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../DirectEditFeature/DirectEditFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../DirectEditFeature/DirectEditFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../DirectEditFeature/DirectEditFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../DirectEditFeature/DirectEditFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../DirectEditFeature/DirectEditFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../DirectEditFeature/DirectEditFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DirectEditFeature/DirectEditFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../DirectEditFeature/DirectEditFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [DirectEditOperations](../DirectEditFeature/DirectEditFeature_DirectEditOperations.md) | Gets all the operations of this direct edit feature. |
| [ExtendedName](../DirectEditFeature/DirectEditFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../DirectEditFeature/DirectEditFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../DirectEditFeature/DirectEditFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../DirectEditFeature/DirectEditFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../DirectEditFeature/DirectEditFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../DirectEditFeature/DirectEditFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../DirectEditFeature/DirectEditFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../DirectEditFeature/DirectEditFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../DirectEditFeature/DirectEditFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../DirectEditFeature/DirectEditFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../DirectEditFeature/DirectEditFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../DirectEditFeature/DirectEditFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../DirectEditFeature/DirectEditFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../DirectEditFeature/DirectEditFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../DirectEditFeature/DirectEditFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DirectEditDeleteOperation.Parent](../DirectEditDeleteOperation/DirectEditDeleteOperation_Parent.md), [DirectEditDeleteOperationProxy.Parent](../DirectEditDeleteOperationProxy/DirectEditDeleteOperationProxy_Parent.md), [DirectEditFeatureProxy.NativeObject](../DirectEditFeatureProxy/DirectEditFeatureProxy_NativeObject.md), [DirectEditFeatures.Item](../DirectEditFeatures/DirectEditFeatures_Item.md), [DirectEditMoveOperation.Parent](../DirectEditMoveOperation/DirectEditMoveOperation_Parent.md), [DirectEditMoveOperationProxy.Parent](../DirectEditMoveOperationProxy/DirectEditMoveOperationProxy_Parent.md), [DirectEditOperation.Parent](../DirectEditOperation/DirectEditOperation_Parent.md), [DirectEditOperationProxy.Parent](../DirectEditOperationProxy/DirectEditOperationProxy_Parent.md), [DirectEditRotateOperation.Parent](../DirectEditRotateOperation/DirectEditRotateOperation_Parent.md), [DirectEditRotateOperationProxy.Parent](../DirectEditRotateOperationProxy/DirectEditRotateOperationProxy_Parent.md), [DirectEditScaleOperation.Parent](../DirectEditScaleOperation/DirectEditScaleOperation_Parent.md), [DirectEditScaleOperationProxy.Parent](../DirectEditScaleOperationProxy/DirectEditScaleOperationProxy_Parent.md), [DirectEditSizeOperation.Parent](../DirectEditSizeOperation/DirectEditSizeOperation_Parent.md), [DirectEditSizeOperationProxy.Parent](../DirectEditSizeOperationProxy/DirectEditSizeOperationProxy_Parent.md)

## Derived Classes

[DirectEditFeatureProxy](../DirectEditFeatureProxy/DirectEditFeatureProxy.md)

## Version

Introduced in version 2015
