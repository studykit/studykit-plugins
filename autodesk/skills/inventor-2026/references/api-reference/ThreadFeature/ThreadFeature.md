# ThreadFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ThreadFeature object represents thread modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ThreadFeature/ThreadFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ThreadFeature/ThreadFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ThreadFeature/ThreadFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ThreadFeature/ThreadFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ThreadFeature/ThreadFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ThreadFeature/ThreadFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ThreadFeature/ThreadFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetThreadDepth](../ThreadFeature/ThreadFeature_SetThreadDepth.md) | Method that sets the thread depth for the thread feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ThreadFeature/ThreadFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ThreadFeature/ThreadFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ThreadFeature/ThreadFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ThreadFeature/ThreadFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ThreadFeature/ThreadFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ThreadFeature/ThreadFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [DirectionReversed](../ThreadFeature/ThreadFeature_DirectionReversed.md) | Property that gets and sets whether the direction of the thread is in the default direction or reversed. |
| [DisplayInModel](../ThreadFeature/ThreadFeature_DisplayInModel.md) | Property that gets and sets whether the threads are displayed on the part when viewed in any of the 3d environments, i.e. part or assembly. |
| [ExtendedName](../ThreadFeature/ThreadFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ThreadFeature/ThreadFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ThreadFeature/ThreadFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [FullDepth](../ThreadFeature/ThreadFeature_FullDepth.md) | Property that gets and sets whether the threads extend the full length of the cylinder or cone. If True, they extend the full length. If False, the depth is controlled by the value of the ThreadDepth property |
| [HealthStatus](../ThreadFeature/ThreadFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ThreadFeature/ThreadFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ThreadFeature/ThreadFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ThreadFeature/ThreadFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ThreadFeature/ThreadFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ThreadFeature/ThreadFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ThreadFeature/ThreadFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ThreadFeature/ThreadFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ThreadFeature/ThreadFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StartEdge](../ThreadFeature/ThreadFeature_StartEdge.md) | Property that returns the thread depth is measured from. |
| [Suppressed](../ThreadFeature/ThreadFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ThreadFeature/ThreadFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [ThreadDepth](../ThreadFeature/ThreadFeature_ThreadDepth.md) | Property that returns the parameter that controls the depth of the thread. Even though the parameter for the thread depth is always created and accessible through this property, it is only used in the case where the FullDepth property is False. |
| [ThreadedFace](../ThreadFeature/ThreadFeature_ThreadedFace.md) | Property that returns the set of that the thread is applied to. Usually this is just the face that was input for application of the thread feature, but in the case where the original face has been cut by subsequent features, the multiple resulting faces will be returned. |
| [ThreadInfo](../ThreadFeature/ThreadFeature_ThreadInfo.md) | Property that gets and sets the thread information of the feature. This can return either a StandardThreadInfo or TaperedThreadInfo object. The ThreadType property can be used to determine the type before getting the thread info. |
| [ThreadInfoType](../ThreadFeature/ThreadFeature_ThreadInfoType.md) | Property that returns a indicating the thread type. |
| [ThreadOffset](../ThreadFeature/ThreadFeature_ThreadOffset.md) | Property that gets the parameter that controls the offset value of the thread. The offset is the distance along the axis of the cylinder or cone from the start edge to the start of the thread. |
| [Type](../ThreadFeature/ThreadFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ThreadFeatureProxy.NativeObject](../ThreadFeatureProxy/ThreadFeatureProxy_NativeObject.md), [ThreadFeatures.Add](../ThreadFeatures/ThreadFeatures_Add.md), [ThreadFeatures.Item](../ThreadFeatures/ThreadFeatures_Item.md)

## Derived Classes

[ThreadFeatureProxy](../ThreadFeatureProxy/ThreadFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 5
