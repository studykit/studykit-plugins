# FilletFeatureProxy Object

Derived from: [FilletFeature](../FilletFeature/FilletFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FilletFeatureProxy/FilletFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../FilletFeatureProxy/FilletFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../FilletFeatureProxy/FilletFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../FilletFeatureProxy/FilletFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../FilletFeatureProxy/FilletFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../FilletFeatureProxy/FilletFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../FilletFeatureProxy/FilletFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../FilletFeatureProxy/FilletFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../FilletFeatureProxy/FilletFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../FilletFeatureProxy/FilletFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../FilletFeatureProxy/FilletFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FilletFeatureProxy/FilletFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutomaticEdgeChain](../FilletFeatureProxy/FilletFeatureProxy_AutomaticEdgeChain.md) | Property that returns whether or not to use all tangentially connected edges. A value of True indicates that automatic edge chaining of tangentially connected edges should be performed. |
| [ConsumeInputs](../FilletFeatureProxy/FilletFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../FilletFeatureProxy/FilletFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../FilletFeatureProxy/FilletFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../FilletFeatureProxy/FilletFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../FilletFeatureProxy/FilletFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [FilletDefinition](../FilletFeatureProxy/FilletFeatureProxy_FilletDefinition.md) | Property that returns the object which defines the various input that was used to create the fillet feature. |
| [HealthStatus](../FilletFeatureProxy/FilletFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../FilletFeatureProxy/FilletFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../FilletFeatureProxy/FilletFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../FilletFeatureProxy/FilletFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../FilletFeatureProxy/FilletFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../FilletFeatureProxy/FilletFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../FilletFeatureProxy/FilletFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../FilletFeatureProxy/FilletFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PreserveAllFeatures](../FilletFeatureProxy/FilletFeatureProxy_PreserveAllFeatures.md) | Property that specifies whether all other features that intersect with the feature are checked and their intersections calculated during this feature operation. If False, only the objects that are part of this feature operation are calculated. |
| [RangeBox](../FilletFeatureProxy/FilletFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [RollAlongSharpEdges](../FilletFeatureProxy/FilletFeatureProxy_RollAlongSharpEdges.md) | Property that specifies the solution method for fillets when the specified radius would cause adjacent faces to be extended. When True, the radius will be varied when necessary to preserve the edges of adjacent faces. When False, a constant radius will be maintained and adjacent faces extended as needed. |
| [RollingBallWherePossible](../FilletFeatureProxy/FilletFeatureProxy_RollingBallWherePossible.md) | Property that specifies the corner style for the fillet. When True, the fillet will be defined as if a ball had been rolled along the edge and around the corners. When False, a continuous tangent transition between fillets in sharp corners is created. |
| [Shared](../FilletFeatureProxy/FilletFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SmoothRadiusTransition](../FilletFeatureProxy/FilletFeatureProxy_SmoothRadiusTransition.md) | Property that applies only to variable radius fillets and specifies whether the transition between different radii is to be smooth. For a smooth transition there is a gradual blending transition between the defined radius points and the transitions are tangent. Without a smooth transition, a linear transition is used between radius points. |
| [Suppressed](../FilletFeatureProxy/FilletFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../FilletFeatureProxy/FilletFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../FilletFeatureProxy/FilletFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
