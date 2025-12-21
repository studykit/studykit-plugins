# ThickenFeatureProxy Object

Derived from: [ThickenFeature](../ThickenFeature/ThickenFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ThickenFeatureProxy/ThickenFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ThickenFeatureProxy/ThickenFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ThickenFeatureProxy/ThickenFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ThickenFeatureProxy/ThickenFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ThickenFeatureProxy/ThickenFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ThickenFeatureProxy/ThickenFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ThickenFeatureProxy/ThickenFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ThickenFeatureProxy/ThickenFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ThickenFeatureProxy/ThickenFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ThickenFeatureProxy/ThickenFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ThickenFeatureProxy/ThickenFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApproximationOptimized](../ThickenFeatureProxy/ThickenFeatureProxy_ApproximationOptimized.md) | Gets and sets whether the approximation is optimized. |
| [ApproximationTolerance](../ThickenFeatureProxy/ThickenFeatureProxy_ApproximationTolerance.md) | Gets and set the approximation tolerance. |
| [ApproximationType](../ThickenFeatureProxy/ThickenFeatureProxy_ApproximationType.md) | Gets and sets the approximation method used for the feature. |
| [AttributeSets](../ThickenFeatureProxy/ThickenFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutomaticBlending](../ThickenFeatureProxy/ThickenFeatureProxy_AutomaticBlending.md) | Property that returns whether the offset operation should propagate to adjacent tangent faces. |
| [AutomaticFaceChain](../ThickenFeatureProxy/ThickenFeatureProxy_AutomaticFaceChain.md) | Property that gets whether or not to perform chaining of tangent continuous faces. |
| [ConsumeInputs](../ThickenFeatureProxy/ThickenFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../ThickenFeatureProxy/ThickenFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CreateVerticalSurfaces](../ThickenFeatureProxy/ThickenFeatureProxy_CreateVerticalSurfaces.md) | Property that gets whether or not to create vertical or "side" faces connecting the offset faces to the original work surface. |
| [Direction](../ThickenFeatureProxy/ThickenFeatureProxy_Direction.md) | Gets and sets the distance direction of the feature. |
| [Distance](../ThickenFeatureProxy/ThickenFeatureProxy_Distance.md) | Property that returns the parameter that controls the thickness of the Thickness feature or the distance of the Offset feature. |
| [ExtendedName](../ThickenFeatureProxy/ThickenFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ThickenFeatureProxy/ThickenFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ThickenFeatureProxy/ThickenFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ThickenFeatureProxy/ThickenFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputFaces](../ThickenFeatureProxy/ThickenFeatureProxy_InputFaces.md) | Specifies the faces used to create the feature. |
| [IsOwnedByFeature](../ThickenFeatureProxy/ThickenFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ThickenFeatureProxy/ThickenFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../ThickenFeatureProxy/ThickenFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Operation](../ThickenFeatureProxy/ThickenFeatureProxy_Operation.md) | Gets and sets the type of operation used to add the feature to the model. |
| [OwnedBy](../ThickenFeatureProxy/ThickenFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ThickenFeatureProxy/ThickenFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ThickenFeatureProxy/ThickenFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ThickenFeatureProxy/ThickenFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ThickenFeatureProxy/ThickenFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ThickenFeatureProxy/ThickenFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ThickenFeatureProxy/ThickenFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ThickenFeatureProxy/ThickenFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ThickenFeatureProxy/ThickenFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
