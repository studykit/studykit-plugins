# ThreadFeatureProxy Object

Derived from: [ThreadFeature](../ThreadFeature/ThreadFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ThreadFeatureProxy/ThreadFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ThreadFeatureProxy/ThreadFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ThreadFeatureProxy/ThreadFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ThreadFeatureProxy/ThreadFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ThreadFeatureProxy/ThreadFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ThreadFeatureProxy/ThreadFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ThreadFeatureProxy/ThreadFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetThreadDepth](../ThreadFeatureProxy/ThreadFeatureProxy_SetThreadDepth.md) | Method that sets the thread depth for the thread feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ThreadFeatureProxy/ThreadFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ThreadFeatureProxy/ThreadFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ThreadFeatureProxy/ThreadFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ThreadFeatureProxy/ThreadFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ThreadFeatureProxy/ThreadFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ThreadFeatureProxy/ThreadFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../ThreadFeatureProxy/ThreadFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DirectionReversed](../ThreadFeatureProxy/ThreadFeatureProxy_DirectionReversed.md) | Property that gets and sets whether the direction of the thread is in the default direction or reversed. |
| [DisplayInModel](../ThreadFeatureProxy/ThreadFeatureProxy_DisplayInModel.md) | Property that gets and sets whether the threads are displayed on the part when viewed in any of the 3d environments, i.e. part or assembly. |
| [ExtendedName](../ThreadFeatureProxy/ThreadFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ThreadFeatureProxy/ThreadFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ThreadFeatureProxy/ThreadFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [FullDepth](../ThreadFeatureProxy/ThreadFeatureProxy_FullDepth.md) | Property that gets and sets whether the threads extend the full length of the cylinder or cone. If True, they extend the full length. If False, the depth is controlled by the value of the ThreadDepth property |
| [HealthStatus](../ThreadFeatureProxy/ThreadFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ThreadFeatureProxy/ThreadFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ThreadFeatureProxy/ThreadFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../ThreadFeatureProxy/ThreadFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../ThreadFeatureProxy/ThreadFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ThreadFeatureProxy/ThreadFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ThreadFeatureProxy/ThreadFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ThreadFeatureProxy/ThreadFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ThreadFeatureProxy/ThreadFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ThreadFeatureProxy/ThreadFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StartEdge](../ThreadFeatureProxy/ThreadFeatureProxy_StartEdge.md) | Property that returns the thread depth is measured from. |
| [Suppressed](../ThreadFeatureProxy/ThreadFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ThreadFeatureProxy/ThreadFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [ThreadDepth](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadDepth.md) | Property that returns the parameter that controls the depth of the thread. Even though the parameter for the thread depth is always created and accessible through this property, it is only used in the case where the FullDepth property is False. |
| [ThreadedFace](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadedFace.md) | Property that returns the set of that the thread is applied to. Usually this is just the face that was input for application of the thread feature, but in the case where the original face has been cut by subsequent features, the multiple resulting faces will be returned. |
| [ThreadInfo](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadInfo.md) | Property that gets and sets the thread information of the feature. This can return either a StandardThreadInfo or TaperedThreadInfo object. The ThreadType property can be used to determine the type before getting the thread info. |
| [ThreadInfoType](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadInfoType.md) | Property that returns a indicating the thread type. |
| [ThreadOffset](../ThreadFeatureProxy/ThreadFeatureProxy_ThreadOffset.md) | Property that gets the parameter that controls the offset value of the thread. The offset is the distance along the axis of the cylinder or cone from the start edge to the start of the thread. |
| [Type](../ThreadFeatureProxy/ThreadFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
